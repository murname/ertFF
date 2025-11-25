# tests/test_repository.py

import unittest
import os
import shutil
import json
from src.repository import JsonRepository
from src.models import Student, Course

# Set up a temporary testing environment
TEST_DATA_DIR = 'test_data'

class TestJsonRepository(unittest.TestCase):
    
    def setUp(self):
        """Setup runs before each test method."""
        # Override the repository file path for testing purposes
        self.student_repo = JsonRepository("Student")
        self.student_repo.file_path = os.path.join(TEST_DATA_DIR, 'students.json')
        
        # Create a temporary data directory (Architecture Setup)
        os.makedirs(TEST_DATA_DIR, exist_ok=True)
        
        # Ensure test file is clean before each test
        if os.path.exists(self.student_repo.file_path):
            os.remove(self.student_repo.file_path)

    # Test Basic Functionality: Create and Read [cite: 26]
    def test_create_and_read(self):
        student_id = "S001"
        student1 = Student(student_id, "Alice Smith", "alice@example.com")
        
        # 1. Create (Save)
        self.student_repo.create(student1)
        
        # 2. Read (Retrieve)
        retrieved_data = self.student_repo.get_by_id(student_id)
        
        self.assertIsNotNone(retrieved_data)
        self.assertEqual(retrieved_data['student_id'], student_id)
        self.assertEqual(retrieved_data['name'], "Alice Smith")

    # Test for handling empty or missing files (Exception Handling) [cite: 28]
    def test_load_empty_file(self):
        # The file doesn't exist yet, it should return an empty list.
        data = self.student_repo._load_data()
        self.assertEqual(data, [])

    def test_multiple_creations(self):
        self.student_repo.create(Student("S002", "Bob", "bob@e.com"))
        self.student_repo.create(Student("S003", "Charlie", "charlie@e.com"))
        
        data = self.student_repo._load_data()
        self.assertEqual(len(data), 2)
        
    def tearDown(self):
        """Teardown runs after each test method."""
        # Remove the temporary test data directory
        if os.path.exists(TEST_DATA_DIR):
            shutil.rmtree(TEST_DATA_DIR)

# To run tests, use: python -m unittest tests.test_repository.py
