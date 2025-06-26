
#quiz app
import random
print("Welcome to the quiz app")
score = 0
attempt = 3
questions = {
    "Who is the richest person in the world?" :"Elon musk",
    "In which continent Nepal is in?" : "Asia",
    "Which vitamin does sunlight give?": "Vitamin D",
    "Where do Gautam Buddha born?": "Nepal",
    "Which is the nearest planet to Sun?": "Mercury"
}
askedQsn = []
while attempt > 0 and len(askedQsn) < len(questions):
    question = random.choice(list(questions.keys()))
    if question in askedQsn:
        continue
    askedQsn.append(question)
    print("Question :", question)

    correctAns = questions[question]
    userInput = input("Enter your answer: ")
    if userInput.lower() == correctAns.lower():
        print("Thats a correct answer!")
        score += 1
    elif userInput.lower() == "exit":
        print("Thanks for playing our game!")
        break
    else:
        print("Sorry! the correct answer is", correctAns)
        attempt -=1
        print(f"You have {attempt} attempts left")

print("The quiz is over ")
print(f"The total score is {score} out of {len(questions)}")
