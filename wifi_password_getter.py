"""
This file is used to retrieve the passwords of any wifi you have connected to (Ever)
"""

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for profile in profiles:
    try:

        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode("utf-8").split("\n")
        password_lines = [line.split(':')[1][1:-1] for line in results if 'Key Content' in line]
        

        if password_lines:
            print("{:<30}|  {:<}".format(profile, password_lines[0]))
        else:
            print("{:<30}|  {:<}".format(profile, "Password not found"))
    except:
        pass
