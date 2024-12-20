import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_numbers_100():
    for i in range(5):
        print(i * 100)

thread1 = threading.Thread(target=print_numbers)
thread1.start()
thread2 = threading.Thread(target=print_numbers_100)
thread2.start()
thread1.join()  # Waits for the thread to finish
thread2.join()  # Waits for the thread to finish
