def split_at_first_digit(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number


def split_before_each_uppercase(formula):
    result = []
    current = ""

    for char in formula:
        if char.isupper() and current:
            result.append(current)
            current = char
        else:
            current += char

    result.append(current)
    return result
