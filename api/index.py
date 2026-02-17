import os
import sys

# Add the project_agri directory to sys.path so imports within crop_predict.py work
sys.path.append(os.path.join(os.path.dirname(__file__), '../project_agri'))

try:
    from crop_predict import app
except Exception as e:
    import traceback
    error_msg = traceback.format_exc()
    print(error_msg)
    
    # Create a dummy app to show the error in the browser if it fails to load
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    @app.route('/<path:path>')
    def catch_all(path=None):
        return f"<pre>Initialization Error:\n{error_msg}</pre>", 500
