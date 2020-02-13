import json
import csv


class JsonImporter:
    def import_from_file(self, file_path):
        with open(file_path) as file_object:
            user_stories = json.load(file_object)
        return user_stories

    def export_to_csv(self, user_stories_data: list):
        csv_headers = user_stories_data[0].keys()
        csv_file_path = "jsonfiles/UserStories.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(user_stories_data)
        return csv_file_path
