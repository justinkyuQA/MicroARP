from pathlib import Path

def show():

    print()
    print("MicroARP")
    print("=" * 40)

    arp = Path("/proc/net/arp")

    if not arp.exists():
        print("/proc/net/arp not found.")
        return

    print(arp.read_text())
