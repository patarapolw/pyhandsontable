# pyhandsontable

[![Build Status](https://travis-ci.org/patarapolw/pyhandsontable.svg?branch=master)](https://travis-ci.org/patarapolw/pyhandsontable)
[![PyPI version shields.io](https://img.shields.io/pypi/v/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI license](https://img.shields.io/pypi/l/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyhandsontable.svg)](https://pypi.python.org/pypi/pyhandsontable/)

View a list of dictionaries or a 2-D array, in HandsOnTable, in Jupyter Notebook.

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
  data: data
  rowHeaders: true,
  colHeaders: true,
  dropdownMenu: true,
  filters: true,
  modifyColWidth: function(width, col){
    if(width > maxColWidth) return maxColWidth;
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

## Post-creation editing of the HTML

You might try `from bs4 import BeautifulSoup`:

        renderers = {
            1: 'markdownRenderer',
            2: 'markdownRenderer'
        }
        config = {
            'colHeaders': ['id'] + list(CardTuple._fields),
            'rowHeaders': False
        }

        filename = 'temp.handsontable.html'
        try:
            table = view_table(data=([[i] + list(record.to_formatted_tuple())
                                      for i, record in self.find(keyword_regex, tags)]),
                               width=width,
                               height=height,
                               renderers=renderers,
                               config=config,
                               filename=filename,
                               autodelete=False)
            with open(filename, 'r') as f:
                soup = BeautifulSoup(f.read(), 'html5lib')

            div = soup.new_tag('div')

            js_markdown = soup.new_tag('script',
                                       src='https://cdn.rawgit.com/showdownjs/showdown/1.8.6/dist/showdown.min.js')
            js_custom = soup.new_tag('script')

            with open('gflashcards/js/markdown-hot.js') as f:
                js_custom.append(f.read())

            div.append(js_markdown)
            div.append(js_custom)

            script_tag = soup.find('script', {'id': 'generateHandsontable'})
            soup.body.insert(soup.body.contents.index(script_tag), div)

            with open(filename, 'w') as f:
                f.write(str(soup))

            return table
        finally:
            Timer(5, os.unlink, args=[filename]).start()

[Source](https://github.com/patarapolw/gflashcards/blob/master/gflashcards/app.py#L93)

## Screenshots

![0.png](/screenshots/0.png?raw=true)
![1.png](/screenshots/1.png?raw=true)

## Related projects

- https://github.com/patarapolw/gflashcards
- https://github.com/patarapolw/jupyter-flashcards
