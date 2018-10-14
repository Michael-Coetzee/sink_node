# Sink Node

The code serves to send two kinds of messages from the client(ATM's) to the server, with the respective responses.
Each request that the server receives gets updated to a database
Each session has a key created and shared to the server, keys are also logged 

## Future Improvements

- [x] Update time and date on config request from the server response
- [x] Add database on client side to log responses
- [ ] Improve key management
- [x] introduce threading for multiple clients(ATM's)
- [x] code refactoring

## Requirements

1. I did this on a linux rig, however is should work on all OS's(testing needed) - distro used Arch Linux
2. package installed: python2-mysql-connector(archlinux naming, may need to find your distro equivalent)
3. python 2.6
4. mysql

## Installation Instructions

```
Note:create mysql database and database user
The example code will run through on the localhost
$git clone https://github.com/Michael-Coetzee/sink_node.git
$cd sink_node
Open server.py with your favorite editor
Change the usename, password and database
$python2 server.py
$python2 client.py <config> | <health>
$python2 client2.py <config> | <health>
```

## Visual Output server.py

```
➜  sink_node git:(master) ✗ python2 server.py
Got connection from TERM001
received config request
session id: 94b2acf5e489750a0fed281f7d9d477434e29ca58de2176f
Got connection from TERM001
received config request
session id: 6a72abce49da633b28b0f09a4b6c2658cbd81ce61f2f8b6c
Got connection from TERM001
received health request
session id: 136c8655751b9c71dc99a68ecf7d5578fec432f503c497ad
Got connection from TERM001
received health request
session id: dd28d248db38f52e8ef736e3eba59038ec992a45901ce4b3
```
## Visual Output client.py

```
➜  sink_node git:(master) ✗ python2 client.py config
Current ATM date: 2018-10-15 Current ATM time: 00:29:01
session key: 94b2acf5e489750a0fed281f7d9d477434e29ca58de2176f
recieved config response: "STXH0.BANK001:1CTERM001:1C88:1C2018-10-1500:31:06:1C...:1C---:1C---:1C---:1C---:1C:1C------:1C------OFT"
updading atm configuration
ATM_Date: 2018-10-15 ATM_Time: 00:31:06
➜  sink_node git:(master) ✗ python2 client.py health
session key: dd28d248db38f52e8ef736e3eba59038ec992a45901ce4b3
recieved health response: "STXH0.BANK001:1CTERM001:1CH0OFT"
➜  sink_node git:(master) ✗ 
```

## Visual Output client2.py

```
➜  sink_node git:(master) ✗ python2 client.py config                                        
Current ATM date: 2018-10-15 Current ATM time: 00:31:06
session key: 6a72abce49da633b28b0f09a4b6c2658cbd81ce61f2f8b6c
recieved config response: "STXH0.BANK001:1CTERM001:1C88:1C2018-10-1500:31:13:1C...:1C---:1C---:1C---:1C---:1C:1C------:1C------OFT"
updading atm configuration
ATM_Date: 2018-10-15 ATM_Time: 00:31:13
➜  sink_node git:(master) ✗ python2 client.py health
session key: 136c8655751b9c71dc99a68ecf7d5578fec432f503c497ad
recieved health response: "STXH0.BANK001:1CTERM001:1CH0OFT"
➜  sink_node git:(master) ✗ 
```

## Closing Off
I hope this answers the test question, albeit a rudimentary version< i really enjoyed this project, learned new things  :muscle:  :smile: