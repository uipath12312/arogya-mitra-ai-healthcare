import os
from datetime import datetime
from werkzeug.utils import secure_filename

class S3Service:
    def __init__(self):
        # Use local file storage instead of S3
        self.upload_folder = os.path.join(os.getcwd(), 'uploads')
        os.makedirs(self.upload_folder, exist_ok=True)
    
    def upload_file(self, file) -> str:
        """Upload medical document to local storage"""
        try:
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            new_filename = f"{timestamp}_{filename}"
            filepath = os.path.join(self.upload_folder, new_filename)
            
            file.save(filepath)
            
            return f"local://{new_filename}"
        
        except Exception as e:
            print(f"File upload error: {e}")
            return None
