# sysmon

Simple CLI-based system monitor.

## Run

```bash
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

* Works on Windows and Linux
* Uses SQLite (`sysmon.db`)
* Run from the project root directory

