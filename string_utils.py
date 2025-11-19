def split_at_first_digit(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    # This check MUST be outside the loop
    if digit_location == len(formula):
        return formula, 1

    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number


def split_before_each_uppercase(formula):
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

# Test your code with your input
formula = "Ir6"
print(split_at_first_digit(formula))
