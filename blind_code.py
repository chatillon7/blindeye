def who_came(a, b):
    if a == 0:
        if b == 0:
            return "None came"
        elif b == 1:
            return "B came alone"
        else:
            return "Invalid input"
    elif a == 1:
        if b == 0:
            return "A came alone"
        elif b == 1:
            return "A and B came together"
        else:
            return "Invalid input"
    else:
        return "Invalid input"

def blind_code(given_code, a, b):
    while True:
        input_code = input("Enter the blind code: ")
        if input_code == given_code:
            a = 1
            return a, b, who_came(a, b)
        else:
            print("Invalid input. Please try again.")

def generate_code():
    import random
    import string
    given_code = ''.join(random.choices(string.digits, k=6))
    return given_code

a = 0
b = 0
given_code = generate_code()
print("Generated blind code:", given_code)
a, b, result = blind_code(given_code, a, b)
print(result)