import keyboard
import time

recorded_keys = []

print("Ready to start the recording: Press \"Enter\"")
rec = keyboard.read_event()
if rec.name == "enter":
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "enter":
                break
            recorded_keys.append((event.name, time.time()))

start = keyboard.read_event()
print("Ready to Execute the recording: Press \"Enter\"")
if start.name == "enter":
    while True:
        if keyboard.read_event().name == "`":
            start_time = recorded_keys[0][1]
            
            for key, timestamp in recorded_keys:
                time.sleep(timestamp - start_time)
                keyboard.press_and_release(key)
                start_time = timestamp
            if key.name == "esc":
                break