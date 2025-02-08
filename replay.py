import keyboard
import time
import json
import os

SCRIPT_DIR = os.path.dirname(__file__)
json_files = [f for f in os.listdir(SCRIPT_DIR) if f.endswith(".json")]
file_mapping = {str(i + 1): json_files[i] for i in range(len(json_files))}

print("Available recordings:")
for key, filename in file_mapping.items():
    print(f"{key}: {filename}")

def load_recording(file):
    save_file = os.path.join(os.path.dirname(__file__), file)
    try:
        with open(save_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No saved recording found for {file}.")
        return []

def replay_keys(recorded_keys):
    if not recorded_keys:
        print("No recorded keys found. Skipping replay.")
        return
    
    print("Replaying recorded keys...")
    start_time = recorded_keys[0][1]
    
    for key, timestamp in recorded_keys:
        time.sleep(timestamp - start_time)
        keyboard.press_and_release(key)
        start_time = timestamp
    
    print("Replay finished!")

while True:
    key_event = keyboard.read_event()
    key = key_event.name

    if key in file_mapping:
        file = file_mapping[key]
        recorded_keys = load_recording(file)
        replay_keys(recorded_keys)

    elif key == "esc":
        print("Exiting...")
        break
