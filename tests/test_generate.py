import pytest
from pathlib import Path

from pyhandsontable import generate_html


@pytest.mark.parametrize('kwargs', [
    {'data': []},
    {'data': [[1, 2, 3]]},
    {'data': [[False]]},
    {'data': [], 'config': {'rowHeaders': False}}
])
def test_generate(kwargs, request):
    with Path('tests/output').joinpath(request.node.name + '.html').open('w') as f:
        f.write(generate_html(**kwargs))
