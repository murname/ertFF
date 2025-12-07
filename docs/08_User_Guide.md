# User Guide — Interactive CLI

## Running the Application
To start the E-Learning Management System, run the following command in your terminal:

```bash
python main.py

## Menu Options
```
1. Add Student: Create a new student profile (Name, Email).
2. Add Course: Create a new course (Title, Instructor).
3. Add Quiz: Add a quiz to a specific Course (Title, Max Score).
4. Add Progress: Record a student's score for a specific Quiz.
5. View Student
6. View Course
7. View Quiz
8. View Progress
9. Update Student: Change Name or Email.
10. Update Course: Change Title or Instructor.
11. Update Quiz: Change Title or Max Score.
12. Update Progress: Change the recorded Score.
13. Delete Student
14. Delete Course
15. Delete Quiz
16. Delete Progress
17. List All Students
18. List All Courses
19. List All Quizzes
20. List All Progress
21. Exit: Close the application.

## Data Storage
All actions write to JSON files in:

```
/data/*.json
```

## Purpose
Allows simple end-user interaction for creating and viewing Students, Courses, Quizzes, and Progress records in Sprint 1.
