# This Python script retrieves the history of Wi-Fi networks that a device 
# has previously connected to. It uses the netsh command-line utility to 
# get information about the Wi-Fi profiles stored on the device. 
# For each profile, it checks if a security key is present. 
# If a security key is present, it retrieves the password for that profile 
# and stores the profile name and password in a list. Finally, it prints 
# out each item in the list, which contains the name and password of a 
# previously connected Wi-Fi network. The script does not explain the code, 
# but it provides a summary of its functionality.

# This code is not licensed under any particular license.

import subprocess
import re

wifi_profile_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
wifi_names = (re.findall("All User Profile     : (.*)\r", wifi_profile_output))
wifi_list = []
if len(wifi_names) != 0:
    for name in wifi_names:
        wifi_profile = {}
        wifi_profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", wifi_profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            wifi_profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", wifi_profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    print(wifi_list[x])