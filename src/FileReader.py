import json

class FileReader:

    file_path: string

    def get_data_from_file(self, file_path: string):
        with open(file_path) as file:
            file_data = json.load(file)
        return file_data


