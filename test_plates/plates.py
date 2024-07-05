def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (is_valid_length(s) and
            starts_with_two_letters(s) and
            contains_only_alphanumeric(s) and
            has_numbers_at_end(s) and
            first_number_not_zero(s))


def is_valid_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[0:2].isalpha()


def contains_only_alphanumeric(s):
    return s.isalnum()


def has_numbers_at_end(s):
    first_digit_index = -1
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break

    if first_digit_index == -1:
        return True

    for char in s[first_digit_index:]:
        if not char.isdigit():
            return False

    return True


def first_number_not_zero(s):
    for char in s:
        if char.isdigit():
            return char != '0'
    return True

if __name__ == "__main__":
    main()
