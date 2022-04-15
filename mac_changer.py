import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address" )
    parser.add_option("-m","--mac", dest="new_mac", help="new Mac address")
    (options ,argumnents) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more info..")
    elif not options.new_mac:
        parser.error("[+] Please specify an interface, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] changing Mac address for "  +   interface   +   " to "    +   new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    
    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("[-] sorry could not read mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current Mac[-] " )

change_mac(options.interface, options.new_mac)


current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address did not get changed.. " + current_mac )

else:
    print("[+]MAC address was succesfully changed as per your request.. ")




print("------Thank you for using my Program ------")