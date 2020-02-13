import csv


class CsvExporter:

    def export_to_csv(self, user_stories_data: list):
        csv_headers = user_stories_data[0].keys()
        csv_file_path = "jsonfiles/UserStories.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(user_stories_data)
        return csv_file_path
