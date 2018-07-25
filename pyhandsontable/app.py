from jinja2 import Environment, PackageLoader
from threading import Timer
import os
from IPython.display import IFrame

env = Environment(
    loader=PackageLoader('pyhandsontable', 'templates')
)


def generate_html(data, **kwargs):
    template = env.get_template('sheet.html')

    return template.render(data=data, **kwargs)


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
