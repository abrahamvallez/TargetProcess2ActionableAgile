from src.JsonImporter import JsonImporter


def test_export_return_a_path_of_file():
    dictionary = [{"data1": 1, "data2": 2, "data3": 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3}]
    exporter = JsonImporter()
    file_path = exporter.export_to_csv(dictionary)
    assert type(file_path) == str, "file path returned should be a string"
