from src.DataFormatter import DataFormatter


def test_formatted_data_has_a_field_named_ID():
    data_formatter = DataFormatter()
    data_list = [
        {"date": "Date1", "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": "Date2", "currentUserStory": {"id": 2, "name": "name2"}, "entityState": {"name": "Open"}},
        {"date": "Date2", "currentUserStory": {"id": 3, "name": "name2"}, "entityState": {"name": "Open"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    assert formatted_data_dict.get(1).get('ID'), "Id index should be exist"


def test_formatted_data_has_same_ids_from_data_list():
    ids = [1, 2, 3]
    data_formatter = DataFormatter()
    data_list = [
        {"date": "Date1", "currentUserStory": {"id": ids[0], "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": "Date2", "currentUserStory": {"id": ids[1], "name": "name2"}, "entityState": {"name": "Open"}},
        {"date": "Date2", "currentUserStory": {"id": ids[2], "name": "name2"}, "entityState": {"name": "Open"}}
    ]

    formatted_data_dict = data_formatter.format_to_TP(data_list)
    assert formatted_data_dict.get(1).get('ID') == ids[0], "First element Id should be 1"
    assert formatted_data_dict.get(2).get('ID') == ids[1], "Second element Id should be 1"
    assert formatted_data_dict.get(3).get('ID') == ids[2], "Third element Id should be 1"

def test_dates_are_grouped_same_row_by_id():
    data_formatter = DataFormatter()
    dates: list = ["Date1", "Date2", "Date3"]
    data_list = [
        {"date": dates[0], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Open"}},
        {"date": dates[1], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "WIP"}},
        {"date": dates[2], "currentUserStory": {"id": 1, "name": "name1"}, "entityState": {"name": "Done"}}
    ]
    formatted_data_dict = data_formatter.format_to_TP(data_list)
    values_in_formatted_data: list = formatted_data_dict.get(1).values()
    assert dates[0] in values_in_formatted_data, "Date1 should be in same row"
    assert dates[1] in values_in_formatted_data, "Date2 should be in same row"
    assert dates[2] in values_in_formatted_data, "Date2 should be in same row"

