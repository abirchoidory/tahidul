cyan="\033[0;36m"         # Cyan
color_off="\033[0m"       # Text Reset
import sys

def exit():
	sys.exit()
	
def sub():
	import math
	a=int(input("\n\n\tENTER FIRST NUMBER\t:"))
	b=int(input("\n\n\tENTER SECEND NUMBER\t:"))
	c=str(math.gcd(a,b))
	print("The GCD Number Of This Two Numbers Is:"+c)
	
def hello():
	year=int(input("\n\n\tENTER THE YEAR:\t\t"))
	if year%4==0:
		print("\n\n\t\tTHIS IS A LEAP YEAR\t\t")
	else:
		print("\n\n\t\tTHIS IS NOT A LEAP YEAR\n\n\t\t")
	
logo=str(cyan+""" _______    _______        _______    _______   _________
(       )  (  ____ )      (  ____ )  (  ___  )  \__    _/
| () () |  | (    )|      | (    )|  | (   ) |     )  (  
| || || |  | (____)|      | (____)|  | (___) |     |  |  
| |(_)| |  |     __)      |     __)  |  ___  |     |  |  
| |   | |  | (\ (         | (\ (     | (   ) |     |  |  
| )   ( |  | ) \ \__      | ) \ \__  | )   ( |  |\_)  )  
|/     \|  |/   \__/      |/   \__/  |/     \|  (____/   
                                                         
""")
line=("____________________TR TAHIDUL RAJ______________________________________________________________________________________\n\n\n\n\t\t")

version=str("     [VERTION 1.2.0]")

logo2=("\n\n\n\tHACKING NOT A CRIMR ×× IT's MY PASSION")
logo3=("\n\n\t\tDEVLOPER BY TR TAHIDUL RAJ")

logo4=("\n\n\t\tFACEBOOK ACCOUNT Tâ Hî Dúl")

print(logo+line+version+logo3+logo4+logo2+color_off)

print("\n\n\n\n[>]SELECT YOUR OPTION\n\n[1]LEAP YEAR CHACK\n\n[2]GCD NUMBER RESULT\n\n[0]EXIT\n\n")

otp=int(input("[$$]ENTER YOUR OPTION NUMBER\t"))

if otp==1:
	hello()
elif otp==2:
	sub()
elif otp==0:
	exit()