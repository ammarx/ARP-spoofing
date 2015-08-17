# ARP-spoofing 

> Python script to perform ARP spoofing on a network

This python script allows you to perform ARP spoofing, which can be used to perform attacks such as denial of service, man in the middle, or session hijacking.

# Requirements

For this attack to be performed, you need the following tools to be installed on the machine you will be performing this attacking from:
```
* Python 2.7.6
* Scapy 2.2.0
* Nmap 6.40
* Wireshark
* This python script
```

# Requirement details

Python comes installed on ubuntu by default. 

You can get Scapy from the Ubuntu Software Center:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/1.png)

You can also get Nmap from the Ubuntu Software Center:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/2.png)

Wireshark is also available on the Ubuntu Software Center, however I recommend getting the latest version from the website:
```
https://www.wireshark.org/download.html
```

# Installation

You can download this python script by running the following command in the terminal:
```
$ wget https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/src/mmattack.py
```

# Setting up IP Forwarding

We will be using this script to perform man in the middle attack. Which means we will use this to get the data from another device connected to the same network.

The first step you have to do it turn on the ip forwarding. This step is required so that the connection on the victim's device does not get interrupted. 

To turn on IP forwarding, open terminal and type:
```
$ sudo nano '/proc/sys/net/ipv4/ip_forward'
```

This will open up the ip_forward file. The default value in it should be `0`, change it to `1` and then save and exit.
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/3.png)

Now that we have that sorted, we need to get the MAC address and the IP address of the victim we want to attack on our network. To do that, you first need to see what IP address the router has given you. On Ubuntu you can get that info by going to the Connection Information menu:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/4.png)

# Gathering MAC and IP addresses

According to this we are connected on IP Address: `192.168.20.230` and the Route IP is: `192.168.20.1`
Now here is where a things get a bit tricky because you need a bit of technical knowledge of how IPs work. I wont be going into full details, however I will explain the part that is required for this script to work.

In the above image, you also can see that our Subnet Mask is: `255.255.255.0` 
The `0` in the above simply means that that block `1-254` is available to the client, while the rest of the blocks are available to the host.

Now keep that in mind and look at this image below:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/subnetting_c.png)

As you can see the Mask length for the `255.255.255.0` is `24`, you can calculate this yourself by converting the Subnet Mask into binary and then counting all the ones. Example: `255.255.255.0` into binary: `1111 1111 . 1111 1111 . 1111 1111 . 0000 0000` So the number of ones are `24`. Now you might be wondering why we need this number? Well this is required for the next step, which is to get the MAC addresses and the IP addresses of everyone connected to your network.

Open up the terminal and type:

```
$ sudo nmap -sP {Route IP with ending octate as zero}/{this magical number you got in the previous step}
```

Here is mine:
```
$ sudo nmap -sP 192.168.20.0/24
```

You should see something like this after it is done scanning your network:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/5.png)

# Performing the attack

Now that you have gotten the IP address and the MAC address of the victim, all you need to do is launch the actual attack. To do that fire up the script you downloaded.
```
$ sudo python '/home/ammar/Desktop/mmattack.py'
```

Now all you need to do is enter the details it asks. Here is an example of what it should look like:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/6.png)

If everything goes well, you should be able to start sending packets.
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/7.png)

Now while this ARP request is being spammed, we need to open wireshark
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/8.png)

Select the proper interface you are connected to. If you are not sure, select the `any` option and click start.

You should see a screen like this now:
![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/9.png)

With the `ARP` protocol requests getting spammed. If you don't see this, you have done something wrong. 

Now to see what the victim is browsing, you can type the following in the filter:
```
ip.addr=={ipaddress_of_the_victim} and http.request
```

> Note: This filter allows you to see the http traffic only. If you want to look at other traffic, I recommend you learn how to use wireshark as this will help you to snoop around more easily. Because the IP address of the victim is `192.168.20.240` for me, I will type the following in the filter:
```
ip.addr==192.168.20.240 and http.request
```

and press enter.

![](https://raw.githubusercontent.com/ammarx/ARP-spoofing/master/res/10.png)

As you see from the image above, the victim is on an android device and is browsing the website `www.tagcraftmc.com`

This sort of attack should work on any network that uses ARP request to get the device details.

# Credits

This script is made by `www.arppoisoning.com` 
However, I have made this script easier to use.