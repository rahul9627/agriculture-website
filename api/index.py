import os
import sys

# Add project_agri to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'project_agri'))

from crop_predict import app
