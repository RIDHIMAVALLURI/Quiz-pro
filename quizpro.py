import re
import time
import random

RECORD_FILE = "quiz_records.txt"
TOTAL_QUESTIONS = 10


def q(question, correct, wrong1, wrong2, wrong3):
    """Builds one question dictionary. The correct answer is listed first and
    the options are shuffled later when the question is displayed."""
    return {"question": question, "options": [correct, wrong1, wrong2, wrong3]}


# ---------------------------------------------------------------
# Question bank: dictionary -> subject -> difficulty -> list of dictionaries
# ---------------------------------------------------------------
questions = {
    "Maths": {
        "Easy": [
            q("What is 5 + 7?", "12", "10", "13", "14"),
            q("What is 6 x 6?", "36", "30", "42", "48"),
            q("What is 20 / 4?", "5", "4", "6", "8"),
            q("What is 15 - 8?", "7", "5", "6", "8"),
            q("What is 9 + 9?", "18", "16", "17", "19"),
            q("What is 8 x 7?", "56", "54", "58", "64"),
            q("What is 100 - 45?", "55", "45", "65", "75"),
            q("What is 3 x 9?", "27", "24", "26", "30"),
            q("What is 81 / 9?", "9", "7", "8", "10"),
            q("What is 14 + 27?", "41", "39", "43", "45"),
        ],
        "Medium": [
            q("What is 12 x 12?", "144", "124", "154", "164"),
            q("What is 25% of 200?", "50", "25", "40", "75"),
            q("What is the HCF of 12 and 18?", "6", "2", "3", "9"),
            q("What is 2^3 + 3^2?", "17", "15", "18", "20"),
            q("What is the average of 10, 20 and 30?", "20", "15", "25", "30"),
            q("What is the LCM of 4 and 6?", "12", "10", "18", "24"),
            q("What is 15% of 300?", "45", "30", "35", "40"),
            q("Solve for x: 3x + 5 = 20", "5", "3", "4", "6"),
            q("What is the area of a rectangle with sides 8 and 5?", "40", "26", "13", "45"),
            q("What is the next prime number after 7?", "11", "9", "13", "15"),
        ],
        "Hard": [
            q("What is the derivative of x^2?", "2x", "x", "x^2", "2"),
            q("What is 2^5?", "32", "16", "24", "64"),
            q("What is the square root of 144?", "12", "10", "11", "14"),
            q("What is 15 x 8?", "120", "100", "110", "130"),
            q("What is the integral of 2x dx?", "x^2 + C", "2 + C", "x + C", "2x^2 + C"),
            q("What is the value of sin 90 degrees?", "1", "0", "1/2", "-1"),
            q("What is log10(1000)?", "3", "2", "4", "10"),
            q("What are the roots of x^2 - 5x + 6 = 0?", "2 and 3", "1 and 6", "-2 and -3", "1 and 5"),
            q("What is the value of 5! (5 factorial)?", "120", "60", "100", "150"),
            q("What is the derivative of sin x?", "cos x", "-cos x", "-sin x", "tan x"),
        ],
    },
    "Physics": {
        "Easy": [
            q("What is the SI unit of force?", "Newton", "Joule", "Watt", "Pascal"),
            q("What is the SI unit of energy?", "Joule", "Newton", "Watt", "Volt"),
            q("Which force pulls objects towards Earth?", "Gravity", "Friction", "Tension", "Magnetic force"),
            q("Which instrument is used to measure temperature?", "Thermometer", "Ammeter", "Barometer", "Voltmeter"),
            q("What is the SI unit of power?", "Watt", "Joule", "Newton", "Pascal"),
            q("What is the approximate speed of light?", "3 x 10^8 m/s", "3 x 10^6 m/s", "300 m/s", "3 x 10^5 m/s"),
            q("Which of these is a source of light?", "Sun", "Moon", "Mirror", "Planet"),
            q("What is the SI unit of frequency?", "Hertz", "Metre", "Second", "Kelvin"),
            q("Sound cannot travel through which of these?", "Vacuum", "Water", "Steel", "Air"),
            q("Which instrument measures electric current?", "Ammeter", "Voltmeter", "Barometer", "Thermometer"),
        ],
        "Medium": [
            q("What is Newton's second law?", "F = ma", "E = mc^2", "V = IR", "P = VI"),
            q("What is the unit of resistance?", "Ohm", "Volt", "Ampere", "Watt"),
            q("What is the formula for kinetic energy?", "1/2 mv^2", "mgh", "ma", "Fd"),
            q("What is the SI unit of electric current?", "Ampere", "Volt", "Ohm", "Watt"),
            q("Which device converts electrical energy into mechanical energy?", "Motor", "Battery", "Generator", "Transformer"),
            q("Which formula represents Ohm's law?", "V = IR", "P = VI", "F = ma", "E = mc^2"),
            q("What is the acceleration due to gravity on Earth?", "9.8 m/s^2", "1.6 m/s^2", "8.9 m/s^2", "10.8 m/s^2"),
            q("Which lens is used to correct short-sightedness?", "Concave", "Convex", "Plane", "Cylindrical"),
            q("What is the formula for momentum?", "mv", "m/v", "m + v", "m - v"),
            q("What is the SI unit of pressure?", "Pascal", "Newton", "Joule", "Watt"),
        ],
        "Hard": [
            q("What is Einstein's mass-energy relation?", "E = mc^2", "E = mc", "E = m^2c", "E = 2mc"),
            q("What is the approximate escape velocity from Earth?", "11.2 km/s", "7.9 km/s", "3 km/s", "25 km/s"),
            q("The Heisenberg uncertainty principle relates which two quantities?", "Position and momentum", "Mass and energy", "Charge and current", "Speed and time"),
            q("Lenz's law is based on the conservation of which quantity?", "Energy", "Mass", "Charge", "Momentum"),
            q("Which particle carries the electromagnetic force?", "Photon", "Gluon", "Graviton", "W boson"),
            q("What is the time period of a simple pendulum?", "2 pi sqrt(l/g)", "2 pi sqrt(g/l)", "2 pi l g", "pi sqrt(l/g)"),
            q("What is the work done by the centripetal force in uniform circular motion?", "Zero", "Maximum", "Positive", "Negative"),
            q("What is the power of a lens with focal length 0.5 m?", "2 D", "0.5 D", "1 D", "5 D"),
            q("Which phenomenon proves the wave nature of light?", "Interference", "Photoelectric effect", "Compton effect", "Emission of X-rays"),
            q("What is the SI unit of magnetic flux?", "Weber", "Tesla", "Henry", "Farad"),
        ],
    },
    "Python": {
        "Easy": [
            q("Which keyword is used to define a function?", "def", "function", "define", "fun"),
            q("Which symbol is used for comments in Python?", "#", "//", "/*", "--"),
            q("Which data type stores True or False?", "bool", "int", "str", "float"),
            q("Which function is used to display output?", "print()", "display()", "output()", "show()"),
            q("Which brackets are used for a list?", "[]", "()", "{}", "<>"),
            q("Which data type is used to store text?", "str", "int", "float", "bool"),
            q("What is the output of print(5 // 2)?", "2", "2.5", "3", "2.0"),
            q("Which operator is used for exponent (power)?", "**", "^", "//", "%"),
            q("Which function is used to take input from the user?", "input()", "read()", "scan()", "get()"),
            q("What is the file extension of a Python file?", ".py", ".pt", ".pyt", ".python"),
        ],
        "Medium": [
            q("Which data structure stores key-value pairs?", "Dictionary", "List", "Tuple", "Set"),
            q("What does len() return?", "Length", "Data type", "Index", "Memory"),
            q("Which keyword is used for exception handling?", "try", "check", "error", "catch"),
            q("Which loop is used to iterate over a sequence?", "for", "repeat", "loop", "iterate"),
            q("Which method adds an item to the end of a list?", "append()", "add()", "insertEnd()", "push()"),
            q("Which of these creates a tuple?", "(1, 2)", "[1, 2]", "{1, 2}", "<1, 2>"),
            q("What is the output of 'Hello'[1]?", "e", "H", "l", "o"),
            q("Which keyword is used to exit a loop?", "break", "stop", "exit", "end"),
            q("Which method converts a string to uppercase?", "upper()", "up()", "capitalize()", "caps()"),
            q("Which file mode is used for appending data?", "'a'", "'r'", "'w'", "'x'"),
        ],
        "Hard": [
            q("What is a lambda function?", "Anonymous function", "Loop", "Class", "Module"),
            q("Which concept allows one class to acquire properties of another?", "Inheritance", "Encapsulation", "Iteration", "Looping"),
            q("What is the purpose of _init_()?", "Initialize an object", "Delete an object", "Print an object", "Copy an object"),
            q("What is the output of [x * 2 for x in range(3)]?", "[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "[1, 2, 3]"),
            q("Which of these is immutable?", "tuple", "list", "dict", "set"),
            q("What does 'self' represent in a class method?", "The current object", "The class", "A module", "A function"),
            q("Which keyword is used to create a generator function?", "yield", "return", "generate", "next"),
            q("What is the average time complexity of a dictionary lookup?", "O(1)", "O(n)", "O(log n)", "O(n^2)"),
            q("What does the 'with' statement ensure when handling files?", "File is closed automatically", "File is encrypted", "File is read only", "File is deleted"),
            q("What is the output of bool([])?", "False", "True", "None", "Error"),
        ],
    },
}


# ---------------------------------------------------------------
# Login with regular expressions
# ---------------------------------------------------------------
def get_name():
    while True:
        name = input("Enter your name: ").strip()
        if re.fullmatch(r"[A-Za-z][A-Za-z .]{1,48}", name):
            return name
        print("Invalid name. Use only letters and spaces (at least 2 characters).\n")


def get_reg_no():
    while True:
        reg_no = input("Enter your registration number: ").strip().upper()
        if reg_no != "" and "|" not in reg_no:
            return reg_no
        print("Registration number cannot be empty.\n")


def get_email():
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    while True:
        email = input("Enter your email ID: ").strip().lower()
        if re.fullmatch(pattern, email):
            return email
        print("Invalid email ID. Please enter a valid email.\n")


def login():
    print("\n====================================")
    print("              QUIZPRO")
    print("       Python Quiz Application")
    print("====================================\n")
    name = get_name()
    reg_no = get_reg_no()
    email = get_email()
    print("\nLogin successful! Welcome,", name)
    return {"name": name, "reg_no": reg_no, "email": email}


# ---------------------------------------------------------------
# Menus
# ---------------------------------------------------------------
def select_subject():
    subjects = ["Maths", "Physics", "Python"]
    while True:
        print("\n========== SELECT SUBJECT ==========")
        for i in range(len(subjects)):
            print(i + 1, ".", subjects[i])
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return "Maths"
        elif choice == "2":
            return "Physics"
        elif choice == "3":
            return "Python"
        else:
            print("Please select a valid subject.")


def select_difficulty():
    difficulties = ["Easy", "Medium", "Hard"]
    while True:
        print("\n========== SELECT DIFFICULTY ==========")
        for i in range(len(difficulties)):
            print(i + 1, ".", difficulties[i])
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        else:
            print("Please select a valid difficulty.")


# ---------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------
def start_quiz(user):
    subject = select_subject()
    difficulty = select_difficulty()
    question_list = questions[subject][difficulty][:]
    random.shuffle(question_list)
    score = 0

    print("\n====================================")
    print("            QUIZ STARTED")
    print("====================================")
    print("Student Name   :", user["name"])
    print("Reg. Number    :", user["reg_no"])
    print("Student Email  :", user["email"])
    print("Subject        :", subject)
    print("Difficulty     :", difficulty)
    print("Total Questions:", TOTAL_QUESTIONS)
    print("====================================")

    start_time = time.time()

    for number in range(TOTAL_QUESTIONS):
        q_item = question_list[number]
        options = q_item["options"][:]
        correct_text = options[0]
        random.shuffle(options)
        letters = ["A", "B", "C", "D"]
        correct_letter = letters[options.index(correct_text)]

        print("\nQuestion", number + 1, "of", TOTAL_QUESTIONS)
        print(q_item["question"])
        for i in range(4):
            print(letters[i] + ".", options[i])

        while True:
            answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()
            if answer in letters:
                break
            print("Invalid input. Please enter A, B, C or D.")

        if answer == correct_letter:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is " + correct_letter + ".")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    percentage = round((score / TOTAL_QUESTIONS) * 100, 1)

    return subject, difficulty, score, percentage, time_taken


# ---------------------------------------------------------------
# Result and file handling
# ---------------------------------------------------------------
def display_result(user, subject, difficulty, score, percentage, time_taken):
    print("\n====================================")
    print("            QUIZ RESULT")
    print("====================================")
    print("Student Name  :", user["name"])
    print("Reg. Number   :", user["reg_no"])
    print("Student Email :", user["email"])
    print("Subject       :", subject)
    print("Difficulty    :", difficulty)
    print("Score         : " + str(score) + "/" + str(TOTAL_QUESTIONS))
    print("Percentage    : " + str(percentage) + "%")
    print("Time Taken    : " + str(time_taken) + " seconds")
    print("====================================")


def save_record(user, subject, difficulty, score, percentage, time_taken):
    record = [user["email"], user["name"], user["reg_no"], subject, difficulty,
              str(score), str(percentage), str(time_taken)]
    try:
        with open(RECORD_FILE, "a") as file:
            file.write("|".join(record) + "\n")
        print("\nQuiz record saved successfully!")
    except OSError:
        print("\nSorry, the record could not be saved.")


def view_previous_scores(user):
    found = False
    try:
        with open(RECORD_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    print("\n====================================")
    print("          PREVIOUS SCORES")
    print("====================================")
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 8 and parts[0] == user["email"]:
            found = True
            print("\nSubject    :", parts[3])
            print("Difficulty :", parts[4])
            print("Score      : " + parts[5] + "/" + str(TOTAL_QUESTIONS))
            print("Percentage : " + parts[6] + "%")
            print("Time Taken : " + parts[7] + " seconds")
            print("------------------------------------")
    if not found:
        print("\nNo previous records found for", user["email"])


# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------
def main():
    user = login()
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Start Quiz")
        print("2. View Previous Scores")
        print("3. Exit")
        print("===============================")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            subject, difficulty, score, percentage, time_taken = start_quiz(user)
            display_result(user, subject, difficulty, score, percentage, time_taken)
            save_record(user, subject, difficulty, score, percentage, time_taken)
        elif choice == "2":
            view_previous_scores(user)
        elif choice == "3":
            print("\nThank you for using QuizPro!")
            break
        else:
            print("Please select 1, 2 or 3.")


main()
