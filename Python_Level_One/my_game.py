import random

def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def get_guess():
    return list(input("What is your guess? "))

def generate_clues(code,user_guess):
    if user_guess==code:
        return "CODE CRACKED"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["nope"]
    else:
        return clues


print("welcome code breaker")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":

    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
