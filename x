asn1crypto==0.22.0
bcrypt==3.1.3
cffi==1.10.0
cryptography==2.0
enum34==1.1.6
idna==2.5
ipaddress==1.0.18
pyasn1==0.2.3
pycparser==2.18
PyNaCl==1.1.2
pytz==2017.2
six==1.10.0

#!/bin/sh
cd ~
ln -s /media/ubuntu/OSDisk/Users/user1/Desktop/git c
#sudo fallocate -l 4G /home/ubuntu/c/swapfile
#mkswap /home/ubuntu/c/swapfile
#swapon /dev/sdb2
sudo cp -a ~/c/sources.list /etc/apt/sources.list
sudo apt update
sudo apt install -y libpython-all-dev
sudo apt install -y python-pip
sudo apt install -y git
git config --global user.email "1@1.1"
git config --global push.default simple
pip install --upgrade pip
sudo pip install virtualenv
#sudo apt install -y vlc
. ~/c/env/bin/activate
pip install -r ~/c/netops-api/requirements.txt
exit 0

deb cdrom:[Ubuntu 16.04.3 LTS _Xenial Xerus_ - Release amd64 (20170801)]/ xenial main restricted
deb http://archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse #Added by software-properties
deb http://security.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://security.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse #Added by software-properties
deb http://archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse #Added by software-properties

