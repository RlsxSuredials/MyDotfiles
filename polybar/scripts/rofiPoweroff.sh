#!/bin/bash

rofi_poweroff_menu () {
     echo -e "    Logout\n󰜉    Reboot\n󰤆    Shutdown" | rofi -show run -font "HackNerd Bold 11" -show-icons -width 20 -l 3 -dmenu -i
}

chosen=$(rofi_poweroff_menu)

if [[ $chosen = "    Logout" ]]; then
    pkill -KILL -u $USER
elif [[ $chosen = "󰤆    Shutdown" ]]; then
    systemctl poweroff
elif [[ $chosen = "󰜉    Reboot" ]]; then
    systemctl reboot
fi

