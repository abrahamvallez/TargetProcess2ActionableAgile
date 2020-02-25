from src.DataFormatter import DataFormatter


def test_formatted_data_has_a_field_named_ID():
    data_formatter = DataFormatter()
    data_list = [
        {"date": "2020-02-16T10:11:50.79", "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": "2020-02-17T10:11:50.79", "currentUserStory": {"id": 2, "name": "name2"}, "entityState": {"name": "In Progress"}},
        {"date": "2020-02-18T10:11:50.79", "currentUserStory": {"id": 3, "name": "name2"}, "entityState": {"name": "Done"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    assert formatted_data_dict.get(1).get('ID'), "Id index should be exist"


def test_formatted_data_has_same_ids_from_data_list():
    ids = [1, 2, 3]
    data_formatter = DataFormatter()
    data_list = [
        {"date": "2020-02-16T10:11:50.79", "currentUserStory": {"id": ids[0], "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": "2020-02-17T10:11:50.79", "currentUserStory": {"id": ids[1], "name": "name2"}, "entityState": {"name": "Open"}},
        {"date": "2020-02-18T10:11:50.79", "currentUserStory": {"id": ids[2], "name": "name2"}, "entityState": {"name": "Open"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)

    assert formatted_data_dict.get(1).get('ID') == ids[0], "First element Id should be 1"
    assert formatted_data_dict.get(2).get('ID') == ids[1], "Second element Id should be 1"
    assert formatted_data_dict.get(3).get('ID') == ids[2], "Third element Id should be 1"


def test_dates_are_grouped_in_same_row_by_id():
    data_formatter = DataFormatter()
    dates: list = [
        "2020-02-16T10:11:50.79",
        "2020-02-17T10:11:50.79",
        "2020-02-18T10:11:50.79"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": dates[1], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "In Progress"}},
        {"date": dates[2], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Done"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)

    values_in_formatted_data: list = formatted_data_dict.get(1).values()
    assert dates[0] in values_in_formatted_data, "Date1 should be in same row"
    assert dates[1] in values_in_formatted_data, "Date2 should be in same row"
    assert dates[2] in values_in_formatted_data, "Date3 should be in same row"


def test_create_a_new_row_if_id_is_new():
    data_formatter = DataFormatter()
    dates: list = [
        "2020-02-16T10:11:50.79",
        "2020-02-17T10:11:50.79",
        "2020-02-18T10:11:50.79"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": dates[1], "currentUserStory": {"id": 2, "name": "name1"}, "entityState": {"name": "In Progress"}},
        {"date": dates[2], "currentUserStory": {"id": 2, "name": "name1"}, "entityState": {"name": "Done"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)

    values_in_formatted_data: list = formatted_data_dict.get(2).values()
    assert dates[1] in values_in_formatted_data, "Date2 should be in same row"
    assert dates[2] in values_in_formatted_data, "Date3 should be in same row"


def test_dates_are_classified_by_state():
    data_formatter = DataFormatter()
    dates: list = [
        "2020-02-16T10:11:50.79",
        "2020-02-17T10:11:50.79",
        "2020-02-18T10:11:50.79"]
    states: list = ["Open", "In Progress", "Done"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[2]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)

    user_story_1_row: dict = formatted_data_dict.get(1)
    assert user_story_1_row.get(states[0]) == dates[0], "Open date should be Date1"
    assert user_story_1_row.get(states[1]) == dates[1], "Open date should be Date2"
    assert user_story_1_row.get(states[2]) == dates[2], "Open date should be Date3"


def test_keep_only_one_state_when_back_and_forth():
    data_formatter = DataFormatter()
    dates: list = [
        "2020-02-16T10:11:50.79",
        "2020-02-17T10:17:11.97",
        "2020-02-18T10:13:35.86"]
    states: list = ["Open", "In Progress"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[0]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(1)

    assert list(user_story_1_row.keys()) == ["ID", "Open", "In Progress"], "Should have only two states"


def test_keep_earlier_date_for_same_state_in_workflow_when_back_and_forth():
    data_formatter = DataFormatter()
    dates: list = ["2020-02-16T10:11:50.79",
                   "2020-02-17T10:17:11.97",
                   "2020-02-18T10:13:35.86",
                   "2020-02-19T10:17:11.97"]
    states: list = ["Open", "In Progress"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[3], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": states[1]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(1)

    assert user_story_1_row.get(states[0]) == '2020-02-16T10:11:50.79'
    assert user_story_1_row.get(states[1]) == '2020-02-17T10:17:11.97'


def test_keep_late_state_in_workflow_when_back_and_forth_one_step():
    data_formatter = DataFormatter()
    dates: list = ["2020-02-16T10:11:50.79",
                   "2020-02-17T10:17:11.97",
                   "2020-02-18T10:20:35.86",
                   "2020-02-21T10:14:35.86",
                   "2020-02-22T10:17:11.97"]
    states: list = ["Open", "In Progress", "Pending DoD", "Done"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}},
        {"date": dates[3], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[2]}},
        {"date": dates[4], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(10)

    assert user_story_1_row[states[3]] == '2020-02-18T10:20:35.86'
    assert states[2] not in list(user_story_1_row.keys())


def test_keep_late_state_in_workflow_when_back_and_forth_many_states():
    data_formatter = DataFormatter()
    dates: list = ["2020-02-16T10:11:50.79",
                   "2020-02-17T10:17:11.97",
                   "2020-02-18T10:20:35.86",
                   "2020-02-21T10:14:35.86",
                   "2020-02-22T10:14:35.86",
                   "2020-02-23T10:14:35.86"]
    states: list = ["Open", "In Progress", "Code Review", "Pending DoD", "Done", "Released/Finished"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[5]}},
        {"date": dates[3], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[2]}},
        {"date": dates[4], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}},
        {"date": dates[5], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[5]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(10)

    assert user_story_1_row[states[5]] == '2020-02-18T10:20:35.86', "late state should be Released/Finished"
    assert states[2] not in list(user_story_1_row.keys()), "back and forth should not be saved"
    assert states[3] not in list(user_story_1_row.keys()), "back and forth should not be saved"


def test_keep_late_state_in_workflow_when_back_and_forth_to_repeated_state():
    data_formatter = DataFormatter()
    dates: list = ["2020-02-16T10:11:50.79",
                   "2020-02-17T10:17:11.97",
                   "2020-02-18T10:20:35.86",
                   "2020-02-21T10:14:35.86",
                   "2020-02-23T10:17:11.97"]
    states: list = ["Open", "In Progress", "Pending DoD", "Done"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[2]}},
        {"date": dates[3], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}},
        {"date": dates[4], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[2]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(10)

    assert user_story_1_row[states[3]] == '2020-02-21T10:14:35.86', "late state should be earlier Done"
    assert user_story_1_row[states[2]] == '2020-02-18T10:20:35.86', "Pending DoD should be earlier date"


def test_keep_state_when_wrong_back_and_forth_in_less_than_one_day():
    data_formatter = DataFormatter()
    dates: list = ["2020-02-16T10:11:50.79",
                   "2020-02-17T10:17:11.97",
                   "2020-02-18T10:20:35.86",
                   "2020-02-18T10:21:35.86",
                   "2020-02-22T10:17:11.97"]
    states: list = ["Open", "In Progress", "Pending DoD", "Done"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[0]}},
        {"date": dates[1], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[1]}},
        {"date": dates[2], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}},
        {"date": dates[3], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[2]}},
        {"date": dates[4], "currentUserStory": {"id": 10, "name": "name1"}, "entityState": {"name": states[3]}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    user_story_1_row: dict = formatted_data_dict.get(10)

    assert user_story_1_row.get(states[2]) == '2020-02-18T10:21:35.86', "Pending Dod should be saved"
    assert user_story_1_row.get(states[3]) == '2020-02-22T10:17:11.97', "Wrong Done state should be deleted"
