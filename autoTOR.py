# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import requests
from stem import Signal
from stem.control import Controller

def check_and_install_dependencies():
    if sys.prefix == sys.base_prefix:
        print("This script should be run within a virtual environment.")
        sys.exit(1)

    try:
        import requests
    except ImportError:
        print('[+] "requests" package is not installed. Installing now...')
        subprocess.run(['pip', 'install', 'requests[socks]'], check=True)
        print('[!] "requests" package installed successfully.')

def get_external_ip():
    try:
        url = 'https://api.ipify.org'
        proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        response = requests.get(url, proxies=proxies)
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error obtaining IP: {str(e)}"

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='16:157DBAD6B40602A1607A935C65E0DE3F5F7426ED319C9E31A0BBCF4C38')
        controller.signal(Signal.NEWNYM)
    new_ip = get_external_ip()
    if "Error" not in new_ip:
        print(f'[+] Your IP has been changed to: {new_ip}')
    else:
        print(new_ip)



def main():
    print(r'''\033[1;32;40m
    _          _______
    /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
    / /\ \| | | | __/ _ \     | |/ _ \| '__|
    / ____ \ |_| | || (_) |    | | (_) | |
    /_/    \_\__,_|\__\___/     |_|\___/|_|
    V 2.1 from mrFD
    http://facebook.com/ninja.hackerz.kurdish/
    \033[0m''')

    os.system("sudo service tor start" if sys.platform.startswith('linux') else "brew services start tor")
    time.sleep(3)
    print("\033[1;32;40mChange your SOCKS to 127.0.0.1:9050\033[0m\n")

    time_interval = int(input("[+] Time to change IP in seconds [default=60] >> ") or "60")
    num_changes = input("[+] How many times do you want to change your IP [default=1000] (type 0 for infinite) >> ") or "1000"
    num_changes = int(num_changes)

    try:
        if num_changes == 0:
            while True:
                change_ip()
                time.sleep(time_interval)
        else:
            for _ in range(num_changes):
                change_ip()
                time.sleep(time_interval)
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == '__main__':
    check_and_install_dependencies()
    main()
