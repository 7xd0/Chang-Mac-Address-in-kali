import subprocess
import argparse
import re
import platform

def get_current_mac(interface):
    """
    Get the current MAC address of the specified network interface.
    """
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(f"getmac /v /fo list", shell=True).decode()
            match = re.search(rf"Physical Address[^\n]*:\s+([-\w]{{17}})", output)
        else:
            output = subprocess.check_output(["ifconfig", interface]).decode()
            match = re.search(r"ether ([0-9a-fA-F:]{17})", output)

        return match.group(1) if match else None
    except Exception as e:
        return None

def change_mac(interface, new_mac):
    """
    Change the MAC address of the specified network interface.
    """
    if platform.system() == "Windows":
        print("[!] Windows requires manual registry changes or external drivers.")
    else:
        print(f"[+] Changing MAC address of {interface} to {new_mac}")
        subprocess.call(["sudo", "ifconfig", interface, "down"])
        subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["sudo", "ifconfig", interface, "up"])

def main():
    parser = argparse.ArgumentParser(description="MAC Address Changer Tool")
    parser.add_argument("-i", "--interface", help="Network interface name (e.g., eth0 or wlan0)", required=True)
    parser.add_argument("-m", "--mac", help="New MAC address (e.g., 00:11:22:33:44:55)", required=True)

    args = parser.parse_args()

    current_mac = get_current_mac(args.interface)
    if current_mac:
        print(f"[i] Current MAC of {args.interface} is {current_mac}")
    else:
        print("[!] Could not read current MAC address.")

    change_mac(args.interface, args.mac)

    new_mac = get_current_mac(args.interface)
    if new_mac == args.mac:
        print("[✔] MAC address changed successfully.")
    else:
        print("[✘] MAC address change failed.")

if __name__ == "__main__":
    main()
