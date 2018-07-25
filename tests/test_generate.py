import pytest
from pathlib import Path

from pyhandsontable import generate_html


@pytest.mark.parametrize('kwargs', [
    {'data': [[1, 2, 3], [4, 5, 6]]},
    {'data': [[False]]},
    {'data': [[1, 2, 3], [4, 5, 6]], 'config': {'rowHeaders': False}},
    {'data': [[1, 2, 3], [4, 5, 6]], 'config': {'colHeaders': False}}
])
def test_generate(kwargs, request):
    with Path('tests/output').joinpath(request.node.name + '.html').open('w') as f:
        f.write(generate_html(**kwargs))
