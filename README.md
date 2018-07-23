# pyhandsontable

[![Build Status](https://travis-ci.org/patarapolw/pyhandsontable.svg?branch=master)](https://travis-ci.org/patarapolw/pyhandsontable)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI license](https://img.shields.io/pypi/l/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)

View a 2-D array, probably from [pyexcel](https://github.com/pyexcel/pyexcel) in Jupyter Notebook, and export to `*.html`.

## Installation

```commandline
pip install pyhandsontable
```

## Usage

```python
>>> from pyhandsontable import generate_html, view_table
>>> view_table(width=800, height=500, data=data_matrix, **kwargs)
```

## Acceptable kwargs

- title: title of the HTML file
- maxColWidth: maximum column width. Set to 200.
- css: url of the Handsontable CSS
- js: url of the Handsontable Javascript
- css_custom: your custom CSS
- js_pre: Javascript before rendering the table (but after most other things.)
- js_post: Javascript after rendering the table.
- config: add additional config as defined in https://docs.handsontable.com/pro/5.0.0/tutorial-introduction.html
  - This will override the default config (per key basis) which are:
  
```javascript
{
  rowHeaders: true,
  colHeaders: true,
  dropdownMenu: true,
  filters: true,
  modifyColWidth: function(width, col){
    if(width > maxColWidth) return maxColWidth;
  }
}
```
