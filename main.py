from src.factory import EntityFactory
from src.repository import JsonRepository
from src.utils import input_non_empty, input_optional_id, input_number, input_alpha_spaces
from src.logging_config import logger

def run():
    logger.info("Application started")

    student_repo = JsonRepository("Student")
    course_repo = JsonRepository("Course")
    quiz_repo = JsonRepository("Quiz")
    progress_repo = JsonRepository("Progress")

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
        print("17. Exit")

        choice = input("Select option: ")

        # ------- CREATE -------
        try:
            if choice == "1":
                sid = input_optional_id("Student ID (Enter for auto): ")
                name = input_alpha_spaces("Name: ")
                email = input_non_empty("Email: ")
                student = EntityFactory.create_entity("Student", id=sid, name=name, email=email)
                student_repo.create(student)

            elif choice == "2":
                cid = input_optional_id("Course ID: ")
                title = input_alpha_spaces("Title: ")
                instr = input_alpha_spaces("Instructor: ")
                course = EntityFactory.create_entity("Course", id=cid, title=title, instructor=instr)
                course_repo.create(course)

            elif choice == "3":
                qid = input_optional_id("Quiz ID: ")
                cid = input_non_empty("Course ID: ")
                title = input_non_empty("Quiz Title: ")
                max_s = input_number("Max Score: ")
                quiz = EntityFactory.create_entity("Quiz", id=qid, course_id=cid, title=title, max_score=max_s)
                quiz_repo.create(quiz)

            elif choice == "4":
                pid = input_optional_id("Progress ID: ")
                sid = input_non_empty("Student ID: ")
                qid = input_non_empty("Quiz ID: ")
                score = input_number("Score: ")

                # Referential integrity checks
                if not student_repo.get_by_id(sid):
                    raise ValueError("Student ID does not exist.")
                quiz_data = quiz_repo.get_by_id(qid)
                if not quiz_data:
                    raise ValueError("Quiz ID does not exist.")
                if score < 0 or score > quiz_data["max_score"]:
                    raise ValueError("Score out of range.")

                progress = EntityFactory.create_entity("Progress", id=pid, student_id=sid, quiz_id=qid, score=score)
                progress_repo.create(progress)

        except ValueError as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

        # ------- READ -------
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

        # ------- UPDATE -------
        elif choice == "9":
            sid = input_non_empty("Student ID to update: ")
            name = input_alpha_spaces("New Name: ")
            email = input_non_empty("New Email: ")
            student_repo.update(sid, {"name": name, "email": email})

        elif choice == "10":
            cid = input_non_empty("Course ID to update: ")
            title = input_alpha_spaces("New Title: ")
            instr = input_alpha_spaces("New Instructor: ")
            course_repo.update(cid, {"title": title, "instructor": instr})

        elif choice == "11":
            qid = input_non_empty("Quiz ID to update: ")
            title = input_non_empty("New Title: ")
            max_s = input_number("New Max Score: ")
            quiz_repo.update(qid, {"title": title, "max_score": max_s})

        elif choice == "12":
            pid = input_non_empty("Progress ID to update: ")
            score = input_number("New Score: ")
            progress_repo.update(pid, {"score": score})

        # ------- DELETE -------
        elif choice == "13":
            sid = input_non_empty("Student ID: ")
            student_repo.delete(sid)

        elif choice == "14":
            cid = input_non_empty("Course ID: ")
            course_repo.delete(cid)

        elif choice == "15":
            qid = input_non_empty("Quiz ID: ")
            quiz_repo.delete(qid)

        elif choice == "16":
            pid = input_non_empty("Progress ID: ")
            progress_repo.delete(pid)

        elif choice == "17":
            logger.info("Application exited.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run()
