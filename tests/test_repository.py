import unittest
import os
import shutil
import json
from src.repository import JsonRepository
from src.models import Student, Course


TEST_DATA_DIR = 'test_data'

class TestJsonRepository(unittest.TestCase):
    
    def setUp(self):

        self.student_repo = JsonRepository("Student")
        self.student_repo.file_path = os.path.join(TEST_DATA_DIR, 'students.json')
        
        os.makedirs(TEST_DATA_DIR, exist_ok=True)
        
        if os.path.exists(self.student_repo.file_path):
            os.remove(self.student_repo.file_path)

    def test_create_and_read(self):
        student_id = "S001"
        student1 = Student(student_id, "Alice Smith", "alice@example.com")
        
      
        self.student_repo.create(student1)
        
     
        retrieved_data = self.student_repo.get_by_id(student_id)
        
        self.assertIsNotNone(retrieved_data)
        self.assertEqual(retrieved_data['student_id'], student_id)
        self.assertEqual(retrieved_data['name'], "Alice Smith")


    def test_load_empty_file(self):
      
        data = self.student_repo._load_data()
        self.assertEqual(data, [])

    def test_multiple_creations(self):
        self.student_repo.create(Student("S002", "Bob", "bob@e.com"))
        self.student_repo.create(Student("S003", "Charlie", "charlie@e.com"))
        
        data = self.student_repo._load_data()
        self.assertEqual(len(data), 2)
        
    def tearDown(self):
        
      
        if os.path.exists(TEST_DATA_DIR):
            shutil.rmtree(TEST_DATA_DIR)

# To run tests, use: python -m unittest tests.test_repository.py
