#!/bin/python3


import  subprocess
import  optparse
import  re
import colored
from   colored import fg, bg, attr
from   colored import stylize
from scapy import all as scapy
from scapy.all import srp,Ether,ARP,conf,send,arping,IP,sniff,sys

def main ():
        print_banner()
        (ip) = get_arguments()
        arp_scan(ip)
        
 
def print_banner():
        print (stylize("\n ___           ____  ______   __" +
                       "\n|_ _|         / ___||  _ \ \ / /" +
                       "\n | |   _____  \___ \| |_) \ V / " +
                       "\n |_|  |_____|  ___) |  __/ | |  " +
                       "\n|___|         |____/|_|    |_|  " +

                       "\n                         C0mproX v1.0  by Joe-Tec" + "\n", colored.fg('dark_goldenrod'))); 
        print(stylize("make sure to run I-SPY with sudo privileges !!! & restart your wifi connection after using I-SPY" , colored.fg('light_slate_blue')))

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--ip", dest="ip", help="Ex: -i 192.168.2.0/24")
	(options, arguments) = parser.parse_args()
	
	ip = options.ip
	
	if not ip :
		print(stylize('ERROR: please make sure that you enter a valid ip address. You can type -h for the help message', colored.bg("red")))
		quit()
	else:
		return (ip)
	


 
def arp_scan(ip):
 ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=2,verbose= True)
 ans.summary(lambda p: p[1].sprintf("Broadcast:%Ether.dst% %ARP.pdst% %Ether.src% %ARP.psrc%"))

 
main()
