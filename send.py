import evdev
import serial
from evdev import InputDevice, categorize, ecodes

SELECT_HEX       = 'f'
L3_HEX           = 'a'
R3_HEX           = 'A'
START_HEX        = 'F'

TRIANGLE_HEX     = 'C'
CIRCLE_HEX       = 'B'
CROSS_HEX        = 'b'
SQUARE_HEX       = 'c'

L2_HEX           = 'e'
R2_HEX           = 'E'
L1_HEX           = 'd'
R1_HEX           = 'D'

EVDEV_SELECT     = "BTN_SELECT"
EVDEV_L3         = "BTN_THUMBL"
EVDEV_R3         = "BTN_THUMBR"
EVDEV_START      = "BTN_START"
EVDEV_L2         = "BTN_TL2"
EVDEV_R2         = "BTN_TR2"
EVDEV_L1         = "BTN_TL"
EVDEV_R1         = "BTN_TR"
EVDEV_TRIANGLE   = "['BTN_NORTH', 'BTN_X']"
EVDEV_CIRCLE     = "['BTN_B', 'BTN_EAST']"
EVDEV_CROSS      = "['BTN_A', 'BTN_GAMEPAD', 'BTN_SOUTH']"
EVDEV_SQUARE     = "['BTN_WEST', 'BTN_Y']"



# Init the serial port of the Raspberry Pi
Serial_port = '/dev/ttyAMA0' #GPIO 14 and 15
baudrate = 112500
ser = serial.Serial(Serial_port, baudrate, timeout=1)

# Clear the input buffer
ser.reset_input_buffer()

# List all input devices
devices = [InputDevice(path) for path in evdev.list_devices()]

# Print the list of devices and find your controller
print("Available input devices:")
for device in devices:
    print(f"{device.path}: {device.name}")

# Replace 'your_device_path' with the path of your controller
# For example, it might look like '/dev/input/eventX'
device_path = input("Enter the device path of your controller: ")
controller = InputDevice(device_path)

print(f"Listening to {controller.name}...")

# Read events from the controller
for event in controller.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)

        if   (str(key_event.keycode) == EVDEV_TRIANGLE):
                #is_pressed = TRIANGLE_HEX
                ser.write(TRIANGLE_HEX.encode())
                print("TRIANGLE_HEX")
        elif (str(key_event.keycode) == EVDEV_CIRCLE):
                #is_pressed = CIRCLE_HEX
                ser.write(CIRCLE_HEX.encode())
                print("CIRCLE_HEX")
        elif (str(key_event.keycode) == EVDEV_CROSS) :
                #is_pressed = CROSS_HEX
                ser.write(CROSS_HEX.encode())
                print("CROSS_HEX")
        elif (str(key_event.keycode) == EVDEV_SQUARE) :    
                #is_pressed = SQUARE_HEX    
                ser.write(SQUARE_HEX.encode())
                print("SQUARE_HEX")

        elif (str(key_event.keycode) == EVDEV_R1):
                #is_pressed = R1_HEX
                ser.write(R1_HEX.encode())
                print("R1_HEX")
        elif (str(key_event.keycode) == EVDEV_R2) :
                #is_pressed = R2_HEX
                ser.write(R2_HEX.encode())
                print("R2_HEX")
        elif (str(key_event.keycode) == EVDEV_L1) :
                #is_pressed = L1_HEX
                ser.write(L1_HEX.encode())
                print("L1_HEX")
        elif (str(key_event.keycode) == EVDEV_L2):
                #is_pressed = L2_HEX
                ser.write(L2_HEX.encode())
                print("L2_HEX")

        elif (str(key_event.keycode) == EVDEV_SELECT) :
                #is_pressed = SELECT_HEX
                ser.write(SELECT_HEX.encode())
                print("SELECT_HEX")
        elif (str(key_event.keycode) == EVDEV_START) :
                #is_pressed = START_HEX
                ser.write(START_HEX.encode())
                print("START_HEX")
        else :
                print(f"{key_event.keycode} // {key_event.keystate}")


        # ser.write(f"{is_pressed}\n".encode())
        #is_pressed = 0x0000
        # print(type(key_event)._name_)
        # str_key_event = str(key_event.keycode)
        # print(str_key_event)
        # print(type(str_key_event)._name_)
    # elif event.type == ecodes.EV_ABS:
        # abs_event = categorize(event)
        # print(f"Axis: {abs_event.event.code}, Value: {abs_event.event.value}")