#!/usr/bin/python3
#
# Title: ip_update_panel.py
# Author: G0TH3R
# Description:
#     The code validates an IP address provided as a command-line argument, 
#     and if valid, writes it to the file "/path/to/file/ip_vm.txt". If no IP 
#     address is provided, it prompts the user to provide one.
#
# usage:
#           ip_update_panel.py <ip address>
#

import re
import sys

def write_ip_to_file(ip_address, file_path):
    # Validate the IP address format
    if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_address):
        print("Invalid IP address format.")
        return
    
    # Write the IP address to the file
    with open(file_path, 'w') as file:
        file.write(ip_address)

# Check if the IP address argument is provided
if len(sys.argv) < 2:
    print("Usage: ip_update_panel.py <ip_address>")
else:
    ip_address = sys.argv[1]
    file_path = "/path/to/file/ip_vm.txt"
    write_ip_to_file(ip_address, file_path)
