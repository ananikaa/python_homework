# Task 1
def hello():
    return "Hello!"

print (hello())

# Task 2
def greet(name):
   return f"Hello, {name}!"

#Task 3
def calc(a, b, operation="multiply"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        try:
            return a * b
        except TypeError:
            return "You can't multiply those values!"
    elif operation == "divide":
        if b == 0:
            return "You can't divide by 0!"
        return a / b
    elif operation == "modulo":
        if b == 0:
            return "You can't divide by 0!"
        return a % b
    elif operation == "int_divide":
        if b == 0:
            return "You can't divide by 0!"
        return a // b
    elif operation == "power":
        return a ** b

# Task 4
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type}."

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except Exception:
        return "Invalid data was provided."

#Task 6
def repeat(parrot, count):
    result = ""

    for i in range(count):
        result += parrot

    return result

#Task 7
def student_scores(mode, **kwargs):
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)

#Test 8
def titleize(text):
    words = text.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)

#Task 9
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

#task 10
def pig_latin(word):
    words = word.split()
    result = []
    vowels = "aeiou"

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0

            while index < len(word) and word[index] not in vowels:
                if word[index:index + 2] == "qu":
                    index += 2
                else:
                    index += 1

            new_word = word[index:] + word[:index] + "ay"
            result.append(new_word)

    return " ".join(result)