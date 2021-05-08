"""Task04 - Armstrong number"""


def is_armstrong(number: int) -> bool:
    """Checking if input number is Armstrong number"""
    str_num = str(number)
    list_of_num = [int(str_num[i]) for i in range(len(str(number)))]
    potential_armstrong = sum(map(lambda x: x ** len(str(number)), list_of_num))
    return number == potential_armstrong
