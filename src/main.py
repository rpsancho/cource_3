import utils


JSON_PATH = '../json/operations.json'


def main():
    op_list = utils.get_list_from_json(JSON_PATH)

    op_list = utils.remove_invalid_data_from_list(op_list)
    op_list = utils.sort_operations_by_date(op_list)
    op_list = utils.get_latest_operations(op_list, 5, 'EXECUTED')

    for op in op_list:
        date_str = utils.format_date(op['date'])
        if 'from' in op:
            from_str = utils.format_requisites(op['from']) + ' -> '
        else:
            from_str = ''
        to_str = utils.format_requisites(op['to'])
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        print(f"{date_str} {op['description']}")
        print(f"{from_str}{to_str}")
        print(f"{amount} {currency}\n")


if __name__ == "__main__":
    main()
