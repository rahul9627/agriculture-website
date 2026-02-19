import unittest
from flask import Flask, session
from flask_login import current_user
import sys
import os
from unittest.mock import MagicMock, patch

# Mock MongoDB before importing app
sys.modules['pymongo'] = MagicMock()
sys.modules['pymongo.MongoClient'] = MagicMock()

# Add project path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'project_agri')))

from project_agri.crop_predict import app
from project_agri.models import User, bcrypt

class GlobalAuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.secret_key = 'test_secret_key'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        # Patch User
        self.user_patcher_models = patch('project_agri.models.User')
        self.user_patcher_auth = patch('project_agri.auth.User')
        self.user_patcher_cp = patch('project_agri.crop_predict.User')
        
        self.mock_user_class_models = self.user_patcher_models.start()
        self.mock_user_class_auth = self.user_patcher_auth.start()
        self.mock_user_class_cp = self.user_patcher_cp.start()
        
        # Setup mock user
        self.mock_user = MagicMock()
        self.mock_user.password = bcrypt.generate_password_hash('password123').decode('utf-8')
        self.mock_user.is_authenticated = True
        self.mock_user.is_active = True
        self.mock_user.is_anonymous = False
        self.mock_user.get_id.return_value = '507f1f77bcf86cd799439011'
        
        # Configure behaviors
        self.mock_user_class_auth.find_by_email.return_value = self.mock_user
        self.mock_user_class_cp.get.return_value = self.mock_user
        self.mock_user_class_models.get.return_value = self.mock_user

    def tearDown(self):
        self.user_patcher_models.stop()
        self.user_patcher_auth.stop()
        self.user_patcher_cp.stop()
        self.app_context.pop()

    def test_redirect_to_login(self):
        # Ensure we are logged out
        self.app.get('/logout')
        
        # Try to access root
        response = self.app.get('/', follow_redirects=True)
        
        # Should be redirected to login page logic (which renders 'login.html')
        # We check content or status usually. Since we follow redirects, we check content.
        self.assertIn(b'action="/login"', response.data)

    def test_authenticated_access(self):
         # Log in
        self.app.post('/login', data=dict(
             email='test@example.com',
             password='password123'
         ), follow_redirects=True)
         
        # Try to access root
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Should NOT be login page
        # The home page usually has "Home" or "Agri-Solutions"
        self.assertIn(b'Agri-Solutions', response.data)

if __name__ == '__main__':
    unittest.main()
