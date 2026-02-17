import base64
from pathlib import Path

# Image data from the user's uploaded image
image_data = """your_base64_image_data_here"""

# Save to static folder
output_path = Path(r"C:\Users\rawat\OneDrive\Desktop\Projects\Agriculture_Website-main\project_agri\static\rahul_photo.jpg")

# For now, just create a placeholder - the user will need to manually place their photo
print(f"Please manually copy your photo to: {output_path}")
print("Or use the existing myphoto.jpg and replace it with your photo")
