# src/factory.py

from src.models import Student, Course, Quiz, Progress

class EntityFactory:
    """Factory for creating different entity objects dynamically."""
    
    @staticmethod
    def create_entity(entity_type, **kwargs):
        """
        Creates an instance of the requested entity type based on kwargs.
        This handles object instantiation (GRASP Creator).
        """
        if entity_type == 'Student':
            return Student(
                student_id=kwargs.get('id'), 
                name=kwargs.get('name'), 
                email=kwargs.get('email')
            )
        elif entity_type == 'Course':
            return Course(
                course_id=kwargs.get('id'), 
                title=kwargs.get('title'), 
                instructor=kwargs.get('instructor')
            )
        elif entity_type == 'Quiz':
            return Quiz(
                quiz_id=kwargs.get('id'), 
                course_id=kwargs.get('course_id'), 
                title=kwargs.get('title'),
                max_score=kwargs.get('max_score')
            )
        elif entity_type == 'Progress':
            return Progress(
                progress_id=kwargs.get('id'), 
                student_id=kwargs.get('student_id'), 
                quiz_id=kwargs.get('quiz_id'),
                score=kwargs.get('score')
            )
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
