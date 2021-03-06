from jinja2 import Environment, PackageLoader
from threading import Timer
import os
from collections import OrderedDict
from IPython.display import IFrame

env = Environment(
    loader=PackageLoader('pyhandsontable', 'templates')
)


def generate_html(data, **kwargs):
    renderers = kwargs.pop('renderers', dict())
    config = kwargs.pop('config', dict())

    if isinstance(data[0], (dict, OrderedDict)):
        headers = sum((list(d.keys()) for d in data), list())
        headers = [h for i, h in enumerate(headers) if h not in headers[:i]]
        config['colHeaders'] = list(headers)
    else:
        headers = range(len(data[0]))

    columns = []
    for header in headers:
        columnData = {
            'data': header,
            'renderer': 'jsonRenderer'
        }
        if header in renderers.keys():
            columnData['renderer'] = renderers.get(header)
        columns.append(columnData)

    template = env.get_template('sheet.html')

    return template.render(data=data, columns=columns, config=config, **kwargs)


def view_table(data, width=1000, height=500,
               filename='temp.handsontable.html', autodelete=True, **kwargs):
    # A TemporaryFile does not work with Jupyter Notebook

    try:
        with open(filename, 'w') as f:
            f.write(generate_html(data=data, width=width, height=height, **kwargs))

        return IFrame(filename, width=width, height=height)
    finally:
        if autodelete:
            Timer(5, os.unlink, args=[filename]).start()
