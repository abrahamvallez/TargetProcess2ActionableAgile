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
    'ID'
]


class DataFormatter:

    def format_to_TP(self, data_list: list) -> dict:
        formatted_dict: dict = {}

        for row in data_list:
            user_story_id = row["currentUserStory"]['id']
            user_story_state = row["entityState"]["name"]
            date = row["date"]

            formatted_row: dict = formatted_dict.get(user_story_id)
            if user_story_state in USER_STORIES_STATES:
                if formatted_row:
                    formatted_row.update({user_story_state: date})
                else:
                    formatted_row = {'ID': user_story_id, user_story_state: date}
                    formatted_dict[user_story_id] = formatted_row

        return formatted_dict
