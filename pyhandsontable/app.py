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


def view_table(data, width=800, height=500, **kwargs):
    # A TemporaryFile does not work with Jupyter Notebook

    html_file = 'temp.handsontable.html'
    try:
        with open(html_file, 'w') as f:
            f.write(generate_html(data=data, width=width, height=height, **kwargs))

        return IFrame(html_file, width=width, height=height)
    finally:
        Timer(5, os.unlink, args=[html_file]).start()
