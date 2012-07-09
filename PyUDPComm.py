"""
 PyUDPComm - A Basic UDP Communicator
 Version : 1.0
 Author : Kartik Mankad
 Date : 09-July-2012
 This code is licensed as CC-BY-SA 3.0
 Description : This program creates a simple interactive text environment with any
               UDP transceiver on the local area network.
 Usage : PyUDPComm <TargetIP> <TargetPort>
         PyUDPComm 192.168.1.153 1200
               
"""

import sys,socket,select

#declare the messages to show for Usage,Welcome and Exit.
title="UDP Communicator v1 - Written by kmmankad (http://kmmankad.blogspot.com)\n\nThis program is licensed CC-BY-SA 3.0\n\n"
welcomemsg=title+"Press Enter on a blank line,or Ctrl-C to exit.\n\n"
usagemsg=title+"Usage - PyUDPComm <TargetIP> <TargetPort>\nExample - PyUDPComm 192.168.1.153 1200\n"
exitmsg="\nUDP Communicator v1.0 exited.\n"

#If we dont have enough arguments,
if len(sys.argv)!=3:
    #Exit and mention usage.
    sys.exit(usagemsg)    

print welcomemsg #We have enough arguments,lets proceed.

#Set the important targetIP,targetport and myIP variables.
targetIP=sys.argv[1]
targetPort=sys.argv[2]
myIP=str(socket.gethostbyname(socket.getfqdn()))

#Create the socket.
UDPSocket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Setup the listener.
UDPSocket.bind((myIP,int(targetPort)))

#Keep it non blocking,since we will use select() instead for timeout handling.
UDPSocket.setblocking(0)

try:
    while 1:
        payload = raw_input(" => ")
        if len(payload)==0:
            UDPSocket.close() #Exit on blank line entered.
            sys.exit(exitmsg)
        UDPSocket.sendto(str(payload), (targetIP,int(targetPort)) )#Transmit the entered text
        ready = select.select([UDPSocket], [], [],10)#Wait 10seconds for a reply.
        if ready[0]:
            reply = UDPSocket.recv(1024)#Get the reply,and print it.
            print "\t\t <= \" ",reply,"\"\n---------------------------------------\n"
except KeyboardInterrupt:
    sys.exit(exitmsg) #Exit on Ctrl-C

 
