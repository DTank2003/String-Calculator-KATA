# string_calculator.py
def add(numbers):
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter, numbers = numbers.split("\n", 1)
        delimiter = delimiter[2:]
    else:
        delimiter = ","

    nums = [int(n) for n in numbers.replace("\n", delimiter).split(delimiter)]
    negatives = [n for n in nums if n < 0]
    
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(nums)