import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Mock pymongo before importing models
sys.modules['pymongo'] = MagicMock()
sys.modules['pymongo.MongoClient'] = MagicMock()

# Add project path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'project_agri')))

from project_agri.models import User

class UserModelTestCase(unittest.TestCase):
    @patch('project_agri.models.get_users_collection')
    def test_save_success(self, mock_get_collection):
        mock_collection = MagicMock()
        mock_get_collection.return_value = mock_collection
        mock_collection.insert_one.return_value.inserted_id = 'mock_id'
        
        user = User('test', 'test@example.com', 'password')
        self.assertTrue(user.save())
        self.assertEqual(user.id, 'mock_id')

    @patch('project_agri.models.get_users_collection')
    def test_save_connection_failure(self, mock_get_collection):
        mock_get_collection.return_value = None
        user = User('test', 'test@example.com', 'password')
        self.assertFalse(user.save())

    @patch('project_agri.models.get_users_collection')
    def test_save_exception(self, mock_get_collection):
        mock_collection = MagicMock()
        mock_get_collection.return_value = mock_collection
        mock_collection.insert_one.side_effect = Exception("Database error")
        
        user = User('test', 'test@example.com', 'password')
        self.assertFalse(user.save())

if __name__ == '__main__':
    unittest.main()
