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
        user_story_state_from_data = row_from_data["entityState"]["name"]

        if user_story_state_from_data in USER_STORIES_STATES:
            formatted_row: dict = formatted_dict.get(row_from_data["currentUserStory"]['id'])
            if not formatted_row:
                self.add_new_user_story(formatted_dict, row_from_data)
            else:
                self.update_user_story(formatted_row, row_from_data)

    def add_new_user_story(self, formatted_dict, row_from_data):
        new_user_story = self.format_new_user_story(row_from_data)
        formatted_dict[new_user_story['ID']] = new_user_story

    def update_user_story(self, formatted_row, row_from_data):
        user_story_state = row_from_data["entityState"]["name"]
        new_state_changed_date = row_from_data["date"]
        state_date_saved = formatted_row.get(user_story_state)

        if ((not state_date_saved or state_date_saved > new_state_changed_date)
                and not self.is_a_step_back(formatted_row, row_from_data)):
            formatted_row.update({user_story_state: new_state_changed_date})

    def format_new_user_story(self, row_from_data: dict) -> dict:
        user_story_id = row_from_data["currentUserStory"]['id']
        user_story_state = row_from_data["entityState"]["name"]
        date_in_row_from_data = row_from_data["date"]
        return {
            'ID': user_story_id,
            user_story_state: date_in_row_from_data
        }

    def is_a_step_back(self, formatted_row: dict, row_from_data: dict) -> bool:
        state_id = USER_STORIES_STATES.index(row_from_data["entityState"]["name"])
        states_before = USER_STORIES_STATES[0:state_id - 1]
        new_state_changed_date = row_from_data["date"]

        for state in USER_STORIES_STATES:
            state_date_saved = formatted_row.get(state)
            if (state_date_saved
                    and state not in states_before
                    and new_state_changed_date > state_date_saved):
                return True

        return False

