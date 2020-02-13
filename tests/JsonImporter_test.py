import pytest

from src.JsonImporter import JsonImporter


def test_import_return_a_list():
    importer = JsonImporter()
    list_returned = importer.import_from_file('tests/json_examples/response.json')
    assert type(list_returned) == list, "should return a list"


def test_remove_item_field():
    importer = JsonImporter()
    list_returned: list
    list_returned = importer.import_from_file('tests/json_examples/response.json')
    with pytest.raises(ValueError):
        list_returned.index('Items')
