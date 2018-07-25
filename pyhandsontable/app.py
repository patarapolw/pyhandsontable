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

    if isinstance(data[0], (dict, OrderedDict)):
        headers = data[0].keys()
    else:
        headers = range(len(data[0]))

    columns = []
    for header in headers:
        columnData = {
            'data': header
        }
        if header in renderers.keys():
            columnData['renderer'] = renderers.get(header)
        columns.append(columnData)

    template = env.get_template('sheet.html')

    return template.render(data=data, columns=columns, **kwargs)


def view_table(data, width=800, height=500,
               filename='temp.handsontable.html', autodelete=True, **kwargs):
    # A TemporaryFile does not work with Jupyter Notebook

    try:
        with open(filename, 'w') as f:
            f.write(generate_html(data=data, width=width, height=height, **kwargs))

        return IFrame(filename, width=width, height=height)
    finally:
        if autodelete:
            Timer(5, os.unlink, args=[filename]).start()
