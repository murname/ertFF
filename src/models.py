import uuid

# Abstraction/Inheritance Base Class
class BaseModel:
    """Provides common properties and serialization structure."""
    def __init__(self, id_val=None):
        # Encapsulation: Use uuid for robust, unique IDs if none is provided
        self._id = id_val if id_val is not None else str(uuid.uuid4())

    def get_id(self):
        return self._id

    def to_dict(self):
        """Converts the object to a dictionary for storage."""
        raise NotImplementedError("Subclasses must implement to_dict()")
    
    # Polymorphic base method (will be overridden)
    def display_details(self):
        raise NotImplementedError("Subclasses must implement display_details()")

class Student(BaseModel):
    """Represents a student in the platform."""
    def __init__(self, student_id, name, email):
        super().__init__(student_id)
        # Encapsulation
        self._name = name 
        self._email = email

    def display_details(self):
        # Polymorphism
        return f"Student ID: {self._id}, Name: {self._name}, Email: {self._email}"

    def to_dict(self):
        return {'student_id': self._id, 'name': self._name, 'email': self._email}

class Course(BaseModel):
    """Represents an e-learning course."""
    def __init__(self, course_id, title, instructor):
        super().__init__(course_id)
        # Encapsulation
        self._title = title
        self._instructor = instructor

    def display_details(self):
        # Polymorphism
        return f"Course ID: {self._id}, Title: {self._title} by {self._instructor}"

    def to_dict(self):
        return {'course_id': self._id, 'title': self._title, 'instructor': self._instructor}

class Quiz(BaseModel):
    """Represents an assessment for a course."""
    def __init__(self, quiz_id, course_id, title, max_score):
        super().__init__(quiz_id)
        self._course_id = course_id
        self._title = title
        self._max_score = max_score

    def display_details(self):
        return f"Quiz ID: {self._id}, Title: {self._title} (Max: {self._max_score}) for Course: {self._course_id}"

    def to_dict(self):
        return {'quiz_id': self._id, 'course_id': self._course_id, 'title': self._title, 'max_score': self._max_score}

class Progress(BaseModel):
    """Tracks a student's score on a specific quiz."""
    def __init__(self, progress_id, student_id, quiz_id, score):
        super().__init__(progress_id)
        # Composition relationship via IDs
        self._student_id = student_id
        self._quiz_id = quiz_id
        self._score = score

    def display_details(self):
        return f"Progress ID: {self._id} | Student: {self._student_id} scored {self._score} on Quiz: {self._quiz_id}"

    def to_dict(self):
        return {'progress_id': self._id, 'student_id': self._student_id, 'quiz_id': self._quiz_id, 'score': self._score}
