from src.CsvExporter import CsvExporter


def test_export_return_a_path_of_file():
    data_list = [{"id": 1, "Date1": 2, "Date2": 3},
                 {"id": 2, "Date1": 2, "Date2": 3},
                 {"id": 3, "Date1": 2, "Date2": 3},
                 {"id": 4, "Date1": 2, "Date2": 3}]
    exporter = CsvExporter()
    file_path = exporter.export_to_csv(data_list)
    assert type(file_path) == str, "file path returned should be a string"
