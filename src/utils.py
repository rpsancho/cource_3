import json


def get_list_from_json(file_path):
    """
    read json file and convert into python data structure
    :param file_path: path to json file
    :return: data
    """
    with open(file_path, 'r', encoding='UTF-8') as fp:
        data = json.load(fp)
    return data


def remove_invalid_data_from_list(src_list):
    """
    remove invalid items from src_list and return valid_list
    :param src_list: source list
    :return: valid_list
    """
    valid_list = []
    for item in src_list:
        if not item:
            continue
        if 'date' not in item:
            continue
        valid_list.append(item)
    return valid_list


def sort_operations_by_date(src_list):
    """
    sort items in src_list by date from newest to oldest
    and return new sorted list
    :param src_list: source list
    :return: sorted list
    """
    return sorted(src_list, key=lambda x: x['date'], reverse=True)


def get_latest_operations(src_list, quantity=10, state='ANY'):
    """

    :param src_list: source list
    :param quantity: quantity of latest operations
    :param state: get values 'ANY' (default), 'EXECUTED', 'CANCELED'
    filter results by state
    :return: filtered list of operations
    """
    if state == 'ANY':
        return src_list[0:quantity]

    if state in ['EXECUTED', 'CANCELED']:
        result_list = []
        cnt = 0
        for item in src_list:
            if item['state'] == state:
                result_list.append(item)
                cnt += 1
                if cnt == quantity:
                    break
        return result_list


def format_date(date_str):
    """
    convert date string to YYYY.MM.DD format
    :param date_str: source date string
    :return: formatted date string
    """
    return date_str[8:10]+'.'+date_str[5:7]+'.'+date_str[0:4]


def format_requisites(req_str):
    """
    hide digits in card numbers or bank accounts
    :param req_str: source string with requisites
    :return: formatted string with hidden requisites
    """
    req_list = req_str.split(' ')
    number = req_list[-1]
    if req_list[0] == "Счет":
        hidden_number = f"**{number[-4:]}"
    else:
        hidden_number = f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
    req_list[-1] = hidden_number
    return " ".join(req_list)
