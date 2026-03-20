import psutil

def list_processes(limit=10):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append((
                proc.info['pid'],
                proc.info['name'],
                proc.info['cpu_percent']
            ))
        except:
            continue

    processes.sort(key=lambda x: x[2], reverse=True)
    return processes[:limit]