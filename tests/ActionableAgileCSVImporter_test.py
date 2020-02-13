from src.ActionableAgileCSVImporter import ActionableAgileCSVImporter


def test_import_return_a_dictionary():
    importer = ActionableAgileCSVImporter()
    dic_returned = importer.import_from_file('tests/json_examples/response.json')
    assert type(dic_returned) == dict


def test_export_return_a_path_of_file():
    dictionary = [{"data1": 1, "data2": 2, "data3": 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3}]
    exporter = ActionableAgileCSVImporter()
    file_path = exporter.export_to_csv(dictionary)
    assert type(file_path) == str, "file path returned should be a string"
