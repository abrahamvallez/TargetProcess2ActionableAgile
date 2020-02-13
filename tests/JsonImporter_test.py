from src.JsonImporter import JsonImporter


def test_import_return_a_dictionary():
    importer = JsonImporter()
    dic_returned = importer.import_from_file('tests/json_examples/response.json')
    assert type(dic_returned) == dict

