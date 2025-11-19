def split_at_digit(formula):
    digit_location = 1

    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        # No digit found
        return formula, 1
    else:
        prefix = formula[:digit_location]
        number = int(formula[digit_location:])
        return prefix, number

def split_before_each_uppercases(formula):
    # Initialize indices and the result list
    start = 0
    split_formula = []

    # Loop through the string starting from the second character
    for end in range(1, len(formula)):
        if formula[end].isupper():
            # Append the substring from start to current end
            split_formula.append(formula[start:end])
            # Update start to current end
            start = end

    # Append the last part of the string
    split_formula.append(formula[start:])

    return split_formula
