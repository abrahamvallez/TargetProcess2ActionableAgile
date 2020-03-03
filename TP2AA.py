import sys

from src.CsvExporter import CsvExporter
from src.DataFormatter import DataFormatter
from src.JsonImporter import JsonImporter

USER_STORIES_STATES = [
    'Open',
    'Ready',
    'Planned',
    'In Progress',
    'Code Review',
    'Pending DoD',
    'Done',
    'Released/Finished'
]

KEYS = [
    'ID',
    'link',
    'title'
]

ATTRIBUTE_FIELDS = [
    'cycleTime'
]


def main(importer: JsonImporter, exporter: CsvExporter, formatter: DataFormatter, json_file_path: str):
    list_of_data = importer.import_from_file(json_file_path)
    formatted_data = formatter.format_to_TP(list_of_data)
    csv_file_path = exporter.export_to_csv(formatted_data, KEYS + USER_STORIES_STATES + ATTRIBUTE_FIELDS)

if __name__ == "__main__":
    importer = JsonImporter()
    exporter = CsvExporter()
    formatter = DataFormatter()

    main(importer, exporter, formatter, str(sys.argv[1]))


