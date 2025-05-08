import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Dict, Any

# Define the scope and the path to your service account file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/drive.file",
          ]
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'
def log(
    spreadsheet_name: str,
    worksheet_name: str,
    entries: List[Dict[str, Any]],
    value_input_option: str = 'RAW'
) -> Dict[str, Any]:
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
    client = gspread.authorize(creds)
    try:
        worksheet = client.open(spreadsheet_name).worksheet(worksheet_name)
    except gspread.WorksheetNotFound:
        raise ValueError(f"Worksheet '{worksheet_name}' not found in spreadsheet '{spreadsheet_name}'.")

    headers = worksheet.row_values(1)
    header_map = {h.strip(): idx for idx, h in enumerate(headers)}

    appended = 0
    for entry in entries:
        row = [''] * len(headers)
        for key, value in entry.items():
            if key in header_map:
                row[header_map[key]] = value
            else:
                raise KeyError(f"Column '{key}' not found in sheet headers {headers}")
        worksheet.append_row(row, value_input_option=value_input_option)
        appended += 1

    return {
        "status": "success",
        "spreadsheet": spreadsheet_name,
        "worksheet": worksheet_name,
        "rows_appended": appended
    }

# Example usage:
# if __name__ == "__main__":
#     entries = [
#         {"Name": "John Doe", "Age": 30, "City": "New York"}, 
#         {"Name": "Jane Smith", "Age": 25, "City": "Los Angeles"}
#     ]
#     result = log("MySpreadsheet", "Sheet1", entries)
#     print(result)  # This will print the result of the log function