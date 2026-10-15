# First Project!
# Systems CLI Project
# system cli project testing done, code cleaned up.

import psutil
import platform
import socket

user = input( "Choose an Option king:\n""1:"  " System information \n""2:" " Memory information \n" "3:" " Storage information " "\n4: " "Display all of the above" "\nexit?")

def diskinfo():
    print('========STORAGE========')
    print(f"Disk Space Used: {system_data['storage used']:.2f} GB")
    print(f"Disk Space Total: {system_data['total storage']:.2f} GB")
    print(f"Disk Space Usage: {system_data['percentage of storage used']:.2f}%")

def meminfo():
    print('========MEMORY========')
    print(f"Memory Used: {system_data["memory used"]:.2f} GB")
    print(f"Total Memory: {system_data['total memory']:.2f} GB")
    print(f"Memory Usage: {system_data["percentage being used"]:.2f}%")
    print(f"Swap Memory Used: {system_data["swap used"]:.2f} GB")
    print(f"Swap Memory Total: {system_data["swap total"]:.2f} GB")
    print(f"Swap Memory Usage: {system_data["swap percentage being used"]:.2f}%")

def sysinfo():
    print('========SYSTEM========')
    print('OS:',system_data["OS"])
    print('Machine:', system_data["machine"])
    print('Python Ver:', system_data["python ver"])
    print('Host Name:',system_data["host name"])
    print('Cpu:',system_data["cpu"],)
    print('Cpu usage:',system_data["cpu usage"],'%')
    print('Cpu Cores (physical):', system_data["cores"])

def get_system_info():
    memory = psutil.virtual_memory()
    storage = psutil.disk_usage('/')
    swap_memory = psutil.swap_memory()

    return {"cpu": platform.processor(),
             "OS": platform.system(),
             "machine":platform.machine(),
             "python ver":platform.python_version(),
            "host name": socket.gethostname(),
            "cores":psutil.cpu_count(logical=False),
             "cpu usage":psutil.cpu_percent(),
            #memory
            "memory used": memory.used / 1024 / 1024 / 1024,
             "total memory": memory.total / 1024 / 1024 / 1024,
             "percentage being used":memory.percent,
             "swap used":swap_memory.used / 1024 / 1024 / 1024,
             "swap total": swap_memory.total / 1024 / 1024 / 1024,
             "swap percentage being used":swap_memory.percent,
            "storage used": storage.used / 1024 / 1024 / 1024,
            #storage
             "total storage": storage.total / 1024 / 1024 / 1024,
             "percentage of storage used": storage.percent}

system_data = get_system_info()

if user == "1":
    sysinfo()

elif user == "2":
    meminfo()

elif user == "3":
    diskinfo()

elif user == "4":
    sysinfo()
    meminfo()
    diskinfo()

elif user == "exit":
    print("Goodbye, have a nice day")

else:
    print(f"{user} is not valid. Please Pick either: 1, 2, 3; 4 or exit if you would like:).")





