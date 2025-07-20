# Chang-Mac-Address-in-kali
get_current_mac(interface): Retrieves the current MAC address using either ifconfig on Linux or getmac on Windows.

change_mac(interface, new_mac): Changes the MAC address by bringing the interface down, changing the hardware address, and bringing it back up (Linux only).

main(): Handles CLI arguments like --interface and --mac, prints the current MAC, attempts to change it, then confirms if it was changed.


