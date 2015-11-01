import os
import tempfile

import docio

test_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'resources',
    'office_open_xml_presentation.pptx'
)


def test_flow():
    io = docio.OfficeOpenXMLPresentationIO(test_file_path)
    assert io.extract() == ['Title', 'Body', 'Second slide']

    io.swap(['A', None, 'C'])
    with tempfile.NamedTemporaryFile(delete=False) as f:
        dest_file_path = f.name
    io.save(dest_file_path)

    new_io = docio.OfficeOpenXMLPresentationIO(dest_file_path)
    assert new_io.extract() == ['A', 'Body', 'C']
