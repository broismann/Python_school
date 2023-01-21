def is_float(input_str):
    counter = 0
    for i in input_str:
        if not i.isdigit() and i != "." and i != "-":
            return False
        elif i == ".":
            counter += 1
    return counter <= 1

def analyze_input(input_str):
    if input_str.isdigit():
        return "It is positive integer: " + input_str
    elif input_str[0] == "-" and input_str[1:].isdigit():
        return "It is negative integer: " + input_str
    elif is_float(input_str):
        if input_str[0] == "-":
            return "It is negative fractional number: " + input_str
        else:
            return "It is positive fractional number: " + input_str
    else:
        return "Sorry, incorrect number, try again: " + input_str

while True:
    user_input = input("Please enter any number or 'exit', 'quit', 'e', 'q' to quit: ").lower()
    if user_input in ["exit", "quit", "e", "q"]:
        break
    else:
        print(analyze_input(user_input))
