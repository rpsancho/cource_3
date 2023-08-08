import json


def get_list_from_json(file_path):
    with open(file_path, 'r', encoding='UTF-8') as fp:
        data = json.load(fp)
    return data


def remove_invalid_data_from_list(src_list):
    valid_list = []
    for item in src_list:
        if not item:
            continue
        if not item['date']:
            continue
        valid_list.append(item)
    return valid_list


def sort_operations_by_date(src_list):
    return sorted(src_list, key=lambda x: x['date'], reverse=True)


def get_latest_operations(src_list, quantity=10, state='ANY'):
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
    return date_str[8:10]+'.'+date_str[5:7]+'.'+date_str[0:4]


def format_requisites(req_str):
    req_list = req_str.split(' ')
    number = req_list[-1]
    if req_list[0] == "Счет":
        hidden_number = f"**{number[-4:]}"
    else:
        hidden_number = f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"
    req_list[-1] = hidden_number
    return " ".join(req_list)
