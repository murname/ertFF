# Class Documentation

## BaseModel
Common parent class for all entities.
- Handles IDs
- Defines abstract methods

## Student
Attributes:
- student_id
- name
- email

Purpose:
Represents a user of the learning system.

## Course
Attributes:
- course_id
- title
- instructor

Purpose:
Represents an educational course.

## Quiz
Attributes:
- quiz_id
- course_id
- title
- max_score

Purpose:
Assessment belonging to a course.

## Progress
Attributes:
- progress_id
- student_id
- quiz_id
- score

Purpose:
Stores a student's score on a quiz.

## EntityFactory
Creates:
- Student
- Course
- Quiz
- Progress

Purpose:  
Centralized object creation using the Factory Pattern.

## Repository (JsonRepository)
Handles:
- JSON data loading  
- Saving  
- ID-based searches  

Purpose:  
Provide persistence layer independent of core logic.
