import os
import uuid
import re
from src.models import Student, Course, Quiz, Progress
from src.factory import EntityFactory
from src.repository import JsonRepository

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ------------ Input Validation ------------------

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("❌ Input cannot be empty. Try again!")
        else:
            return value

def input_optional_id(prompt):
    value = input(prompt).strip()
    return value if value != "" else str(uuid.uuid4())

def input_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("❌ Enter a valid number!")

def input_alpha_spaces(prompt):
    pattern = re.compile(r'^[A-Za-z\s]+$')
    while True:
        value = input(prompt).strip()
        if value == "":
            print("❌ Input cannot be empty. Try again!")
        elif not pattern.match(value):
            print("❌ Only letters and spaces allowed!")
        else:
            return value

# ---------------- MENU --------------------------

def menu():
    print("\n======== E-LEARNING PLATFORM MENU ========")
    print("1. Add Student")
    print("2. Get Student by ID")
    print("3. Add Course")
    print("4. Get Course by ID")
    print("5. Add Quiz")
    print("6. Get Quiz by ID")
    print("7. Add Progress")
    print("8. Get Progress by ID")
    print("9. Exit")
    print("==========================================")
    return input("Choose an option: ")

# ---------------- RUN ---------------------------

def run():
    student_repo = JsonRepository("Student")
    course_repo = JsonRepository("Course")
    quiz_repo = JsonRepository("Quiz")
    progress_repo = JsonRepository("Progress")

    while True:
        choice = menu()

        if choice == "1":  # Add Student
            clear()
            print("📌 Add New Student")
            sid = input_optional_id("Student ID (press Enter to auto-generate): ")
            if student_repo.get_by_id(sid):
                print("❌ Student with this ID already exists!")
                continue
            name = input_alpha_spaces("Name (letters and spaces only): ")
            email = input_non_empty("Email: ")
            try:
                student = EntityFactory.create_entity('Student', id=sid, name=name, email=email)
                student_repo.create(student)
                print(f"✔️ Student Added! ID = {sid}")
            except ValueError as ve:
                print(ve)

        elif choice == "2":  # Get Student
            clear()
            sid = input_non_empty("Enter Student ID: ")
            data = student_repo.get_by_id(sid)
            if not data:
                print("❌ Student not found.")
                continue
            student = EntityFactory.create_entity('Student', id=data['student_id'], name=data['name'], email=data['email'])
            print(student.display_details())

        elif choice == "3":  # Add Course
            clear()
            print("📌 Add New Course")
            cid = input_optional_id("Course ID (press Enter to auto-generate): ")
            if course_repo.get_by_id(cid):
                print("❌ Course with this ID already exists!")
                continue
            title = input_non_empty("Course Title: ")
            instructor = input_alpha_spaces("Instructor (letters and spaces only): ")
            try:
                course = EntityFactory.create_entity('Course', id=cid, title=title, instructor=instructor)
                course_repo.create(course)
                print(f"✔️ Course Added! ID = {cid}")
            except ValueError as ve:
                print(ve)

        elif choice == "4":  # Get Course
            clear()
            cid = input_non_empty("Enter Course ID: ")
            data = course_repo.get_by_id(cid)
            if not data:
                print("❌ Course not found.")
                continue
            course = EntityFactory.create_entity('Course', id=data['course_id'], title=data['title'], instructor=data['instructor'])
            print(course.display_details())

        elif choice == "5":  # Add Quiz
            clear()
            print("📌 Add Quiz")
            qid = input_optional_id("Quiz ID (press Enter to auto-generate): ")
            if quiz_repo.get_by_id(qid):
                print("❌ Quiz with this ID already exists!")
                continue
            cid = input_non_empty("Course ID: ")
            if not course_repo.get_by_id(cid):
                print("❌ Course does not exist!")
                continue
            title = input_non_empty("Quiz Title: ")
            max_score = input_number("Max Score (number): ")
            quiz = EntityFactory.create_entity('Quiz', id=qid, course_id=cid, title=title, max_score=max_score)
            quiz_repo.create(quiz)
            print(f"✔️ Quiz Added! ID = {qid}")

        elif choice == "6":  # Get Quiz
            clear()
            qid = input_non_empty("Enter Quiz ID: ")
            data = quiz_repo.get_by_id(qid)
            if not data:
                print("❌ Quiz not found.")
                continue
            quiz = EntityFactory.create_entity('Quiz', id=data['quiz_id'], course_id=data['course_id'], title=data['title'], max_score=data['max_score'])
            print(quiz.display_details())

        elif choice == "7":  # Add Progress
            clear()
            print("📌 Add Progress")
            pid = input_optional_id("Progress ID (press Enter to auto-generate): ")
            if progress_repo.get_by_id(pid):
                print("❌ Progress with this ID already exists!")
                continue
            sid = input_non_empty("Student ID: ")
            if not student_repo.get_by_id(sid):
                print("❌ Student does not exist!")
                continue
            qid = input_non_empty("Quiz ID: ")
            if not quiz_repo.get_by_id(qid):
                print("❌ Quiz does not exist!")
                continue
            score = input_number("Score (number): ")
            prog = EntityFactory.create_entity('Progress', id=pid, student_id=sid, quiz_id=qid, score=score)
            progress_repo.create(prog)
            print(f"✔️ Progress Added! ID = {pid}")

        elif choice == "8":  # Get Progress
            clear()
            pid = input_non_empty("Enter Progress ID: ")
            data = progress_repo.get_by_id(pid)
            if not data:
                print("❌ Progress not found.")
                continue
            prog = EntityFactory.create_entity('Progress', id=data['progress_id'], student_id=data['student_id'], quiz_id=data['quiz_id'], score=data['score'])
            print(prog.display_details())

        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("⚠️ Invalid option! Try again.")

if __name__ == '__main__':
    run()
