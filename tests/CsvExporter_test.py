from src.CsvExporter import CsvExporter


def test_export_return_a_path_of_file():
    data_list = [{"data1": 1, "data2": 2, "data3": 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3},
                  {'data1': 1, 'data2': 2, 'data3': 3}]
    exporter = CsvExporter()
    file_path = exporter.export_to_csv(data_list)
    assert type(file_path) == str, "file path returned should be a string"
