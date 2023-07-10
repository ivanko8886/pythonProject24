import json


def print_last_operations():
    with open('operations.json','r',encoding='utf-8') as file:
        data = json.load(file)
        executed_operations = [op for op in data if 'state' in op and op['state'] == 'EXECUTED']
        sorted_operations = sorted(executed_operations, key=lambda op: op['date'], reverse=True)
        for operation in sorted_operations[:5]:
            date = operation['date'].split('T')[0].replace('-', '.')
            description = operation['description']
            from_account = operation.get('from', 'Unknown')
            to_account = operation.get('to', 'Unknown')
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']
            masked_from_account = '**' + from_account[-4:]
            masked_to_account = to_account[:4] + ' ' + to_account[4:-4] + ' **** ' + to_account[-4:]

            print(f'{date} {description}')
            print(f'{masked_from_account} -> {masked_to_account}')
            print(f'{amount} {currency}\n')


print_last_operations()