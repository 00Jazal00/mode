import json
import os

json_file_path = "airplane_mode.json"
def get_airplane_mode_status():
    with open(json_file_path, "r") as file:
        data = json.load(file)
        return data["airplane_mode"]

def set_airplane_mode_status(status):
    with open(json_file_path, "r+") as file:
        data = json.load(file)
        data["airplane_mode"] = "0"
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


os.system("git pull")
current_status = get_airplane_mode_status()
if current_status == "1":
    set_airplane_mode_status("0")
    os.system('git add . && git commit -m "Update" && git push')
