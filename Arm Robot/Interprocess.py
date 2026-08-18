from multiprocessing import Process, Queue
import time

def sender(queue):
    message = "Hello from Process 1"
    print("[Sender] Sending message...")
    queue.put(message)

def receiver(queue):
    print("[Receiver] Waiting for message...")
    message = queue.get()  # This blocks until a message is available
    print(f"[Receiver] Received: {message}")

if __name__ == "__main__":
    q = Queue()

    # Create both processes
    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()
