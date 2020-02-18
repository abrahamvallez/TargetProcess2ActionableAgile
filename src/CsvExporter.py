import csv


class CsvExporter:

    def export_to_csv(self, user_stories_data: dict):
        random_element = user_stories_data.popitem()
        csv_headers = random_element[1].keys()
        print(csv_headers)
        csv_file_path = "jsonfiles/UserStories.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(list(user_stories_data.values()))
        return csv_file_path
