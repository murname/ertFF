# Unit Testing Documentation (Sprint 1)

## Framework
- Python's built-in `unittest` module.

## Test File
- `tests/test_models.py`

## Purpose
Ensures the system works correctly:
- Repository saves and loads data properly.  
- Entities are created with correct attributes.  
- ID generation and inheritance behave as expected.  
- Factory handles object creation and errors.  
- Errors and edge cases are handled gracefully.

---

## Tests Implemented

### A. BaseModel (Inheritance / ID Logic)
- test_base_model_abstract: Verifies that `BaseModel` cannot be instantiated directly.  
- test_base_model_auto_id_generation: Ensures objects get a unique ID when none is provided.  
- test_base_model_provided_id: Confirms that objects use a given ID if provided.

### B. Student Class (Encapsulation / Validation)
- test_student_creation: Checks successful creation of a `Student` object.  
- test_student_to_dict: Validates that `to_dict()` outputs the correct structure.  

**Notes:**  
- Validates that `name` and `email` attributes exist.  
- Ensures that `email` follows standard format.  

### C. Course Class
- test_course_creation: Checks successful creation of a `Course` object.  
- test_course_display_details: Confirms the `display_details()` output format.

### D. Factory Integration
- test_factory_creates_student: Verifies that `EntityFactory` creates a `Student`.  
- test_factory_creates_quiz_correctly: Verifies creation of a `Quiz` object with multiple arguments.  
- test_factory_raises_error_on_unknown_type: Ensures invalid entity types raise a `ValueError`.

### E. Suggested / Future Tests
- Progress creation: Ensure `Progress` links `Student` and `Quiz` correctly.  
- Score validation: Prevent scores exceeding `Quiz.max_score`.  
- Repository integration: Test saving, loading, and retrieving entities with `JsonRepository`.  
- Cleanup: Remove temporary test files after execution to avoid pollution.  

---

## Example Test Flow
1. Attempt to create a `BaseModel` → Expect failure.  
2. Create a `Student` without ID → Verify auto-generated UUID.  
3. Create a `Course` → Verify attributes and display output.  
4. Use `EntityFactory` to create multiple entities → Confirm types and attributes.  
5. Check error handling for invalid factory input.  

---

## Notes
- Unit tests focus on **core functionality** and **data integrity**.  
- They provide a foundation for **future sprints**, including repository and validation enhancements.  
- All tests are designed to be **isolated, repeatable, and self-contained**.  
