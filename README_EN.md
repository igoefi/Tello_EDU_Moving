# Tello EDU Controller for PC
1. Tello

To use this program you need to connect to Wi-Fi of Tello EDU drone

2. SwarmTello


To use the program, you need to connect the Tello EDU drone to the router:

1.Download the ap-tello file
2. Go to the file download directory
3.In the address line write "cmd" (without quotes)
4.Turn on the drone and connect to it
5.In the command line, you need to write "ap-tello.py -s SSID -p PASSWORD" (without quotes), where "SSID" is the name of the router to which you want to connect the Tello EDU drone,
a "PASSWORD" - router password.
6.Connection Ready but not complete


For further actions, you need to go to the Control Panel of the router.


Configuring from the side of the router


1. We go to CP of Router
2. We are looking for DHCP settings (if necessary, turn on DHCP)
4. We are looking for the item "IP Assignment Manually" or "IP Reservation"
5. Next, you need to give each drone an IP from 192.168.0.120 to 192.168.0.125 (you can change 0.120 and 0.125 to any others, but then you will need to change the program code).
6. Done! We reboot the router.


Then you launch the program, the main thing is that the computer and the drones are connected to the same network.
If the drones stop blinking and turn purple or green, then everything is working as it should and they were put into command acceptance mode.

Control:
'w'-forward
'a'-left
's'-back
'd'-right
'p'-lift drone (ov)
'l'-drop drone (ov)
'2'-make a forward flip in the air
'3'-do a flip in the air back
'4'-make a left turn in the air
'5'-make a flip in the air to the right
'0'-quick landing
'1'-fast takeoff

ONLY in Tello:
'z'-check battery power

Swarm Tello ONLY:
'r' - on control of 1 drone
't' - on 2 drone control
'y' - on 3 drone control
'u' - on 4 drone control
'i' - on 5 drone control
'[' - on control of all drones
']' - off. control of all drones

Additional 1. Activation of the drone:
1.If you connected the drone to a router, then reset it
2.Connect the drone to your phone and download Tello app
3.In the application below in the red window there will be a request to activate the serial code of the drone, click
4.Dron activated


Resetting the drone:
1.Turn off the drone.
2.When turning on, hold down the power button of the aircraft. (~ 10 sec.)


Known bugs


Q: What should I do if I need to connect to the drone as usual?
A: Drop it. There are no other solutions. Then you have to reconnect to the router


P: Drones don't take off.
A: Check the drones' battery power and whether they are overheated or connected.
S: Charge the battery or keep the drone cool


P: Some drones do not follow the command
A: Perhaps this is due to the distance between the router and the drone
S: Move the router closer to the drone


Q: Drones "think" for a long time
A: This is due to the fact that drones themselves take a long time to process commands.


P: Drones blinked red
A: The drone is not activated
S: Activate the drone. Instructions above

R: The drone is connected, but the program does not work (For Swarm Tello)
A: There are two possible problems
 1.Perhaps the drones or computer are not connected to the router.
 2. Local IP in router settings and code are confused
S: Reread the instructions!


P: Unknown error, the drone does not fly well, etc.
S: Reset the drone and use the app on your phone to check it and update it (if it's not up to date).
