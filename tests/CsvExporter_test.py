from src.CsvExporter import CsvExporter


def test_export_return_a_path_of_file():
    keys = ['ID', "Open", "Done"]
    data_dict = {"1": {"ID": 1, "Open": 2, "Done": 3},
                 "2": {"ID": 2, "Open": 2, "Done": 3},
                 "3": {"ID": 3, "Open": 2, "Done": 3},
                 "4": {"ID": 4, "Open": 2, "Done": 3}}
    exporter = CsvExporter()
    file_path = exporter.export_to_csv(data_dict, keys)
    assert type(file_path) == str, "file path returned should be a string"
