from src.ActionableAgileCSVExporter import ActionableAgileCSVExporter


def test_return_a_dictionary():
    exporter = ActionableAgileCSVExporter()
    dic_returned = exporter.export_from_file('tests/json_examples/response.json')
    assert type(dic_returned) == dict
