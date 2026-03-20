import argparse
from db.database import init_db
from cli.commands import live_monitor, log_stats, show_history


def main():
    parser = argparse.ArgumentParser(description="Cross-Platform System Monitor")
    parser.add_argument("command", choices=["live", "log", "history"])
    parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    init_db()

    if args.command == "live":
        live_monitor()
    elif args.command == "log":
        log_stats()
    elif args.command == "history":
        show_history(args.limit)


if __name__ == "__main__":
    main()