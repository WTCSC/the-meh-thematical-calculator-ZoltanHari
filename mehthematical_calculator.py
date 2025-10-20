import sys 
import time

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_number(prompt):
    while True:
        type_out(prompt)
        user_input = input().strip()
        try:
            return float(user_input)
        except ValueError:
            type_out("That’s not a number. Figures. Try again")

def get_operation(prompt):
    while True:
        type_out(prompt)
        operation = input().strip()
        if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "^":
            return operation
        else:
            type_out("That’s not a valid operation. Whatever. Try again.")

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return round(num_1 * num_2, 2)

def divide(num_1, num_2):
    if num_2 == 0 and num_1 == 0:
        type_out("You can't divide zero by zero, genius")
        return None
    elif num_2 == 0:
        type_out("Great job, Einstein. You can't divide by zero. It's undefined.")
        return None
    else:
        return round(num_1 / num_2, 2)

def exponent(num_1, num_2):
    try:
        return round(num_1 ** num_2, 2)
    except Exception:
        type_out("Try to do a calculation that's actually possible next time. If you can get that through your thick skull")
        return None

if __name__ == "__main__":
    type_out("Ugh... welcome to the most boring calculator ever. Let's get this over with")
    while True:
        operation = get_operation("Alright, it's time to do some math, I guess\nLet's get this over with\nTell me which operation you so desperately want to do? Not like it matters to me (+, -, *, /, ^)")
        num_1 = get_number("Just tell me the first number already, I don't care enough to wait for you")
        num_2 = get_number("What’s the next number? Not that I really care")
        match operation:
            case "+":
                result = add(num_1, num_2)
                type_out(f"The answer is like {result}, I guess. Try not to get too excited.")
            case "-":
                result = subtract(num_1, num_2)
                type_out(f"The answer is {result}. Not that it really matters.")
            case "*":
                result = multiply(num_1, num_2)
                type_out(f"The answer is {result}. Not like it's important.")
            case "/":
                result = divide(num_1, num_2)
                type_out(f"The answer is {result}. Big deal")
            case "^":
                result = exponent(num_1, num_2)
                type_out(f"The answer is {result}. Not that I care.")
            case _:
                type_out("Ugh, I can't do that. Try again, I guess. This isn't rocket science. Just pick a real operation.")
                continue

        type_out("Do you want to do another calculation?")
        again = input().strip().lower()
        if again == "no":
            type_out("Finally, a break. Goodbye.")
            break
        elif again == "yes":
            type_out("Another calculation? Sigh. Fine.")
        else:
            type_out("I don't understand that. Let's just say no so I can get out of here\nBye")
            break