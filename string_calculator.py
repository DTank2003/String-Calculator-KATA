# string_calculator.py
def add(numbers):
    if numbers == "":
        return 0
    return sum(int(n) for n in numbers.replace("\n", ",").split(","))