# main.py (Interactive Version)

import os
from src.models import Student, Course, Quiz, Progress
from src.factory import EntityFactory
from src.repository import JsonRepository

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

def run():
    student_repo = JsonRepository("Student")
    course_repo = JsonRepository("Course")
    quiz_repo = JsonRepository("Quiz")
    progress_repo = JsonRepository("Progress")

    while True:
        choice = menu()

        # --------------------------
        # 1. Add Student
        if choice == "1":
            clear()
            print("📌 Add New Student")
            sid = input("Student ID: ")
            name = input("Name: ")
            email = input("Email: ")

            new_student = EntityFactory.create_entity(
                'Student', id=sid, name=name, email=email
            )
            student_repo.create(new_student)
            print("✔️ Student Added!\n")

        # --------------------------
        # 2. Get Student
        elif choice == "2":
            clear()
            sid = input("Enter Student ID: ")
            data = student_repo.get_by_id(sid)
            if data:
                student = EntityFactory.create_entity(
                    'Student',
                    id=data['student_id'],
                    name=data['name'],
                    email=data['email']
                )
                print(student.display_details())
            else:
                print("❌ Student not found.")

        # --------------------------
        # 3. Add Course
        elif choice == "3":
            clear()
            print("📌 Add New Course")
            cid = input("Course ID: ")
            title = input("Course Title: ")
            instructor = input("Instructor: ")

            course = EntityFactory.create_entity(
                'Course', id=cid, title=title, instructor=instructor
            )
            course_repo.create(course)
            print("✔️ Course Added!\n")

        # --------------------------
        # 4. Get Course
        elif choice == "4":
            clear()
            cid = input("Enter Course ID: ")
            data = course_repo.get_by_id(cid)
            if data:
                course = EntityFactory.create_entity(
                    'Course',
                    id=data['course_id'],
                    title=data['title'],
                    instructor=data['instructor']
                )
                print(course.display_details())
            else:
                print("❌ Course not found.")

        # --------------------------
        # 5. Add Quiz
        elif choice == "5":
            clear()
            print("📌 Add Quiz")
            qid = input("Quiz ID: ")
            cid = input("Course ID: ")
            title = input("Quiz Title: ")
            max_score = input("Max Score: ")

            quiz = EntityFactory.create_entity(
                'Quiz',
                id=qid,
                course_id=cid,
                title=title,
                max_score=max_score
            )
            quiz_repo.create(quiz)
            print("✔️ Quiz Added!\n")

        # --------------------------
        # 6. Get Quiz
        elif choice == "6":
            clear()
            qid = input("Enter Quiz ID: ")
            data = quiz_repo.get_by_id(qid)
            if data:
                quiz = EntityFactory.create_entity(
                    'Quiz',
                    id=data['quiz_id'],
                    course_id=data['course_id'],
                    title=data['title'],
                    max_score=data['max_score']
                )
                print(quiz.display_details())
            else:
                print("❌ Quiz not found.")

        # --------------------------
        # 7. Add Progress
        elif choice == "7":
            clear()
            print("📌 Add Progress")
            pid = input("Progress ID: ")
            sid = input("Student ID: ")
            qid = input("Quiz ID: ")
            score = input("Score: ")

            prog = EntityFactory.create_entity(
                'Progress',
                id=pid,
                student_id=sid,
                quiz_id=qid,
                score=score
            )
            progress_repo.create(prog)
            print("✔️ Progress Added!\n")

        # --------------------------
        # 8. Get Progress
        elif choice == "8":
            clear()
            pid = input("Enter Progress ID: ")
            data = progress_repo.get_by_id(pid)
            if data:
                prog = EntityFactory.create_entity(
                    'Progress',
                    id=data['progress_id'],
                    student_id=data['student_id'],
                    quiz_id=data['quiz_id'],
                    score=data['score']
                )
                print(prog.display_details())
            else:
                print("❌ Progress not found.")

        # --------------------------
        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid option!")

if __name__ == '__main__':
    run()
