questions = (
    ("How many elements are in the preidic table?: "),
    ("Which animal layes the largest eggs?: "),
    ("What is the most abundant gas in Earth's atmosphere?: "),
    ("How many bones are in human body?: "),
    ("Which planet in solar system is the hottest?: "),
)
options = (
    ("A. 116 ", "B. 117 ", "C. 118 ", "D. 119 "),
    ("A. Whale ", "B. Crocodile ", "C. Elephant ", "D. Ostrich "),
    ("A. Nitrogen", "B. Oxgen", "C. Carbon-dioxide ", "D. Hydrogen"),
    ("A. 206 ", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
)

correct_answers = ("C", "D", "A", "A", "B")
# since we are changing it by appending values it needs to be a list
guesses = []
score = 0
question_num = 0


for question in questions:
    print("-----------------")
    print(question)

    for option in options[question_num]:
        print(option)

    userAnswer = input(
        "Select the correct answer by choosing the corrcet letter (A, B, C, D)? "
    ).upper()

    guesses.append(userAnswer)

    if userAnswer == correct_answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"{correct_answers[question_num]} is the correct answer")

    question_num += 1

print("----------------")
print("     Results    ")
print("----------------")

print("answers: ", end=" ")
for answer in correct_answers:
    print(answer, end=" ")

print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")

precentage = int(score / len(questions) * 100)
print(f"your total score out of 5 is {score} / 5 wich is {precentage}%")
