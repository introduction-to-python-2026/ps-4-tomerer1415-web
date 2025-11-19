def split_at_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            number_str = ''
            while i < len(formula) and formula[i].isdigit():
                number_str += formula[i]
                i += 1
            return prefix, int(number_str)
    return formula, 1

def split_before_each_uppercases(formula):
    parts = []
    start = 0
    for i, char in enumerate(formula[1:], start=1):
        if char.isupper():
            parts.append(formula[start:i])
            start = i
    parts.append(formula[start:])
    return parts
