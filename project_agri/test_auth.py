import unittest
from unittest.mock import patch
from crop_predict import app, db
from models import User, bcrypt

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        # Patch analytics functions before they are imported in routes
        self.patcher1 = patch('analytics.track_visit')
        self.patcher2 = patch('analytics.track_page_view')
        self.mock_track_visit = self.patcher1.start()
        self.mock_track_page_view = self.patcher2.start()

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def register(self, username, email, password, confirm_password):
        return self.app.post(
            '/register',
            data=dict(username=username, email=email, password=password, confirm_password=confirm_password),
            follow_redirects=True
        )

    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_user_registration(self):
        response = self.register('testuser', 'test@example.com', 'password123', 'password123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your account has been created!', response.data)
        
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'test@example.com')
            self.assertTrue(bcrypt.check_password_hash(user.password, 'password123'))

    def test_login_logout(self):
        self.register('testuser', 'test@example.com', 'password123', 'password123')
        response = self.login('test@example.com', 'password123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logout (testuser)', response.data)
        
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_invalid_login(self):
        self.register('testuser', 'test@example.com', 'password123', 'password123')
        response = self.login('test@example.com', 'wrongpassword')
        self.assertIn(b'Login Unsuccessful', response.data)

    def test_protected_route(self):
        # Access analytics while logged out
        response = self.app.get('/analytics', follow_redirects=True)
        # Should redirect to login
        self.assertIn(b'Login', response.data)
        self.assertIn(b'Account', response.data)
        
        # Log in and try again
        self.register('testuser', 'test@example.com', 'password123', 'password123')
        self.login('test@example.com', 'password123')
        response = self.app.get('/analytics', follow_redirects=True)
        # Should show analytics dashboard
        self.assertIn(b'Analytics', response.data)
        self.assertIn(b'Dashboard', response.data)

if __name__ == '__main__':
    unittest.main()
