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
- maxColWidth: maximum column width. (Default: 200)
- autodelete: whether the temporary HTML file should be autodeleted. (Default: True)
- filename: filename of the temporary HTML file (default: 'temp.handsontable.html')
- css: url of the Handsontable CSS
- js: url of the Handsontable Javascript
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

## Post-creation editing of the HTML

You might try `from bs4 import BeautifulSoup`:

```python
        config = {
            'colHeaders': ['id'] + list(CardTuple._fields),
            'columns': [
                {'data': 0},
                {'data': 1, 'renderer': 'markdownRenderer'},
                {'data': 2, 'renderer': 'markdownRenderer'},
                {'data': 3},
                {'data': 4}
            ]
        }
        
        filename = 'temp.handsontable.html'
        try:
            table = view_table(data=([[i] + list(record.to_formatted_tuple())
                                 for i, record in self.find(keyword_regex, tags)]),
                               width=width,
                               height=height,
                               config=config,
                               filename=filename,
                               autodelete=False)
            with open(filename, 'r') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            div = soup.new_tag('div')

            js_markdown = soup.new_tag('script',
                                       src='https://cdn.rawgit.com/showdownjs/showdown/1.8.6/dist/showdown.min.js')
            js_custom = soup.new_tag('script')

            with open('gflashcards/js/markdown-hot.js') as f:
                js_custom.append(f.read())

            div.append(js_markdown)
            div.append(js_custom)

            script_tag = soup.find('script')
            soup.body.insert(soup.body.contents.index(script_tag) + 1, div)

            with open(filename, 'w') as f:
                f.write(str(soup))

            return table
        finally:
            Timer(5, os.unlink, args=[filename]).start()
```

[Source](https://github.com/patarapolw/gflashcards/blob/master/gflashcards/app.py#L93)

## Screenshots

<img src="https://github.com/patarapolw/pyhandsontable/blob/master/screenshots/0.png" />

## Related projects

- https://github.com/patarapolw/gflashcards
- https://github.com/patarapolw/jupyter-flashcards
