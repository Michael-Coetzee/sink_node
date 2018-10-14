import os
import sys
import json
import socket
import cPickle
import mysql.connector
from collections import OrderedDict

mydb = mysql.connector.connect(
    host="localhost",
    user="michael",
    passwd="password",
    db="testdb"
)
client = mydb.cursor()

def prepare_session(dict_n, config):
    generate_session_key = cPickle.dumps(os.urandom(24).encode('hex'))
    dict_n['session_key'] = generate_session_key
    key = cPickle.loads(str(generate_session_key))
    print 'session key:', key
    dict_n['request'] = config
    global data_string
    data_string = json.dumps(dict(dict_n))


def store_date_and_time(date, time):
    client.execute("CREATE TABLE IF NOT EXISTS TERM001 (id INT AUTO_INCREMENT PRIMARY KEY, atmdate varchar(255), atmtime varchar(255))")
    sql = "INSERT INTO TERM001 (atmdate, atmtime) VALUES ('%s', '%s')" % (date, time)
    client.execute(sql)
    mydb.commit()


def create_socket(data_string):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 5000))
    s.sendall(data_string)
    data = s.recv(2048)
    data_loaded = json.loads(data).split(':1C')
    if data_loaded[2][:2] == 'H0':
        print 'recieved health response: %s' % data
    elif data_loaded[2] == '88':
        store_date_and_time(data_loaded[3][:10], data_loaded[3][10:])
        print 'recieved config response: %s' % data
        print 'updading atm configuration'
        print 'ATM_Date:', data_loaded[3][:10], 'ATM_Time:', data_loaded[3][10:]
    else:
        print 'something went wrong'
    s.close()


def main(args):
    crt = [
        ('Protocol_Dependent_Header', 'STX'),
        ('Record_Format', 'H'),
        ('Application_Type', '0'),
        ('Message_Delimiter', '.'),
        ('Bank_ID_Number', 'BANK001'),
        ('Field_Separator_1', ':1C'),
        ('Terminal_ID', 'TERM001'),
        ('Field_Separator_2', ':1C'),
        ('Request_Type', '88'),
        ('Field_Separator_3', ':1C'),
        ('Unknown_Value_Field', '3'),
        ('Protocol_Dependent_Trailer', 'OFT')
    ]


    hcrt = [
        ('Protocol_Dependent_Header', 'STX'),
        ('Record_Format', 'H'),
        ('Application_Type', '0'),
        ('Message_Delimiter', '.'),
        ('Bank_ID_Number', 'BANK001'),
        ('Field_Separator_1', ':1C'),
        ('Terminal_ID', 'TERM001'),
        ('Field_Separator_2', ':1C'),
        ('Response_Type', 'H0'),
        ('Field_Separator_3', ':1C'),
        ('ATM_Date', '---'),
        ('ATM_Time', '---'),
        ('Field_Separator_4', ':1C'),
        ('Bill_Count_1', '---'),
        ('Field_Separator_5', ':1C'),
        ('Bill_Count_2', '---'),
        ('Field_Separator_6', ':1C'),
        ('Bill_Count_3', '---'),
        ('Field_Separator_7', ':1C'),
        ('Bill_Count_4', '---'),
        ('Field_Separator_8', ':1C'),
        ('Mode_Type', '---'),
        ('Field_Separator_9', ':1C'),
        ('Error_Code', '---'),
        ('Field_Separator_10', ':1C'),
        ('New_Journal_Count', '---'),
        ('Protocol_Dependent_Trailer', 'OFT')
    ]

    crt = OrderedDict(crt)
    hcrt = OrderedDict(hcrt)
    date = '---'
    time = '---'
    config_request = ''.join(str(x) for x in crt.values())
    health_check = ''.join(str(x) for x in hcrt.values())
    if len(args) == 1:
        if sys.argv[1] == 'health':
            prepare_session(hcrt, health_check)
            create_socket(data_string)
        elif sys.argv[1] == 'config':
            client.execute('SELECT * FROM TERM001 ORDER BY id DESC LIMIT 1')
            records = client.fetchall()
            print 'Current ATM date:', records[0][1], 'Current ATM time:', records[0][2]
            prepare_session(crt, config_request)
            create_socket(data_string)
        else:
            print 'Usage: python %s <config> | <health>' % sys.argv[0]
    else:
        print 'Usage: python %s <config> | <health>' % sys.argv[0]


if __name__ == '__main__':
    main(sys.argv[1:])