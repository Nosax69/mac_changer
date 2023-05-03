#!/bin/python3
import subprocess
import optparse

def get_arguments():
    p = optparse.OptionParser() #P is a instance & OptionParser() is for options
    p.add_option("-i", "--interface", dest="interface", help="Interface to change its New MAC Address")
    p.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = p.parse_args() #it will return the value
    if not options.interface:
        p.error("[-] Please specify an Interface, use --help for more info")
    elif not options.new_mac:
        p.error("[-] Please specify an Interface, use --help for more info")
    else:
        return options
        
         
def mac(interface, new_mac):
    print('\n')
    print("[+] Changing MAC Address")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print('\n')
    subprocess.call(["ifconfig"])

options = get_arguments() #options=user_input & arguments=--mac
mac(options.interface, options.new_mac)
