import time
import psutil

def print_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage is {cpu_percent}%")

if __name__ == "__main__":
    while True:
        print_cpu_percent()
        time.sleep(1) # wait for 1 second before taking the next 
measurement

