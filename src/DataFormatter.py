import dateutil.parser

LINK_URL = "http://targetprocess.voxelgroup.net/TargetProcess2/entity/"

DAYS_ERROR_ALLOWED = 1


class DataFormatter:

    def format_from_raw_TP_data(self, user_stories_list: list, states: list, element_key: str) -> dict:
        formatted_dict: dict = {}

        for row_from_list in user_stories_list:
            self.manage_one_row(formatted_dict, row_from_list, states, element_key)

        return formatted_dict

    def manage_one_row(self, formatted_dict, row_to_format: dict, states: list, element_key: str):
        user_story_state = row_to_format["entityState"]["name"]

        if user_story_state in states:
            formatted_row: dict = formatted_dict.get(row_to_format[element_key]['id'])
            if not formatted_row:
                self.add_new_user_story(formatted_dict, row_to_format, element_key)
            else:
                self.update_user_story(formatted_row, row_to_format, states)

    def add_new_user_story(self, formatted_dict, new_user_story_data, element_key: str):
        new_user_story = self.format_new_user_story(new_user_story_data, element_key)
        formatted_dict[new_user_story['ID']] = new_user_story

    def update_user_story(self, formatted_row, user_story_data, states: list):
        user_story_state = user_story_data["entityState"]["name"]
        updated_date = user_story_data["date"]

        old_date = formatted_row.get(user_story_state)
        if old_date and old_date > updated_date:
            formatted_row.update({user_story_state: updated_date})
        if not old_date:
            state_where_come_from = self.is_a_step_back(formatted_row, user_story_data, states)
            if (state_where_come_from
                    and self.is_an_error_in_workflow_update(formatted_row.get(state_where_come_from), updated_date)):
                formatted_row.pop(state_where_come_from)
                formatted_row.update({user_story_state: updated_date})
            if not state_where_come_from:
                formatted_row.update({user_story_state: updated_date})

    def format_new_user_story(self, row_from_data: dict, element_key: str) -> dict:
        user_story_state = row_from_data["entityState"]["name"]
        if row_from_data.get(element_key).get('cycleTime'):
            cycle_time = round(row_from_data[element_key]['cycleTime'])
        else:
            cycle_time = None

        return {
            'ID': row_from_data[element_key]['id'],
            'link': LINK_URL + str(row_from_data[element_key]['id']),
            'title': row_from_data[element_key]['name'],
            'cycleTime': cycle_time,
            user_story_state: row_from_data["date"]
        }

    def is_an_error_in_workflow_update(self, state_where_come_from_date, updated_date) -> bool:
        return (dateutil.parser.parse(updated_date) -
                dateutil.parser.parse(state_where_come_from_date)).days < DAYS_ERROR_ALLOWED

    def is_a_step_back(self, formatted_row: dict, row_from_data: dict, states: list):
        state_id = states.index(row_from_data["entityState"]["name"])
        states_before = states[:state_id]
        new_state_changed_date = row_from_data["date"]

        for state in states:
            state_date_saved = formatted_row.get(state)
            if (state not in states_before
                    and state_date_saved
                    and new_state_changed_date > state_date_saved):
                return state

        return False
