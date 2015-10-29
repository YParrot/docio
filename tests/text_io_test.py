import os
import tempfile

import docio

test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'text')


def test_extract():
    text_io = docio.TextIO(test_file_path)
    assert text_io.extract() == ["This is a test text."]


def test_substitute():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        dest_file_path = f.name
    text_io = docio.TextIO(test_file_path)
    text_io.substitute(["New text."])
    text_io.save(dest_file_path)

    with open(dest_file_path) as f:
        assert f.read() == "New text."
