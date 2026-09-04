import os
import time
from datetime import datetime

BASE = "/sdcard/JHER_PC_CHECKER"
REPORT = os.path.join(BASE, "jher_mobile_report.txt")

def header():
    print("\n" + "=" * 36)
    print("        JHER CP CHECKER")
    print("=" * 36)

def full_scan():
    header()
    print("[FULL SCAN]")
    print("Starting...")
    for i in range(0, 101, 10):
        print(f"[{'#' * (i // 10)}{'-' * (10 - i // 10)}] {i}%")
        time.sleep(0.08)

    accessible = os.path.exists("/sdcard")
    count = len(os.listdir("/sdcard")) if accessible else 0

    report = (
        "JHER CP CHECKER\n"
        f"Date: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        f"Storage accessible: {accessible}\n"
        f"Accessible items: {count}\n"
        "Status: COMPLETED\n"
    )

    os.makedirs(BASE, exist_ok=True)
    with open(REPORT, "w") as f:
        f.write(report)

    print("\nSCAN COMPLETE")
    print("REPORT SAVED")

def device_info():
    header()
    print("DEVICE INFO")
    print("Platform: Android / Pydroid 3")
    print("Python: 3.13.13")

def storage_scan():
    header()
    print("STORAGE SCAN")
    if os.path.exists("/sdcard"):
        items = os.listdir("/sdcard")
        print("Accessible items:", len(items))
        for item in items[:20]:
            print("-", item)
    else:
        print("Storage unavailable.")

def view_report():
    header()
    if os.path.exists(REPORT):
        print(open(REPORT).read())
    else:
        print("No report yet.")

while True:
    header()
    print("[1] FULL SCAN")
    print("[2] DEVICE INFO")
    print("[3] STORAGE SCAN")
    print("[4] VIEW REPORT")
    print("[5] EXIT")

    choice = input("\nJHER > ")

    if choice == "1":
        full_scan()
    elif choice == "2":
        device_info()
    elif choice == "3":
        storage_scan()
    elif choice == "4":
        view_report()
    elif choice == "5":
        print("Goodbye, Jher!")
        break
    else:
        print("Invalid option.")

    input("\nPress Enter to continue...")
