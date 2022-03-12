#!/usr/bin/env python3

import os
import subprocess
import time

x = int(input("Please enter seconds for check time : "))

def arp() -> list:
    os.system("arp -a > deneme.txt")
    liste = []
    with open("deneme.txt", "r") as file:
        for i in file:
            liste.append(list(i.split(" ")))
    os.system("rm -rf deneme.txt")
    return liste

def control(liste) -> bool:
    warning = 0
    i = 0
    while (i < len(liste) - 1):
        j = i + 1
        while (j < len(liste)):
            if (liste[i][3] == liste[j][3]):
                warning = 1
                break
            j += 1
        if warning:
            break
        i+=1

    return warning

def messages(warn) -> None:
    if warn:
        os.system("sudo ifconfig eth0 down")
        subprocess.Popen(['notify-send', "YOU ARE UNDER THE ATTACK!\nYour internet connection has been blocked.\n(for reopen command 'ifconfig eth0 up')"])
    else:
        os.system("sudo ifconfig eth0 up")
        subprocess.Popen(['notify-send', "You are in safe."])

if __name__ == "__main__":
    while 1:
        messages(control(arp()))
        time.sleep(x)