#!/bin/bash

# Step 1: Run Cuckoo Rooter
gnome-terminal --title="Cuckoo Rooter" -- bash -c "echo '[password user]' | sudo -S cuckoo rooter --sudo --group [user]"
sleep 2
xdotool search --onlyvisible --name "Cuckoo Rooter" windowminimize

# Step 3: Run Cuckoo Web
gnome-terminal --title="Cuckoo Web" -- cuckoo web --host 127.0.0.1 --port 8080
sleep 3
xdotool search --onlyvisible --name "Cuckoo Web" windowminimize

# Step 4: Configure VBoxNet0 IP (if required)
vboxnet0_config=$(VBoxManage hostonlyif ipconfig vboxnet0)
if [[ $vboxnet0_config != *"IP: 192.168.56.1"* ]]; then
    VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1 --netmask 255.255.255.0
fi
sleep 2

# Step 5: Run Cuckoo
gnome-terminal --title="Cuckoo" -- cuckoo
sleep 5
xdotool search --onlyvisible --name "Cuckoo" windowminimize

# Step 6: Open Cuckoo Web interface
xdg-open http://127.0.0.1:8080



