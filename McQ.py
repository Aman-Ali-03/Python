question = (
    "How many bone in human body are there?",
    "How many alphabet in english language?",
    "Which of the following is a common responsibility of a student? ",
    "What is the primary goal of a student in school or college? ",
    "Which activity best supports a student’s learning?  "
)
options = (
    ('A. 206',"B. 208","C. 230","D. 199"),
    ("A. 23","B. 26","C. 25","D. 27"),
    ("A. Attending classes regularly",
     "B. Managing a company",
     "C.  Paying employee salaries",
     "D.Conducting national elections "),
    ("A. To earn profit ",
     "B. To gain knowledge and skills ",
     "C. To supervise teachers. ",
     "D. To run a business"),
    ("A. Watching random TV shows",
     "B. Playing video games nonstop",
     "C. Sleeping all day",
     "D. Reading textbooks and reference materials")
)
answer = ("A","B","A","B","D")
question_num = 0
score = 0
for question in question:
    print("\n-------------------------")
    print(question)
    for option in options[question_num]:
        print(f"{option}")
    choice = input("Enter your option: ")
    if choice.upper() == answer[question_num]:
        score += 1
        print()
        print("Correct answer \n")
    else:
        print()
        print("Wrong answer \n")
    question_num += 1

print(f"Your score is {score}/{question_num}")
print(f"Your Percentage Score is {score/question_num*100}")