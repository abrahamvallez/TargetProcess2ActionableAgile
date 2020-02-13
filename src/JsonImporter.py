import json


class JsonImporter:
    def import_from_file(self, file_path):
        with open(file_path) as file_object:
            user_stories = json.load(file_object)
        return user_stories['items']

