import time
import os
import platform
import psutil

from monitor.cpu import get_cpu_usage
from monitor.memory import get_memory_usage
from monitor.process import list_processes
from monitor.disk import get_disk_usage
from db.database import insert_stats, fetch_history


# -------------------------------
# Cross-platform key input
# -------------------------------
if platform.system() == "Windows":
    import msvcrt

    def get_key():
        if msvcrt.kbhit():
            try:
                return msvcrt.getch().decode("utf-8").lower()
            except:
                return None
        return None
else:
    import sys
    import select
    import termios
    import tty

    def get_key():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None


# Enable ANSI support on Windows
if platform.system() == "Windows":
    os.system("")


# -------------------------------
# Screen control (no flicker)
# -------------------------------
def clear_screen_once():
    print("\033[2J", end="")  # clear once


def move_cursor_top():
    print("\033[H", end="")  # move cursor


# -------------------------------
# LIVE MONITOR (with controls)
# -------------------------------
def live_monitor():
    psutil.cpu_percent(interval=None)  # warm-up

    refresh_rate = 1.0

    # Setup Linux terminal for non-blocking input
    if platform.system() != "Windows":
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(fd)

    clear_screen_once()

    try:
        while True:
            move_cursor_top()

            cpu = get_cpu_usage(interval=0.3)
            mem_used, mem_total = get_memory_usage()
            disk = get_disk_usage()
            processes = list_processes()

            output = []
            output.append("=== SYSTEM MONITOR ===\n")
            output.append("Controls: q=quit | r=refresh | +=faster | -=slower\n")
            output.append(f"Refresh rate: {round(refresh_rate, 2)}s\n\n")

            output.append(f"CPU Usage: {cpu}%\n")
            output.append(
                f"Memory: {mem_used // (1024 * 1024)}MB / {mem_total // (1024 * 1024)}MB\n"
            )
            output.append(
                f"Disk: {disk['percent']}% ({disk['used']}GB / {disk['total']}GB)\n"
            )

            output.append("\nTop Processes:\n")
            output.append(f"{'PID':<8}{'Name':<25}{'CPU%':>8}\n")
            output.append("-" * 45 + "\n")

            for pid, name, cpu_percent in processes:
                name = (name[:22] + "...") if len(name) > 25 else name
                output.append(f"{pid:<8}{name:<25}{cpu_percent:>8}%\n")

            print("".join(output), end="")

            # -------------------------------
            # Handle keyboard input
            # -------------------------------
            start = time.time()

            while time.time() - start < refresh_rate:
                key = get_key()

                if key:
                    if key == "q":
                        return
                    elif key == "r":
                        break
                    elif key == "+":
                        refresh_rate = max(0.2, refresh_rate - 0.2)
                    elif key == "-":
                        refresh_rate += 0.2

                time.sleep(0.05)

    finally:
        # Restore terminal settings (Linux only)
        if platform.system() != "Windows":
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# -------------------------------
# LOGGING FUNCTION
# -------------------------------
def log_stats():
    print("Logging started... Press Ctrl+C to stop.")

    try:
        while True:
            cpu = get_cpu_usage(interval=0.5)
            mem_used, mem_total = get_memory_usage()
            disk = get_disk_usage()

            insert_stats(cpu, mem_used, mem_total)

            print(f"Logged: CPU {cpu}% | Memory {mem_used // (1024 * 1024)}MB | Disk {disk['percent']}%")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nLogging stopped.")


# -------------------------------
# HISTORY FUNCTION
# -------------------------------
def show_history(limit=10):
    rows = fetch_history(limit)

    print("=== HISTORY ===")

    for row in rows:
        ts, cpu, mem_used, mem_total = row
        print(f"{ts} | CPU: {cpu}% | Mem: {mem_used // (1024 * 1024)}MB")