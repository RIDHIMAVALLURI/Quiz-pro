
import time
import json
import os

# Store quiz questions
questions = {
    "Maths": {
        "Easy": [
            {
                "question": "What is 5 + 7?",
                "options": ["A. 10", "B. 12", "C. 13", "D. 14"],
                "answer": "B"
            },
            {
                "question": "What is 6 x 6?",
                "options": ["A. 30", "B. 36", "C. 42", "D. 48"],
                "answer": "B"
            },
            {
                "question": "What is 20 / 4?",
                "options": ["A. 4", "B. 5", "C. 6", "D. 8"],
                "answer": "B"
            },
            {
                "question": "What is 15 - 8?",
                "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
                "answer": "C"
            },
            {
                "question": "What is 9 + 9?",
                "options": ["A. 16", "B. 17", "C. 18", "D. 19"],
                "answer": "C"
            }
        ],

        "Medium": [
            {
                "question": "What is 12 x 12?",
                "options": ["A. 124", "B. 144", "C. 154", "D. 164"],
                "answer": "B"
            },
            {
                "question": "What is 25% of 200?",
                "options": ["A. 25", "B. 40", "C. 50", "D. 75"],
                "answer": "C"
            },
            {
                "question": "What is the HCF of 12 and 18?",
                "options": ["A. 2", "B. 3", "C. 6", "D. 9"],
                "answer": "C"
            },
            {
                "question": "What is 2^3 + 3^2?",
                "options": ["A. 15", "B. 17", "C. 18", "D. 20"],
                "answer": "B"
            },
            {
                "question": "What is the average of 10, 20 and 30?",
                "options": ["A. 15", "B. 20", "C. 25", "D. 30"],
                "answer": "B"
            }
        ],

        "Hard": [
            {
                "question": "What is the derivative of x^2?",
                "options": ["A. x", "B. 2x", "C. x^2", "D. 2"],
                "answer": "B"
            },
            {
                "question": "What is 2^5?",
                "options": ["A. 16", "B. 24", "C. 32", "D. 64"],
                "answer": "C"
            },
            {
                "question": "What is the square root of 144?",
                "options": ["A. 10", "B. 11", "C. 12", "D. 14"],
                "answer": "C"
            },
            {
                "question": "What is 15 x 8?",
                "options": ["A. 100", "B. 110", "C. 120", "D. 130"],
                "answer": "C"
            },
            {
                "question": "What is 100 divided by 4?",
                "options": ["A. 20", "B. 25", "C. 30", "D. 40"],
                "answer": "B"
            }
        ]
    },

    "Physics": {
        "Easy": [
            {
                "question": "What is the SI unit of force?",
                "options": ["A. Joule", "B. Newton", "C. Watt", "D. Pascal"],
                "answer": "B"
            },
            {
                "question": "What is the SI unit of energy?",
                "options": ["A. Joule", "B. Newton", "C. Watt", "D. Volt"],
                "answer": "A"
            },
            {
                "question": "Which force pulls objects towards Earth?",
                "options": ["A. Friction", "B. Gravity", "C. Tension", "D. Magnetic force"],
                "answer": "B"
            },
            {
                "question": "Which instrument is used to measure temperature?",
                "options": ["A. Ammeter", "B. Barometer", "C. Thermometer", "D. Voltmeter"],
                "answer": "C"
            },
            {
                "question": "What is the SI unit of power?",
                "options": ["A. Joule", "B. Watt", "C. Newton", "D. Pascal"],
                "answer": "B"
            }
        ],

        "Medium": [
            {
                "question": "What is Newton's second law?",
                "options": ["A. F = ma", "B. E = mc^2", "C. V = IR", "D. P = VI"],
                "answer": "A"
            },
            {
                "question": "What is the unit of resistance?",
                "options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
                "answer": "C"
            },
            {
                "question": "What is the formula for kinetic energy?",
                "options": ["A. mgh", "B. 1/2 mv^2", "C. ma", "D. Fd"],
                "answer": "B"
            },
            {
                "question": "What is the SI unit of electric current?",
                "options": ["A. Ampere", "B. Volt", "C. Ohm", "D. Watt"],
                "answer": "A"
            },
            {
                "question": "Which device converts electrical energy into mechanical energy?",
                "options": ["A. Motor", "B. Battery", "C. Generator", "D. Transformer"],
                "answer": "A"
            }
        ],

        "Hard": [
            {
                "question": "What is the SI unit of electric charge?",
                "options": ["A. Coulomb", "B. Ampere", "C. Ohm", "D. Tesla"],
                "answer": "A"
            },
            {
                "question": "What is the formula for Ohm's law?",
                "options": ["A. V = IR", "B. F = ma", "C. P = VI", "D. E = mc^2"],
                "answer": "A"
            },
            {
                "question": "What is the approximate acceleration due to gravity on Earth?",
                "options": ["A. 4.9 m/s^2", "B. 9.8 m/s^2", "C. 15 m/s^2", "D. 20 m/s^2"],
                "answer": "B"
            },
            {
                "question": "Which quantity is measured in hertz?",
                "options": ["A. Force", "B. Energy", "C. Frequency", "D. Power"],
                "answer": "C"
            },
            {
                "question": "What is the SI unit of magnetic flux?",
                "options": ["A. Tesla", "B. Weber", "C. Henry", "D. Volt"],
                "answer": "B"
            }
        ]
    },

    "Python": {
        "Easy": [
            {
                "question": "Which keyword is used to define a function?",
                "options": ["A. function", "B. define", "C. def", "D. fun"],
                "answer": "C"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["A. //", "B. #", "C. /*", "D. --"],
                "answer": "B"
            },
            {
                "question": "Which data type stores True or False?",
                "options": ["A. int", "B. str", "C. bool", "D. float"],
                "answer": "C"
            },
            {
                "question": "Which function is used to display output?",
                "options": ["A. display()", "B. output()", "C. print()", "D. show()"],
                "answer": "C"
            },
            {
                "question": "Which brackets are used for a list?",
                "options": ["A. ()", "B. {}", "C. []", "D. <>"],
                "answer": "C"
            }
        ],

        "Medium": [
            {
                "question": "Which data structure stores key-value pairs?",
                "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
                "answer": "C"
            },
            {
                "question": "What does len() return?",
                "options": ["A. Data type", "B. Length", "C. Index", "D. Memory"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used for exception handling?",
                "options": ["A. try", "B. check", "C. error", "D. catch"],
                "answer": "A"
            },
            {
                "question": "Which loop is used to iterate over a sequence?",
                "options": ["A. repeat", "B. for", "C. loop", "D. iterate"],
                "answer": "B"
            },
            {
                "question": "Which method adds an item to the end of a list?",
                "options": ["A. add()", "B. insertEnd()", "C. append()", "D. push()"],
                "answer": "C"
            }
        ],

        "Hard": [
            {
                "question": "What is a lambda function?",
                "options": ["A. Anonymous function", "B. Loop", "C. Class", "D. Module"],
                "answer": "A"
            },
            {
                "question": "Which concept allows one class to acquire properties of another?",
                "options": ["A. Encapsulation", "B. Inheritance", "C. Iteration", "D. Looping"],
                "answer": "B"
            },
            {
                "question": "What is the purpose of __init__()?",
                "options": ["A. Delete an object", "B. Initialize an object", "C. Print an object", "D. Import a module"],
                "answer": "B"
            },
            {
                "question": "Which keyword is used to create a class?",
                "options": ["A. object", "B. define", "C. class", "D. create"],
                "answer": "C"
            },
            {
                "question": "Which keyword is used to return a value from a function?",
                "options": ["A. print", "B. return", "C. yield", "D. break"],
                "answer": "B"
            }
        ]
    }
}


# File used to store student records
RECORD_FILE = "quiz_records.json"


# Load previous records
def load_records():
    if os.path.exists(RECORD_FILE):
        try:
            with open(RECORD_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    return {}


# Save student records
def save_records(records):
    with open(RECORD_FILE, "w") as file:
        json.dump(records, file, indent=4)


# Student login
def login():
    while True:
        email = input("Enter your email ID: ").strip()

        if "@" in email and "." in email.split("@")[-1]:
            print("Login successful!")
            return email

        print("Invalid email ID. Please enter a valid email.")


# Select subject
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


# Select difficulty
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


# Start the quiz
def start_quiz(email):
    subject = select_subject()
    difficulty = select_difficulty()

    question_list = questions[subject][difficulty]
    score = 0

    print("\n====================================")
    print("            QUIZ STARTED")
    print("====================================")
    print("Student Email :", email)
    print("Subject       :", subject)
    print("Difficulty    :", difficulty)
    print("Total Questions:", len(question_list))
    print("====================================")

    start_time = time.time()

    for number, q in enumerate(question_list, start=1):
        print("\nQuestion", number, "of", len(question_list))
        print(q["question"])

        for option in q["options"]:
            print(option)

        while True:
            answer = input(
                "\nEnter your answer (A/B/C/D): "
            ).strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Incorrect answer!")
            print("Correct answer:", q["answer"])

    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    total_questions = len(question_list)
    percentage = (score / total_questions) * 100

    print("\n====================================")
    print("             QUIZ RESULT")
    print("====================================")
    print("Student Email :", email)
    print("Subject       :", subject)
    print("Difficulty    :", difficulty)
    print("Score         :", score, "/", total_questions)
    print("Percentage    :", round(percentage, 2), "%")
    print("Time Taken    :", time_taken, "seconds")
    print("====================================")

    # Save the result in the student's record
    records = load_records()

    if email not in records:
        records[email] = []

    result = {
        "subject": subject,
        "difficulty": difficulty,
        "score": score,
        "total_questions": total_questions,
        "percentage": round(percentage, 2),
        "time_taken": time_taken
    }

    records[email].append(result)
    save_records(records)

    print("Your quiz result has been saved!")


# View previous quiz records
def view_history(email):
    records = load_records()

    print("\n========== QUIZ HISTORY ==========")

    if email not in records or not records[email]:
        print("No previous quiz records found.")
        return

    for i, result in enumerate(records[email], start=1):
        print("\nAttempt:", i)
        print("Subject    :", result["subject"])
        print("Difficulty :", result["difficulty"])
        print(
            "Score      :",
            result["score"],
            "/",
            result["total_questions"]
        )
        print("Percentage :", result["percentage"], "%")
        print("Time Taken :", result["time_taken"], "seconds")


# Main program
def main():
    print("====================================")
    print("          WELCOME TO QUIZPRO")
    print("====================================")

    email = login()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Start Quiz")
        print("2. View Quiz History")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            start_quiz(email)

        elif choice == "2":
            view_history(email)

        elif choice == "3":
            print("Thank you for using QuizPro!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Run the application
if __name__ == "__main__":
    main()
