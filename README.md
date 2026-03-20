# sysmon

Simple CLI-based system monitor.

## Run

```bash
python main.py live
```

## Other Commands

```bash
python main.py log       # log system stats to database
python main.py history   # view logged stats
```

## Controls (live mode)

* q → quit
* r → refresh
* + → faster
* - → slower

## Requirements

```bash
pip install psutil
```

## Notes

* Cross-platform (Windows + Linux)
* Uses SQLite (`sysmon.db`) for logging
* Run from this directory (root of project)
