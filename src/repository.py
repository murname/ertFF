import json
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('DataRepository')

class AbstractRepository:
    
    def create(self, entity):
        raise NotImplementedError
    def get_by_id(self, entity_id):
        raise NotImplementedError

class JsonRepository(AbstractRepository):
    
    def __init__(self, entity_name):
        self.entity_name = entity_name
        
        self.file_path = f'data/{entity_name.lower()}s.json'
        
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    
    def create(self, entity):
        
        data = self._load_data()
        entity_dict = entity.to_dict() 
        data.append(entity_dict)
        self._save_data(data)
        logger.info(f"Created {self.entity_name} with ID: {entity.get_id()}") 

    
    def get_by_id(self, entity_id):
       
        data = self._load_data()
        
       
        id_key = f"{self.entity_name.lower()}_id"
        
       
        return next((item for item in data if item.get(id_key) == entity_id), None)

    
    def _load_data(self):
        
        try:
            if not os.path.exists(self.file_path) or os.stat(self.file_path).st_size == 0:
                return []
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            
            logger.error(f"Error loading data from {self.file_path}: {e}")
            return []

    
    def _save_data(self, data):
        
        try:
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logger.error(f"Error saving data to {self.file_path}: {e}")
