class DataFormatter():
    def format_to_TP(self, data_list: list) -> dict:
        formatted_data: dict = {}
        i = 0
        for row in data_list:
            user_story_data = row["currentUserStory"]
            date = row["date"]
            formatted_row :dict = formatted_data.get(user_story_data['id'])
            if formatted_row:
                formatted_row.update({i: date})
            else:
                formatted_row = {'ID': user_story_data['id'], 'date': date}
                formatted_data[user_story_data['id']] = formatted_row
            i += 1

        return formatted_data
