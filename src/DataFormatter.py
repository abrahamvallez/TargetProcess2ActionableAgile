class DataFormatter():
    def format_to_TP(self, data_list) -> list:
        formatted_data: list = []
        i = 0
        for row in data_list:
            formatted_row = {'ID': row['id']}
            formatted_data.append(formatted_row)
            i += 1

        return formatted_data
