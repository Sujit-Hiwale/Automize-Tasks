import keyboard
import time
import json
import os

filename = input("Enter the filename to save the recording (without extension): ") + ".json"
SAVE_FILE = os.path.join(os.path.dirname(__file__), filename)
recorded_keys = []

def save_recording():
    with open(SAVE_FILE, "w") as f:
        json.dump(recorded_keys, f)
    print(f"Recording saved to {SAVE_FILE}")

print("Press 'Enter' to start recording (waiting indefinitely)...")
keyboard.wait("enter")

print("Recording started... (Press 'Delete' to stop)")
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "delete":
            break
        recorded_keys.append((event.name, time.time()))

save_recording()
