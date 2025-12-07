# Architecture Documentation

## Folder Structure

/erFF
    /src
        models.py
        factory.py
        repository.py
        utils.py
        logging_config.py
        services.py
    /tests
        test_models.py
        test_repository.py
        test_services.py
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

### 2. Repository Layer (Isolation and Persistence)
This design implements the **Repository Pattern** to decouple the application from the data layer.

 **JsonRepository:** This class handles all data persistence (reading/writing JSON files) and enforces 
 **Decoupling:** Storage logic is isolated; the Controller (`main.py`) only interacts with the          repository's high-level methods, not the JSON files directly.

### 3. Factory Pattern
Used to create entity objects dynamically.  
Improves scalability and reduces coupling.

### 4. High Cohesion, Low Coupling
- Each class has a clearly defined purpose.
    Models: store data structure and to_dict() method.
    Repository: persistence only.
    Factory: object creation.
    Services: business logic.
    Main.py: handles user input and orchestrates operations.
- Storage logic is isolated from business classes.
- Object creation is isolated from logic (Factory).

## Interactions
- User → main.py (controller)
- Controller → Service Layer
- Service → Factory → Model Objects
- Service → Repository → JSON Data

## Data Flow Example
- User selects “Add Student” in CLI.
- main.py collects student info.
- StudentService.create_student() is called.
- EntityFactory creates a Student object.
- JsonRepository.create() stores the object in students.json.
- Logging records the operation.
