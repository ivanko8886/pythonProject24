import json
from io import StringIO
import sys
import pytest
from main import print_last_operations
def test_print_last_operations(mocker):

    operations = [
    {
    "date": "2022-01-01T00:00:00",
    "description": "Operation 1",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "EXECUTED",
    "operationAmount": {
    "amount": 100,
    "currency": {
    "name": "USD"
    }
    }
    },
    {
    "date": "2022-01-02T00:00:00",
    "description": "Operation 2",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "EXECUTED",
    "operationAmount": {
    "amount": 200,
    "currency": {
    "name": "EUR"
    }
    }
    },
    {
    "date": "2022-01-03T00:00:00",
    "description": "Operation 3",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "EXECUTED",
    "operationAmount": {
    "amount": 300,
    "currency": {
    "name": "GBP"
    }
    }
    },
    {
    "date": "2022-01-04T00:00:00",
    "description": "Operation 4",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "EXECUTED",
    "operationAmount": {
    "amount": 400,
    "currency": {
    "name": "JPY"
    }
    }
    },
    {
    "date": "2022-01-05T00:00:00",
    "description": "Operation 5",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "EXECUTED",
    "operationAmount": {
    "amount": 500,
    "currency": {
    "name": "AUD"
    }
    }
    },
    {
    "date": "2022-01-06T00:00:00",
    "description": "Operation 6",
    "from": "1111222233334444",
    "to": "5555666677778888",
    "state": "PENDING",
    "operationAmount": {
    "amount": 600,
    "currency": {
    "name": "CAD"
    }
    }
    }
    ]



    mocker.patch('builtins.open', return_value=StringIO(json.dumps(operations)))

# Заменяем стандартный вывод на StringIO для получения результатов печати
captured_output = StringIO()
sys.stdout = captured_output

# Вызываем функцию
print_last_operations()

# Получаем результаты печати
output = captured_output.getvalue()

# Проверяем, что результаты печати соответствуют ожидаемому выводу
expected_output = "2022.01.05 Operation 5\n**4444 -> 5555 6666 **** 8888\n500 AUD\n\n" + \
                 "2022.01.04 Operation 4\n**4444 -> 5555 6666 **** 8888\n400 JPY\n\n" + \
                 "2022.01.03 Operation 3\n**4444 -> 5555 6666 **** 8888\n300 GBP\n\n" + \
                 "2022.01.02 Operation 2\n**4444 -> 5555 6666 **** 8888\n200 EUR\n\n" + \
                 "2022.01.01 Operation 1\n**4444 -> 5555 6666 **** 8888\n100 USD\n\n"
assert output == expected_output

# Возвращаем стандартный вывод
sys.stdout = sys.__stdout__

pytest.main()