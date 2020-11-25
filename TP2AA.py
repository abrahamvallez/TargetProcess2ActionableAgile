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

FEATURES_STATES = [
    'Open',
    'Refinement',
    'Dev',
    'Done',
]

KEYS = [
    'ID',
    'link',
    'title'
]

ATTRIBUTE_FIELDS = [
    'cycleTime'
]


def main(importer: JsonImporter, exporter: CsvExporter, formatter: DataFormatter, json_file_path: str, ElementType: str):
    if ElementType in ['feature', 'f']:
        states = FEATURES_STATES
        element_key = 'currentFeature'
    else:
        states = USER_STORIES_STATES
        element_key = 'currentUserStory'
    list_of_data = importer.import_from_file(json_file_path)
    formatted_data = formatter.format_from_raw_TP_data(list_of_data, states, element_key)
    exporter.export_to_csv(formatted_data, KEYS + states + ATTRIBUTE_FIELDS)

if __name__ == "__main__":
    importer = JsonImporter()
    exporter = CsvExporter()
    formatter = DataFormatter()

    main(importer, exporter, formatter, str(sys.argv[1]), str(sys.argv[2]))


