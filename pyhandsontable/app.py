from jinja2 import Environment, PackageLoader
from threading import Timer
import os
from collections import OrderedDict
from IPython.display import IFrame

env = Environment(
    loader=PackageLoader('pyhandsontable', 'templates')
)


def generate_html(data, **kwargs):
    if not data:
        raise ValueError('Please input some data.')

    columns = list()
    if isinstance(data[0], (dict, OrderedDict)):
        colHeaders = kwargs.get('colHeaders', data[0].keys())
    else:
        colHeaders = kwargs.get('colHeaders', range(len(data[0])))

    for header in colHeaders:
        entry = {'data': header}
        if 'renderers' in kwargs.keys():
            entry['renderer'] = kwargs['renderers'].get(header)
        columns.append(entry)

    colHeaders = kwargs.get('colHeaders', True)
    rowHeaders = kwargs.get('rowHeaders', True)

    template = env.get_template('sheet.html')
    return template.render(data=data,
                           columns=columns, colHeaders=colHeaders, rowHeaders=rowHeaders,
                           **kwargs)


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
