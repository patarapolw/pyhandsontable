import pytest

from pyhandsontable import generate_html


@pytest.mark.parametrize('kwargs', [
    {'data': []}
])
def test_generate(kwargs, request):
    with open('tests/output/' + request.node.name + '.html', 'w') as f:
        f.write(generate_html(**kwargs))
