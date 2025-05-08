import tempfile
import os
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google.oauth2 import service_account
import time

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'

def upload_file_to_drive(file, folder_id):
    """Upload a file to Google Drive and return its ID and web view link."""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=creds)
    fd, tmp_filepath = tempfile.mkstemp(suffix=".pdf")
    os.close(fd) 
    filename = file.filename
    try:
        file.save(tmp_filepath)
        file_metadata = {
            'name': filename,
            'parents': [folder_id]
        }
        with open(tmp_filepath, 'rb') as f:
            media = MediaFileUpload(
                tmp_filepath, 
                mimetype='application/pdf',
                resumable=True
            )
            uploaded = drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id, webViewLink'
            ).execute()
        time.sleep(0.5)
        return uploaded['id'], uploaded['webViewLink']
    except Exception as e:
        print(f"Error uploading file to Drive: {e}")
        raise
    finally:
        for _ in range(3):
            try:
                if os.path.exists(tmp_filepath):
                    os.remove(tmp_filepath)
                break
            except PermissionError:
                time.sleep(1)