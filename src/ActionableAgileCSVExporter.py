import json


class ActionableAgileCSVExporter:
    def export_from_file(self, file_path):

        with open(file_path) as file_object:
            userstories = json.load(file_object)
        return userstories
