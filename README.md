# Sink Node

The code serves to send two kinds of messages from the client(ATM's) to the server, with the respective responses.
Each request that the server receives gets updated to a database
Each session has a key created and shared to the server, keys are also logged 

## Future Improvements

- [ ] Update time and date on config request from the server response
- [ ] Add database on client side to log responses
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
received health request
session id: 8069e94e697aad6d0925417f3f8cc8eaa115f82d2d24d005
Got connection from TERM002
received health request
session id: 2d75668827bf68a6622b7badc81ed7131e4cc4766885bbbb
```
## Visual Output client.py

```
➜  sink_node git:(master) ✗ python2 client.py health
session key: 8069e94e697aad6d0925417f3f8cc8eaa115f82d2d24d005
recieved health response: "STXH0.BANK001:1CTERM001:1CH0OFT"
```

## Visual Output client2.py

```
➜  sink_node git:(master) ✗ python2 client2.py health                                      
session key: 2d75668827bf68a6622b7badc81ed7131e4cc4766885bbbb
recieved health response: "STXH0.BANK001:1CTERM001:1CH0OFT"
```

## Closing Off
I hope this answers the test question, albeit a rudimentary version 