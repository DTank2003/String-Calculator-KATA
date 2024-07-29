# string_calculator.py
import re

def add(numbers):
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter_spec, numbers = numbers.split("\n", 1)
        if delimiter_spec.startswith("//[") and delimiter_spec.endswith("]"):
            delimiters = re.findall(r'\[(.*?)\]', delimiter_spec)
            delimiter = '|'.join(map(re.escape, delimiters))
        else:
            delimiter = delimiter_spec[2:]
    else:
        delimiter = ","

    nums = [int(n) for n in re.split(f"[{delimiter}\n]", numbers)]
    negatives = [n for n in nums if n < 0]
    
    if negatives:
        raise ValueError(f"negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(n for n in nums if n <= 1000)