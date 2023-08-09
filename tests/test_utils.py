import src.utils as ut

# result for test_get_list_from_json()
result_1 = [
  {
    "word": "qwerty",
    "number": 12345,
    "dict": {
      "bool": True
    }
  },
  {
    "word": "asdfg",
    "number": 67890
  }
]


def test_get_list_from_json():
    assert ut.get_list_from_json('tests/test_files/test_list.json') == result_1


# input for test_remove_invalid_data_from_list()
input_list_1 = [
    {
        "id": 123,
        "date": "2021-01-01"
    },
    {
        "id": 123
    },
    {}
]

# result for test_remove_invalid_data_from_list()
result_list_1 = [
    {
        "id": 123,
        "date": "2021-01-01"
    }
]


def test_remove_invalid_data_from_list():
    assert ut.remove_invalid_data_from_list(input_list_1) == result_list_1


# input for test_sort_operations_by_date()
input_list_2 = [
    {
        "id": 123,
        "date": "2020-05-05"
    },
    {
        "id": 234,
        "date": "2021-01-01"
    },
]

# result for test_sort_operations_by_date()
result_list_2 = [
    {
        "id": 234,
        "date": "2021-01-01"
    },
    {
        "id": 123,
        "date": "2020-05-05"
    }
]


def test_sort_operations_by_date():
    assert ut.sort_operations_by_date(input_list_2) == result_list_2


input_list_3 = [
    {
        "id": 1,
        "state": "EXECUTED"
    },
    {
        "id": 2,
        "state": "CANCELED"
    },
    {
        "id": 3,
        "state": "CANCELED"
    },
]

result_list_3_1 = [
    {
        "id": 1,
        "state": "EXECUTED"
    },
    {
        "id": 2,
        "state": "CANCELED"
    }
]

result_list_3_2 = [
    {
        "id": 1,
        "state": "EXECUTED"
    }
]

result_list_3_3 = [
    {
        "id": 2,
        "state": "CANCELED"
    },
    {
        "id": 3,
        "state": "CANCELED"
    },
]


def test_get_latest_operations():
    assert ut.get_latest_operations(input_list_3, 2, 'ANY') == result_list_3_1
    assert ut.get_latest_operations(input_list_3, 2, 'EXECUTED') == result_list_3_2
    assert ut.get_latest_operations(input_list_3, 2, 'CANCELED') == result_list_3_3


def test_format_date():
    assert ut.format_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_format_requisites():
    assert ut.format_requisites("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert ut.format_requisites("Счет 64686473678894779589") == "Счет **9589"
    assert ut.format_requisites("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
