import evdev
from evdev import InputDevice, categorize, ecodes
import serial
import time

Serial_port = '/dev/ttyUSB0'
Baudrate = 115200


# --- 1. List and pick controller ---
devices = [InputDevice(path) for path in evdev.list_devices()]
print("Available input devices:")
for dev in devices:
    print(f"  {dev.path}: {dev.name}")

device_path = input("Enter the device path of your controller (e.g. /dev/input/event3): ")
controller = InputDevice(device_path)
print(f"Listening to {controller.name}...\n")

# --- 2. Open serial port to ESP32 ---
ser = serial.Serial(Serial_port, Baudrate, timeout=0.1)
time.sleep(2)  # give ESP32 time to reset after serial open

# --- 3. Define mapping from EV_KEY to command strings ---
KEY_COMMAND_MAP = {
    'BTN_': "X_P",
    'BTN_':  "X_N",
    'BTN_': "Y_P",
    'BTN_':  "Y_N",
    'BTN_': "Z_P",
    'BTN_':  "Z_N",}

def send_command(cmd: str):
    """We send a newline-terminated command over serial"""
    cmd_msg = (cmd + '\n').encode('ascii') # we encode it in ASCII for processing later on ESP32
    ser.write(cmd_msg)
    print(f">>> Sent: {cmd}")

# --- 4. Event loop: detect button presses and send commands ---
for event in controller.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        if key.keystate == key.key_down:
            code = key.keycode if isinstance(key.keycode, str) else key.keycode[0]
            cmd = KEY_COMMAND_MAP.get(code)
            if cmd:
                send_command(cmd)
            else:
                print(f"(No mapping for {code})")

