# Architecture Documentation

## Folder Structure

/project_root
/src
models.py
factory.py
repository.py
/tests
test_repository.py
/docs
(*.md files)
main.py
/data
students.json
courses.json
quizzes.json
progress.json

## Core Architectural Decisions

### 1. Use of JSON for Storage
- Simple and lightweight  
- Perfect for Sprint 1 prototyping  
- Requires no external database  
- Human-readable data format  

### 2. Repository Layer
Implements the Dependency Inversion Principle:

- `AbstractRepository` defines the interface  
- `JsonRepository` implements create/read persistence  

### 3. Factory Pattern
Used to create entity objects dynamically.  
Improves scalability and reduces coupling.

### 4. High Cohesion, Low Coupling
- Each class has a clearly defined purpose.
- Storage logic is isolated from business classes.
- Object creation is isolated from logic (Factory).

## Interactions
- User → main.py (controller)
- main.py → Factory → Model Objects
- main.py → Repository → JSON Data
