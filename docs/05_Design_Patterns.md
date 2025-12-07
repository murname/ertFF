# Design Patterns

## Factory Pattern
Used in `factory.py`.

### Why?
- Removes creation logic from other classes  
- Allows dynamic instantiation  
- Supports adding new entity types easily  

## Repository Pattern
Used in `repository.py`.

### Why?
- Separates storage logic from domain classes  
- Supports DIP (Dependency Inversion)  
- Allows switching storage types without changing logic  

## Controller Pattern (GRASP)
Location: main.py
Purpose: Orchestrates application flow and user interactions.
## Why:
- Acts as the single entry point for user commands
- Delegates tasks to services
- Keeps business logic and storage isolated


## Logging as Cross-Cutting Concern
Location: logging_config.py
Purpose: Centralizes logging for audit and debugging.
## Why:
- Services and repository log all operations
- Helps trace errors and user actions