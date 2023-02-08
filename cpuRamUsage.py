import time
import psutil
import platform

def sys_info():
    a = platform.platform()
    b = platform.system()
    c = platform.processor()

    print("Your platform is: "+a)
    print("Your os is :"+b)
    print("Your processor is based on: "+c)
    print("\n\n")

sys_info()

def display_usage(cpu_usage, mem_usage, bars = 50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) #cpu değerini progress bar benzeri göstermek için kullanıldı (alt+219(numpad ile))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)
