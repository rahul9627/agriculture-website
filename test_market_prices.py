import unittest
from flask import Flask
from unittest.mock import MagicMock, patch
import sys
import os

# Mock MongoDB and other dependencies
sys.modules['pymongo'] = MagicMock()
sys.modules['pymongo.MongoClient'] = MagicMock()

# Add project path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'project_agri')))

from project_agri.crop_predict import app
from project_agri.models import User, bcrypt
from project_agri.market_prices import get_market_prices

class MarketPricesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.secret_key = 'test_secret_key'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        # Patch User in crop_predict for load_user and current_user checks
        self.user_patcher = patch('project_agri.crop_predict.User')
        self.mock_user_class = self.user_patcher.start()
        
        # Mock authenticated user
        self.mock_user = MagicMock()
        self.mock_user.is_authenticated = True
        self.mock_user.get_id.return_value = '1'
        self.mock_user_class.get.return_value = self.mock_user
        
        # Also need to patch models.User because it might be used elsewhere
        self.user_model_patcher = patch('project_agri.models.User')
        self.mock_user_model_class = self.user_model_patcher.start()
        self.mock_user_model_class.get.return_value = self.mock_user

    def tearDown(self):
        self.user_patcher.stop()
        self.user_model_patcher.stop()
        self.app_context.pop()

    def login(self):
        with self.app.session_transaction() as sess:
            sess['_user_id'] = '1'
            sess['_fresh'] = True

    def test_market_prices_page_loads(self):
        self.login()
        response = self.app.get('/market-prices', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Real-Time Market Prices', response.data)

    def test_mock_data_structure(self):
        data = get_market_prices(state="Maharashtra", commodity="Onion")
        self.assertTrue(len(data) > 0)
        item = data[0]
        self.assertEqual(item['state'], "Maharashtra")
        self.assertEqual(item['commodity'], "Onion")
        self.assertIn('min_price', item)
        self.assertIn('max_price', item)
        self.assertIn('modal_price', item)

    def test_filters(self):
        self.login()
        response = self.app.get('/market-prices?state=Punjab&commodity=Wheat', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Punjab', response.data)
        self.assertIn(b'Wheat', response.data)

if __name__ == '__main__':
    unittest.main()
