import json
import os
from src.logging_config import logger

class JsonRepository:
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.file_path = f"data/{entity_name.lower()}s.json"
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def _load_data(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            logger.error(f"Failed to load {self.entity_name} data.")
            return []

    def _save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"{self.entity_name}: Data saved successfully.")

    # --- READ ---
    def get_by_id(self, entity_id):
        data = self._load_data()
        return next((item for item in data if item.get("id") == entity_id), None)

    def get_by_id_key(self, key, value):
        data = self._load_data()
        return next((item for item in data if item.get(key) == value), None)

    def email_exists(self, email):
        return self.get_by_id_key("email", email) is not None

    # --- CREATE ---
    def create(self, entity):
        entity_dict = entity.to_dict()

        # Unique PK constraint
        if self.get_by_id(entity_dict["id"]):
            raise ValueError(f"ID '{entity_dict['id']}' already exists.")

        # Unique email for Student
        if self.entity_name == "Student":
            if self.email_exists(entity_dict["email"]):
                raise ValueError(f"Email '{entity_dict['email']}' already exists.")

        # Unique title for Course
        if self.entity_name == "Course":
            if self.get_by_id_key("title", entity_dict["title"]):
                raise ValueError(f"Course title '{entity_dict['title']}' already exists.")

        data = self._load_data()
        data.append(entity_dict)
        self._save_data(data)

        logger.info(f"{self.entity_name} created with ID {entity_dict['id']}")

    # --- UPDATE ---
    def update(self, entity_id, new_data):
        data = self._load_data()
        found = False

        for i, item in enumerate(data):
            if item["id"] == entity_id:
                data[i].update(new_data)
                found = True
                break

        if not found:
            raise ValueError(f"{self.entity_name} with ID '{entity_id}' not found.")

        self._save_data(data)
        logger.info(f"{self.entity_name} updated (ID: {entity_id})")

    # --- DELETE ---
    def delete(self, entity_id):
        data = self._load_data()
        new_data = [item for item in data if item["id"] != entity_id]

        if len(new_data) == len(data):
            raise ValueError(f"{self.entity_name} with ID '{entity_id}' not found.")

        self._save_data(new_data)
        logger.info(f"{self.entity_name} deleted (ID: {entity_id})")
