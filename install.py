import os

def install():
    print("[+] Installing Auto Tor IP Changer...")
    os.system('chmod 777 autoTOR.py')
    os.system('mkdir -p /usr/local/share/aut')
    os.system('cp autoTOR.py /usr/local/share/aut/autoTOR.py')

    command = '#! /bin/sh\nexec python3 /usr/local/share/aut/autoTOR.py "$@"'
    with open('/usr/local/bin/aut', 'w') as file:
        file.write(command)
    
    os.system('chmod +x /usr/local/bin/aut')
    os.system('chmod +x /usr/local/share/aut/autoTOR.py')
    print('''\n\nCongratulations! Auto Tor IP Changer is installed successfully.
From now, just type 'aut' in the terminal to use it.''')

def uninstall():
    print("[+] Uninstalling Auto Tor IP Changer...")
    os.system('rm -rf /usr/local/share/aut')
    os.system('rm /usr/local/bin/aut')
    print('[!] Auto Tor IP Changer has been removed successfully.')

def main():
    choice = input('[+] To install press (Y), to uninstall press (N) >> ')
    if choice.lower() == 'y':
        install()
    elif choice.lower() == 'n':
        uninstall()
    else:
        print("[!] Invalid input. Please enter 'Y' to install or 'N' to uninstall.")

if __name__ == '__main__':
    main()
