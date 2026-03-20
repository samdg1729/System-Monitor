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

## Controls (live mode)

* q → quit
* r → refresh
* `+` → faster
* `-` → slower

## Notes

* Cross-platform (Windows and Linux)
* Uses SQLite (`sysmon.db`) for logging
* Run commands from the project root directory
