from multiprocessing import Process, Queue
import serial
import time

def serial_reader(queue):
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    while True:
        if ser.in_waiting:
            data = ser.readline().decode().strip()
            print(f"[Serial] Received: {data}")
            queue.put(data)

def esp32_commander(queue):
    while True:
        if not queue.empty():
            data = queue.get()
            print(f"[ESP32] Processing: {data}")
            # Add your command logic here
            # For example, send a command to ESP32 over socket or serial
            # esp_socket.send(data.encode())

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=serial_reader, args=(q,))
    p2 = Process(target=esp32_commander, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
