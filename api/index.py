import os
import sys

# Add project_agri to path for imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(BASE_DIR, '..', 'project_agri'))
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)

app = None
init_error = None

try:
    from crop_predict import app as flask_app
    app = flask_app
except Exception as e:
    import traceback
    init_error = traceback.format_exc()

if init_error:
    from flask import Flask
    app = Flask(__name__)
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def error_page(path):
        return f"<h1>App Initialization Failed</h1><pre>{init_error}</pre>", 500
