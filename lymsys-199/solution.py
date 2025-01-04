# file: solution.py
def parse_delimited_numbers(input_string: str) -> list[str]:
    """Parse a string as a list of numbers delimited by integers."""
    delimiter = "1"
    result = []
    while(input_string):
        split_array = input_string.split(delimiter, 1)
        if(len(split_array) < 2):
            result.append(split_array[0])
            break
        if(split_array[0] != ""):
            result.append(split_array[0])
        input_string = split_array[1]
        delimiter = str(int(delimiter) + 1)

    return result


if __name__ == "__main__":
    numbers = parse_delimited_numbers("3162433224558")
    print(numbers)
