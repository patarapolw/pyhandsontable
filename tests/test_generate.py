import pytest
from pathlib import Path

from pyhandsontable import generate_html


@pytest.mark.parametrize('kwargs', [
    {'data': []}
])
def test_generate(kwargs, request):
    with Path('tests/output').joinpath(request.node.name + '.html').open('w') as f:
        f.write(generate_html(**kwargs))
