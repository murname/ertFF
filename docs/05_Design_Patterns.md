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
`main.py` acts as the system controller.
