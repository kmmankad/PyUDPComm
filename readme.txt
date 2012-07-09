PyUDPComm - A Basic UDP Communicator written in Python 2.7.3
------------------------------------------------------------

This program basically creates an interactive text environment
with a networked device whose IP address and UDP port are specified correctly.

 Usage : PyUDPComm <TargetIP> <TargetPort>
 Example :  PyUDPComm 192.168.1.153 1200

Known bug:If you are connected to the internet via Wifi,and the 
	  network device with which you wish to communicate is 
	  hooked up to your NIC,then this program associates the 
	  UDP connections with the IP address of your Wireless 
	  adapter,and not your NIC. 

Tested with Windows 7 x64 and Python 2.7.3

-kmmankad

http://kmmankad.blogspot.com

This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.