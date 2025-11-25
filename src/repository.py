
import json
import os
import logging

# Configure basic logging (for basic functionality) [cite: 28]
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DataRepository')

class AbstractRepository:
    """Abstract interface defining the repository contract (for DIP)."""
    def create(self, entity):
        raise NotImplementedError
    def get_by_id(self, entity_id):
        raise NotImplementedError

class JsonRepository(AbstractRepository):
    """Handles JSON-based persistence for a specific entity type."""
    def __init__(self, entity_name):
        self.entity_name = entity_name
        # The file path is determined by the entity name
        self.file_path = f'data/{entity_name.lower()}s.json'
        # Ensures the data directory exists (Architecture Setup) [cite: 14]
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    # Implements Basic CRUD: Create [cite: 26]
    def create(self, entity):
        """Adds a new entity (dictionary) to the JSON file."""
        data = self._load_data()
        entity_dict = entity.to_dict() # Uses Student A's to_dict() method
        data.append(entity_dict)
        self._save_data(data)
        logger.info(f"Created {self.entity_name} with ID: {entity.get_id()}") # Logging [cite: 68]

    # Implements Basic CRUD: Read [cite: 26]
    def get_by_id(self, entity_id):
        """Retrieves an entity (dictionary) by its ID."""
        data = self._load_data()
        
        # Determine the correct ID key based on the entity name
        id_key = f"{self.entity_name.lower()}_id"
        
        # Search the list for the matching ID
        return next((item for item in data if item.get(id_key) == entity_id), None)

    # Helper method with exception handling [cite: 28, 68]
    def _load_data(self):
        """Loads data from the JSON file, handling errors."""
        try:
            if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
                return []
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Basic exception handling [cite: 28]
            logger.error(f"Error loading data from {self.file_path}: {e}")
            return []

    # Helper method with exception handling [cite: 28, 68]
    def _save_data(self, data):
        """Saves data to the JSON file."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logger.error(f"Error saving data to {self.file_path}: {e}")
