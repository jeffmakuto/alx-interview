#!/usr/bin/python3
import sys
from collections import defaultdict


def parse_log():
    """
    Reads stdin line by line, computes metrics, and prints statistics after every 10 lines
    or a keyboard interruption.

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    # Initialize variables to store metrics
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            # Split the line and extract relevant information
            parts = line.strip().split()
            if len(parts) != 7:
                continue  # Skip lines with incorrect format

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update total file size
            total_file_size += file_size

            # Update status code counts
            if status_code.isdigit():
                status_code_counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print("Total file size: File size:", total_file_size)
                for code in sorted(status_code_counts.keys(), key=int):
                    print(f"{code}: {status_code_counts[code]}")
                print()

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption

    # Print final statistics
    print("Total file size: File size:", total_file_size)
    for code in sorted(status_code_counts.keys(), key=int):
        print(f"{code}: {status_code_counts[code]}")

if __name__ == "__main__":
    parse_log()
