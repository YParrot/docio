import os
import tempfile

import docio

test_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'resources',
    'xml.xml'
)


def test_extract():
    io = docio.XMLIO(test_file_path)
    assert io.extract() == ['\n    hoge\n    ', 'foo', 'bar', '\n    piyo\n  ']


def test_swap():
    io = docio.XMLIO(test_file_path)
    io.swap(['A', 'B', None, 'D'])
    with tempfile.NamedTemporaryFile(delete=False) as f:
        dest_file_path = f.name
    io.save(dest_file_path)

    new_io = docio.XMLIO(dest_file_path)
    assert new_io.extract() == ['A', 'B', 'bar', 'D']
