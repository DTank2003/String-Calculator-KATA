# string_calculator.py
def add(numbers):
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter, numbers = numbers.split("\n", 1)
        delimiter = delimiter[2:]
    else:
        delimiter = ","

    return sum(int(n) for n in numbers.replace("\n", delimiter).split(delimiter))