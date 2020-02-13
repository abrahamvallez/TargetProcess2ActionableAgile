from src.DataFormatter import DataFormatter


def test_formatted_data_has_a_field_named_ID():
    data_formatter = DataFormatter()
    data_list = [{"id": 1, "Date1": 2, "Date2": 3},
                 {"id": 2, "Date1": 2, "Date2": 3},
                 {"id": 3, "Date1": 2, "Date2": 3},
                 {"id": 4, "Date1": 2, "Date2": 3}]

    formatted_data_list = data_formatter.format_to_TP(data_list)
    assert formatted_data_list[0].get('ID'), "Id index should be exist"


def test_formatted_data_has_same_ids_from_data_list():
    data_formatter = DataFormatter()
    data_list = [{"id": 1, "Date1": 2, "Date2": 3},
                 {"id": 2, "Date1": 2, "Date2": 3},
                 {"id": 3, "Date1": 2, "Date2": 3},
                 {"id": 4, "Date1": 2, "Date2": 3}]

    formatted_data_list = data_formatter.format_to_TP(data_list)
    assert formatted_data_list[0].get('ID') == 1, "Id index should be exist"
    assert formatted_data_list[1].get('ID') == 2, "Id index should be exist"
    assert formatted_data_list[2].get('ID') == 3, "Id index should be exist"
