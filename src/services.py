from src.factory import EntityFactory
from src.logging_config import logger

class StudentService:
    def __init__(self, repo):
        self.repo = repo

    def create_student(self, student_id, name, email):
        student = EntityFactory.create_entity("Student", id=student_id, name=name, email=email)
        self.repo.create(student)
        logger.info(f"Student created (ID: {student_id})")

    def update_student(self, student_id, name, email):
        if not self.repo.get_by_id(student_id):
            logger.error(f"Student ID {student_id} not found for update")
            raise ValueError(f"Student ID {student_id} not found.")
        self.repo.update(student_id, {"name": name, "email": email})
        logger.info(f"Student updated (ID: {student_id})")

    def delete_student(self, student_id):
        if not self.repo.get_by_id(student_id):
            logger.error(f"Student ID {student_id} not found for delete")
            raise ValueError(f"Student ID {student_id} not found.")
        self.repo.delete(student_id)
        logger.info(f"Student deleted (ID: {student_id})")


class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def create_course(self, course_id, title, instructor):
        course = EntityFactory.create_entity("Course", id=course_id, title=title, instructor=instructor)
        self.repo.create(course)
        logger.info(f"Course created (ID: {course_id})")

    def update_course(self, course_id, title, instructor):
        if not self.repo.get_by_id(course_id):
            logger.error(f"Course ID {course_id} not found for update")
            raise ValueError(f"Course ID {course_id} not found.")
        self.repo.update(course_id, {"title": title, "instructor": instructor})
        logger.info(f"Course updated (ID: {course_id})")

    def delete_course(self, course_id):
        if not self.repo.get_by_id(course_id):
            logger.error(f"Course ID {course_id} not found for delete")
            raise ValueError(f"Course ID {course_id} not found.")
        self.repo.delete(course_id)
        logger.info(f"Course deleted (ID: {course_id})")


class QuizService:
    def __init__(self, repo, course_repo):
        self.repo = repo
        self.course_repo = course_repo

    def create_quiz(self, quiz_id, course_id, title, max_score):
    # Check course exists
        if not self.course_repo.get_by_id(course_id):
            raise ValueError(f"Course ID {course_id} does not exist.")
        quiz = EntityFactory.create_entity("Quiz", id=quiz_id, course_id=course_id, title=title, max_score=max_score)
        self.repo.create(quiz)

        logger.info(f"Quiz created (ID: {quiz_id})")

    def update_quiz(self, quiz_id, title, max_score):
        if not self.repo.get_by_id(quiz_id):
            logger.error(f"Quiz ID {quiz_id} not found for update")
            raise ValueError(f"Quiz ID {quiz_id} not found.")
        self.repo.update(quiz_id, {"title": title, "max_score": max_score})
        logger.info(f"Quiz updated (ID: {quiz_id})")

    def delete_quiz(self, quiz_id):
        if not self.repo.get_by_id(quiz_id):
            logger.error(f"Quiz ID {quiz_id} not found for delete")
            raise ValueError(f"Quiz ID {quiz_id} not found.")
        self.repo.delete(quiz_id)
        logger.info(f"Quiz deleted (ID: {quiz_id})")


class ProgressService:
    def __init__(self, student_repo, quiz_repo, progress_repo):
        self.student_repo = student_repo
        self.quiz_repo = quiz_repo
        self.progress_repo = progress_repo

    def create_progress(self, progress_id, student_id, quiz_id, score):
        # Referential integrity checks
        if not self.student_repo.get_by_id(student_id):
            logger.error(f"Student ID {student_id} does not exist for progress creation")
            raise ValueError("Student ID does not exist.")
        quiz_data = self.quiz_repo.get_by_id(quiz_id)
        if not quiz_data:
            logger.error(f"Quiz ID {quiz_id} does not exist for progress creation")
            raise ValueError("Quiz ID does not exist.")
        if score < 0 or score > quiz_data["max_score"]:
            logger.error(f"Score {score} out of range for quiz {quiz_id}")
            raise ValueError("Score out of range.")

        progress = EntityFactory.create_entity(
            "Progress", id=progress_id, student_id=student_id, quiz_id=quiz_id, score=score
        )
        self.progress_repo.create(progress)
        logger.info(f"Progress created (ID: {progress_id})")

    def update_progress(self, progress_id, score):
        progress = self.progress_repo.get_by_id(progress_id)
        if not progress:
            logger.error(f"Progress ID {progress_id} not found for update")
            raise ValueError(f"Progress ID {progress_id} not found.")
        quiz_data = self.quiz_repo.get_by_id(progress["quiz_id"])
        if score < 0 or score > quiz_data["max_score"]:
            logger.error(f"Score {score} out of range for quiz {progress['quiz_id']}")
            raise ValueError("Score out of range.")
        self.progress_repo.update(progress_id, {"score": score})
        logger.info(f"Progress updated (ID: {progress_id})")

    def delete_progress(self, progress_id):
        if not self.progress_repo.get_by_id(progress_id):
            logger.error(f"Progress ID {progress_id} not found for delete")
            raise ValueError(f"Progress ID {progress_id} not found.")
        self.progress_repo.delete(progress_id)
        logger.info(f"Progress deleted (ID: {progress_id})")
