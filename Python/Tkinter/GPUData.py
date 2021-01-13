import GPUtil
from tabulate import tabulate

def info():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature}°C"        
        gpu_uuid = gpu.uuid
        list_gpus.append(( gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_total_memory, gpu_temperature, gpu_uuid))
    
    return str(tabulate(list_gpus, headers=("ID", "NAME", "LOAD", "Free Memory", "Used Memory", "Total Memory", "Temperature", "UUID"), teblefmt="pretty"))

if __name__ == "__main__":
    print(info())
