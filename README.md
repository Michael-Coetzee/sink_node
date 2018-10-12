# Sink Node

The code serves to send two kinds of messages from the client(ATM's) to the server, with the respective responses.
Each request that the server receives gets updated to the database
Each session has a key created and shared to the server, keys are also logged 

## Future Improvements

1. Update time and date on config request from the server response
2. Add database on client side to log responses
3. Improve key management
4. introduce threading for multiple clients(ATM's)

## Requirements
1. I did this on a linux rig, however is should work on all OS's(testing needed) - distro used Arch Linux
2. package installed: python2-mysql-connector(archlinux naming, may need to find your distro equivalent)
3. python 2.6 or >
4. mysql

## Installation Instructions

```
note:create mysql databses and user, we will also do this through the loopback(localhost)
$git clone https://github.com/Michael-Coetzee/sink_node.git
$cd sink_node
change the database usename, password and database with your favorite editor
python2 server.py
python2 client.py <config> | <health>
```

## Visual Output server.py

```
➜  sink_node git:(master) ✗ python2 server.py
Got connection from ('127.0.0.1', 48120)
received health request
session id: cb18d7f0b5419945ef7905b574fb90c71f243c4f4a63ad5b
```
## Visual Output client.py

```
➜  sink_node git:(master) ✗ python2 client.py health
session id: S'cb18d7f0b5419945ef7905b574fb90c71f243c4f4a63ad5b'
.
reply recieved from server ['STXH0.BANK001', 'TERM001', 'H0OFT']
```
## Closing Off
I hope this answers the test question, albiet a very rudimentary version 