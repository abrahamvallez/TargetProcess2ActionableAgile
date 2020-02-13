import sys

from src.CsvExporter import CsvExporter
from src.JsonImporter import JsonImporter


def main(importer: JsonImporter, exporter: CsvExporter, json_file_path: str):
    list_of_data = importer.import_from_file(json_file_path)
    return exporter.export_to_csv(list_of_data)

if __name__ == "__main__":
    importer = JsonImporter()
    exporter = CsvExporter()
    main(importer, exporter, str(sys.argv[1]))
