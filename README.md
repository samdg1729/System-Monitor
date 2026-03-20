# sysmon

Simple CLI-based system monitor.

## Setup and Run

```bash
git clone https://github.com/samdg1729/System-Monitor.git
cd System-Monitor/sysmon
pip install -r requirements.txt
python main.py live
```

## Other Commands

```bash
python main.py log       # log system stats
python main.py history   # view logs
```

## Shortcut (optional)

```bash
./sysmon live        # Linux/macOS
.\sysmon.bat live    # Windows
```

## Controls

* q → quit
* r → refresh
* `+` → faster
* `-` → slower

## Requirements

```bash
pip install psutil
```

## Notes

* Cross-platform (Windows and Linux)
* Uses SQLite (`sysmon.db`) for logging
* Run commands from the project root directory
