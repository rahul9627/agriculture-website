import os
import sys

# Add project_agri to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'project_agri'))

# Import the Flask app
try:
    from crop_predict import app
except ImportError as e:
    # If it fails, let's try to give a useful error if Vercel allows it to start
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def error():
        return f"Import Error: {str(e)}", 500
