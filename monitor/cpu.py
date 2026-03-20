import psutil

def get_cpu_usage(interval=1):
    return psutil.cpu_percent(interval=interval)