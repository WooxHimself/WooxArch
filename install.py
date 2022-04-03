import os
import time

print("""

▄▄▌ ▐ ▄▌            ▐▄• ▄    ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
██· █▌▐█ ▄█▀▄  ▄█▀▄  █▌█▌▪  ▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
██▪▐█▐▐▌▐█▌.▐▌▐█▌.▐▌ ·██·   ▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▀█
▐█▌██▐█▌▐█▌.▐▌▐█▌.▐▌▪▐█·█▌  ▐█▪ ▐▌▐█•█▌▐███▌██▌▐▀
 ▀▀▀▀ ▀▪ ▀█▄▀▪ ▀█▄▀▪•▀▀ ▀▀   ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·


       Woox's Automated Arch Linux Installer
""")

print("1: /dev/sda")
drive = input("What drive do you want your Arch Linux install to?")

if drive == '1':
    print("PLEASE PARTITION YOUR DRIVES WITH CFDISK")
    print("Swap: 1G")
    print("Boot: 500M")
    print("Root: -Remaining Space-")
    input("Press [ENTER] to continue")
    os.system("cfdisk")
    print("Formating /dev/sda1 in")
    print('3')
    time.sleep(0.7)
    print('2')
    time.sleep(0.5)
    print('1')
    time.sleep(0.3)
    os.system('mkfs.ext4 /dev/sda3')
    os.system('mkfs.fat -F 32 /dev/sda2')
    os.system('mkswap /dev/sda1')
    print("Drives has been parititioned")
    os.system('mount /dev/sda3 /mnt')
    os.system('mkdir /mnt/boot')
    os.system('mount /dev/sda2 /mnt/boot')
    os.system('swapon /dev/sda1')
    print("Drives Mounted")
    print("Installing Firmware & Basics")
    os.system('pacstrap /mnt base linux linux-firmware')
    os.system('genfstab /mnt >> /mnt/etc/fstab')
    os.system('arch-chroot /mnt')
    os.system('pacman -S grub')
    os.system('grub-install /dev/sda')
    os.system('grub-mkconfig /boot/grub/grub.cfg')
    os.system('pacman -S sudo xfce4')
    print("Enter your new Root Password")
    os.system('passwd')
    usrname = input("Enter name for a new user: ")
    os.system('useradd -m ' + usrname)
    os.system("echo " + usrname + " ALL=(ALL:ALL) NOPASSWD: ALL")
    print("Created a new user and made him root")
    print("Enter a password for your new user " + usrname)
    print("Done!")
    print("Rebooting in 3...")
    time.sleep(1)
    print("Rebooting in 2...")
    time.sleep(1)
    print("Rebooting in 1...")
    time.sleep(1)
    os.system('exit')
    os.system('reboot')

