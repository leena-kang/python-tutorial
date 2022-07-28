from question1 import Question

prompt = [
    "What is my name? \n(a) Leena \n(b) Weena \n(c) Linguine \n(d) Thomas \n\n",
    "How do I like my coffee? \n(a) Black \n(b) Sweet and Creamy \n(c) Goldilocks \n(d) It really depends.\n\n",
    "What is my MBTI?\n(a) ISTJ \n(b) ESTJ \n(c) ENFP \n(d) INFP\n\n"
]

the_questions = [
    Question(prompt[0], "a"),
    Question(prompt[1], "d"),
    Question(prompt[2], "a")
]

def quiz(the_questions):
    score = 0
    for i in the_questions:
        user_answer = input(i.prompt)

        if user_answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(the_questions)) + " correct.")

quiz(the_questions)