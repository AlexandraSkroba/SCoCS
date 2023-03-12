import constants


def calculate(num1, num2, operator):
    match operator:
        case constants.ADDITION:
            return num1 + num2

        case constants.DIVISION:
            if num2 == 0:
                return 'Division by zero is FORBIDDEN!'
            else:
                return num1 / num2

        case constants.SUBTRACTION:
            return num1 - num2

        case constants.MULTIPLICATION:
            return num1 * num2

        case _:
            return "Wrong operator! Enter 'add', 'div', 'sub' or 'mul'"
