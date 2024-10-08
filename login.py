from pystyle import *
print(Box.Lines("[+] Learning pyton [+]"))
Write.Print("[+] this program for login page [+] \n",Colors.purple_to_red,interval=0.1)
Write.Print("[+] write user name and password [+] \n \n ",Colors.purple_to_red,interval=0.1)
print(Box.DoubleCube("Example 1"))
while True:
    Username = Write.Input('Write Username:',Colors.blue_to_green, interval=0.1)
    password=Write.Input('Write Password:',Colors.black_to_green,interval=0.1)
    if(Username=='Meriem' and password=='123456'): 
      Write.Print("Welcome Admin",Colors.black_to_green,interval=0.1)
      input ('\n press any key to exit ...')
      break
    else:
      Write.Print("Try again",Colors.red,interval=0.1)


