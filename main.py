from src.repository import JsonRepository
from src.services import StudentService, CourseService, QuizService, ProgressService
# Ensure input_email is imported from utils
from src.utils import input_non_empty, input_optional_id, input_number, input_alpha_spaces, input_email 
from src.logging_config import logger

def run():
    logger.info("Application started")

    # --- Initialize Repositories ---
    student_repo = JsonRepository("Student")
    course_repo = JsonRepository("Course")
    quiz_repo = JsonRepository("Quiz")
    progress_repo = JsonRepository("Progress")

    # --- Initialize Services ---
    student_service = StudentService(student_repo)
    course_service = CourseService(course_repo)
    quiz_service = QuizService(quiz_repo)
    progress_service = ProgressService(student_repo, quiz_repo, progress_repo)

    valid_choices = {str(i) for i in range(1, 22)}

    while True:
        print("\n=== E-LEARNING MENU ===")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Quiz")
        print("4. Add Progress")
        print("-----------------------")
        print("5. View Student")
        print("6. View Course")
        print("7. View Quiz")
        print("8. View Progress")
        print("-----------------------")
        print("9. Update Student")
        print("10. Update Course")
        print("11. Update Quiz")
        print("12. Update Progress")
        print("-----------------------")
        print("13. Delete Student")
        print("14. Delete Course")
        print("15. Delete Quiz")
        print("16. Delete Progress")
        print("-----------------------")
        print("17. List All Students")
        print("18. List All Courses")
        print("19. List All Quizzes")
        print("20. List All Progress")
        print("21. Exit")
        print("-----------------------")

        choice = input("Select option: ").strip()

        # ------- CREATE -------
        try:
            if choice == "1":
                sid = input_optional_id("Student ID (Enter for auto): ")
                name = input_alpha_spaces("Name: ")
                email = input_email("Email: ") # <-- CHANGED TO input_email
                student_service.create_student(sid, name, email)

            elif choice == "2":
                cid = input_optional_id("Course ID: ")
                title = input_alpha_spaces("Title: ")
                instr = input_alpha_spaces("Instructor: ")
                course_service.create_course(cid, title, instr)

            elif choice == "3":
                qid = input_optional_id("Quiz ID: ")
                cid = input_non_empty("Course ID: ")
                title = input_non_empty("Quiz Title: ")
                max_s = input_number("Max Score: ")
                quiz_service.create_quiz(qid, cid, title, max_s)

            elif choice == "4":
                pid = input_optional_id("Progress ID: ")
                sid = input_non_empty("Student ID: ")
                qid = input_non_empty("Quiz ID: ")
                score = input_number("Score: ")
                progress_service.create_progress(pid, sid, qid, score)

        except ValueError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

        # ------- READ / VIEW BY ID -------
        try:
            if choice == "5":
                sid = input_non_empty("Student ID: ")
                print(student_repo.get_by_id(sid) or "Not found.")

            elif choice == "6":
                cid = input_non_empty("Course ID: ")
                print(course_repo.get_by_id(cid) or "Not found.")

            elif choice == "7":
                qid = input_non_empty("Quiz ID: ")
                print(quiz_repo.get_by_id(qid) or "Not found.")

            elif choice == "8":
                pid = input_non_empty("Progress ID: ")
                print(progress_repo.get_by_id(pid) or "Not found.")
        except ValueError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")  

        # ------- UPDATE -------
        try:
            if choice == "9":
                sid = input_non_empty("Student ID to update: ")
                name = input_alpha_spaces("New Name: ")
                email = input_email("New Email: ") # <-- CHANGED TO input_email
                student_service.update_student(sid, name, email)

            elif choice == "10":
                cid = input_non_empty("Course ID to update: ")
                title = input_alpha_spaces("New Title: ")
                instr = input_alpha_spaces("New Instructor: ")
                course_service.update_course(cid, title, instr)

            elif choice == "11":
                qid = input_non_empty("Quiz ID to update: ")
                title = input_non_empty("New Title: ")
                max_s = input_number("New Max Score: ")
                quiz_service.update_quiz(qid, title, max_s)

            elif choice == "12":
                pid = input_non_empty("Progress ID to update: ")
                score = input_number("New Score: ")
                progress_service.update_progress(pid, score)

        except ValueError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

        # ------- DELETE -------
        try:
            if choice == "13":
                sid = input_non_empty("Student ID: ")
                student_service.delete_student(sid)

            elif choice == "14":
                cid = input_non_empty("Course ID: ")
                course_service.delete_course(cid)

            elif choice == "15":
                qid = input_non_empty("Quiz ID: ")
                quiz_service.delete_quiz(qid)

            elif choice == "16":
                pid = input_non_empty("Progress ID: ")
                progress_service.delete_progress(pid)

        except ValueError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

        # ------- LIST ALL -------
        if choice == "17":
            students = student_repo._load_data()
            if not students:
                print("No students found.")
            else:
                for s in students:
                    print(f"ID: {s['id']} | Name: {s['name']} | Email: {s['email']}")

        elif choice == "18":
            courses = course_repo._load_data()
            if not courses:
                print("No courses found.")
            else:
                for c in courses:
                    print(f"ID: {c['id']} | Title: {c['title']} | Instructor: {c['instructor']}")

        elif choice == "19":
            quizzes = quiz_repo._load_data()
            if not quizzes:
                print("No quizzes found.")
            else:
                for q in quizzes:
                    print(f"ID: {q['id']} | Course ID: {q['course_id']} | Title: {q['title']} | Max Score: {q['max_score']}")

        elif choice == "20":
            progresses = progress_repo._load_data()
            if not progresses:
                print("No progress records found.")
            else:
                for p in progresses:
                    print(f"ID: {p['id']} | Student ID: {p['student_id']} | Quiz ID: {p['quiz_id']} | Score: {p['score']}")

        # ------- EXIT / INVALID -------
        if choice == "21":
            logger.info("Application exited.")
            break
        elif choice not in valid_choices:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run()