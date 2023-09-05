from socket import gethostbyname
from pyfiglet import figlet_format
from termcolor import colored
from time import sleep
sleep(0.06)
a = colored(figlet_format("Domain Ip"),'green')
print(a)
sleep(1)
m = colored("Enter Domain Name:",'green')
target = input(m)
print()
print("Target Domain:",target)
getip = str(gethostbyname(target))
print(target,"Ip:",getip)
print()
sleep(0.7)