import os
import sys

# Add the project_agri directory to sys.path so imports within crop_predict.py work
sys.path.append(os.path.join(os.path.dirname(__file__), '../project_agri'))

from crop_predict import app
