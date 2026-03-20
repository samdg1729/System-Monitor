import psutil

def get_disk_usage():
    disk = psutil.disk_usage('/')
    
    return {
        "percent": disk.percent,
        "used": disk.used // (1024**3),
        "total": disk.total // (1024**3)
    }