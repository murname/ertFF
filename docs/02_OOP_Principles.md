# OOP Principles Applied in the Project

## 1. Abstraction
`BaseModel` defines abstract behaviors such as:
- `to_dict()`
- `display_details()`

Subclasses implement them.

## 2. Encapsulation
Model attributes use `_`:
- `_name`, `_email`, `_title`, `_score`

Data is accessed through methods.

## 3. Inheritance
All entities inherit from `BaseModel`:
- Student
- Course
- Quiz
- Progress

## 4. Polymorphism
Each class overrides:
- `display_details()`

Same method name → different behaviors.

## 5. SOLID Principles
- **S (SRP):** each class has a single purpose  
- **O (OCP):** new models can be added without rewriting existing ones  
- **L (LSP):** all subclasses behave like BaseModel  
- **I (ISP):** no class has unnecessary methods  
- **D (DIP):** The Controller relies on the Repository interface (high-level methods), decoupling it from the low-level data storage details.

## 6. GRASP Principles
- Creator → Factory  
- Controller → main.py  
- Low Coupling → Repository & Factory separation  
- High Cohesion → single-purpose classes  

## 7. CUPID Principles
- Composable  
- Understandable  
- Predictable  
- Idiomatic  
- Domain-based  
