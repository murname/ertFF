# Data Persistence

## Storage Method: JSON Files

### Why JSON?
- Lightweight  
- Easy to implement  
- Good for prototyping  
- No external DB needed  

## File Structure
Files stored in /data:

- students.json  
- courses.json  
- quizzes.json  
- progress.json  

## CRUD Supported
- Create (append to JSON)
- Read (search by ID)
- Update: Modify fields, preserving constraints (email/title uniqueness needs additional checks)
- Delete: Remove entries; referential integrity currently needs caution
## Error Handling
Handled using try/except in:
- `_load_data()`
- `_save_data()`

## Logging
Operations logged with Python's `logging` module.
