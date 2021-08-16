"""Read spreadsheet and save records in `records.json`"""

import json
import tfmsheetreader

if __name__ == "__main__":
    spreadsheet = tfmsheetreader.read_spreadsheet("1xoPZXT5apgKm1Z5J-YEv-sXTQ6BjB0vnPgrWLxhRpaU")
    print(f"{len(spreadsheet)} records found")

    with open("records.json", "w") as f:
        json.dump(spreadsheet, f)