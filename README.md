# pyhandsontable

[![Build Status](https://travis-ci.org/patarapolw/pyhandsontable.svg?branch=master)](https://travis-ci.org/patarapolw/pyhandsontable)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI license](https://img.shields.io/pypi/l/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)

View a list of JSON-serializable dictionaries or a 2-D array, in HandsOnTable, in Jupyter Notebook.

Nested JSON renderer is also supported and is default. Image and markdown renderers are possible, but has to be extended.

## Installation

```commandline
pip install pyhandsontable
```

## Usage

In Jupyter Notebook,

```python
>>> from pyhandsontable import PagedViewer
>>> viewer = PagedViewer(data=data_matrix, **kwargs)
>>> viewer
'A Handsontable is shown in Jupyter Notebook.'
>>> viewer.view(-1)
'The last page is shown.'
>>> viewer.previous()
'The previous page (i-1) is shown.'
>>> viewer.next()
'The next page (i+1) is shown.'
```

Data matrix can be either a list of lists (2-D array) or a list of dictionaries.

It is also possible to view all entries at once, but it could be bad, if there are too many rows.

```python
>>> from pyhandsontable import view_table
>>> view_table(data_matrix, **kwargs)
```

## Acceptable kwargs

- height: height of the window (default: 500)
- width: width of the window (default: 1000)
- title: title of the HTML file
- maxColWidth: maximum column width. (Default: 200)
- renderers: the renderers to use in generating the columns (see below.)
- autodelete: whether the temporary HTML file should be autodeleted. (Default: True)
- filename: filename of the temporary HTML file (default: 'temp.handsontable.html')
- css: url of the Handsontable CSS
- js: url of the Handsontable Javascript
- config: add additional config as defined in https://docs.handsontable.com/pro/5.0.0/tutorial-introduction.html
  - This will override the default config (per key basis) which are:
  
```javascript
{
    data: data,
    rowHeaders: true,
    colHeaders: true,
    columns: columns,
    manualColumnResize: true,
    manualRowResize: true,
    renderAllRows: true,
    modifyColWidth: (width, col)=>{
        if(width > maxColWidth) return maxColWidth;
    },
    afterRenderer: (td, row, column, prop, value, cellProperties)=>{
        td.innerHTML = td.innerHTML.slice(0, config.charLimit || 5000);
    }
}
```

`renderers` example, if your data is a 2-D array:

```python
{
    1: 'html',
    2: 'html'
}
```

or if your data is list of dict:

```python
{
    "front": 'html',
    "back": 'html'
}
```

## Enabling Image, HTML and Markdown renderer

This can be done in Python side, by converting everything to HTML. Just use [any markdown for Python library](https://github.com/Python-Markdown/markdown).

```python
from markdown import markdown
import base64
image_html = f'<img src="{image_url}" width=100 />'
image_html2 = f'<img src="data:image/png;base64,{base64.b64encode(image_bytes).decode()}" />'
markdown_html = markdown(markdown_raw)
```

Any then,

```python
PagedViewer(data=data_matrix, renderers={
    "image_field": "html",
    "html_field": "html",
    "markdown_field": "html"
})
```

## Screenshots

![1.png](/screenshots/1.png?raw=true)
![0.png](/screenshots/0.png?raw=true)

## Related projects

- https://github.com/patarapolw/tinydb-viewer

## License

> By installing, copying, or otherwise using this software, you agree to be bound by the terms
> of its General Software License Terms ("Terms") outlined in a file "handsontable-pro-general-terms.pdf"
> available in the main directory of the software repository.
> This software is copyrighted and protected by copyright laws and international treaties.
> 
> You shall obtain a commercial license for this software at handsontable.com.
