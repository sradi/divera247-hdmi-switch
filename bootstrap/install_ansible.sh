#! /bin/bash
# run this as root!

# update sources.list
export ansibleSourceListEntry="deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main"
grep -qxF "${ansibleSourceListEntry}" /etc/apt/sources.list || echo "${ansibleSourceListEntry}" >> /etc/apt/sources.list

apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
apt update
apt install ansible
