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

        for row_from_data in data_list:
            self.format_row(formatted_dict, row_from_data)

        return formatted_dict

    def format_row(self, formatted_dict, row_from_data: dict):
        user_story_state = row_from_data["entityState"]["name"]

        if user_story_state in USER_STORIES_STATES:
            formatted_row: dict = formatted_dict.get(row_from_data["currentUserStory"]['id'])
            if formatted_row and not self.is_a_step_back(formatted_row, row_from_data):
                self.update_user_story(formatted_row, row_from_data)
            elif not formatted_row:
                self.add_new_user_story(formatted_dict, row_from_data)

    def add_new_user_story(self, formatted_dict, row_from_data):
        new_user_story = self.format_new_user_story(row_from_data)
        formatted_dict[new_user_story['ID']] = new_user_story

    def update_user_story(self, formatted_row, row_from_data):
        user_story_state = row_from_data["entityState"]["name"]
        date = row_from_data["date"]
        if not formatted_row.get(user_story_state) or formatted_row.get(user_story_state) > date:
            formatted_row.update({user_story_state: date})

    def format_new_user_story(self, row_from_data: dict) -> dict:
        user_story_id = row_from_data["currentUserStory"]['id']
        user_story_state = row_from_data["entityState"]["name"]
        date = row_from_data["date"]
        return {
            'ID': user_story_id,
            user_story_state: date
        }

    def is_a_step_back(self, formatted_row: dict, row_from_data: dict) -> bool:
        state_id = USER_STORIES_STATES.index(row_from_data["entityState"]["name"])

        states_before = USER_STORIES_STATES[0:state_id-1]
        for state in USER_STORIES_STATES:
            if (formatted_row.get(state)
                    and formatted_row.get(state) < row_from_data["date"]
                    and state not in states_before):
                return True

        return False




