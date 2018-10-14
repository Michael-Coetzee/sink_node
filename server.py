import json
import socket
import cPickle
import datetime
import mysql.connector
from collections import OrderedDict

date = datetime.datetime.date(datetime.datetime.now())
time = datetime.datetime.time(datetime.datetime.now())

mydb = mysql.connector.connect(
    host="localhost",
    user="michael",
    passwd="password",
    db="testdb"
)
mycursor = mydb.cursor()

ct = [
    ('Protocol_Dependent_Header', 'STX'),
    ('Record_Format', 'H'),
    ('Application_Type', '0'),
    ('Message_Delimiter', '.'),
    ('Bank_ID_Number', 'BANK001'),
    ('Field_Separator_1', ':1C'),
    ('Terminal_ID', 'TERM001'),
    ('Field_Separator_2', ':1C'),
    ('Response_Type', '88'),
    ('Field_Separator_3', ':1C'),
    ('Local_Date', str(date)),
    ('Local_Time', str(time)[:8]),
    ('Field_Separator_4', ':1C'),
    ('Health_Message_Timer_Value', '...'),
    ('Field_Separator_5', ':1C'),
    ('TDES_Working_Key_Part_1', '---'),
    ('Field_Separator_6', ':1C'),
    ('Surcharge_Amount', '---'),
    ('Field_Separator_7', ':1C'),
    ('BIN_List_Enable_Flag', '---'),
    ('Field_Separator_8', ':1C'),
    ('TDES_Working_Key_Part_2', '---'),
    ('Field_Separator_9', ':1C'),
    ('TDES_Working_Key_Part_1', '---'),
    ('Field_Separator_10', ':1C'),
    ('AID_Information', '---'),
    ('AID_List', '---'),
    ('Field_Separator_11', ':1C'),
    ('CA_Public_Key_Information', '---'),
    ('CA_Public_Key_List', '---'),
    ('Protocol_Dependent_Trailer', 'OFT'),
]

hcct = [
    ('Protocol_Dependent_Header', 'STX'),
    ('Record_Format', 'H'),
    ('Application_Type', '0'),
    ('Message_Delimiter', '.'),
    ('Bank_ID_Number', 'BANK001'),
    ('Field_Separator_1', ':1C'),
    ('Terminal_ID', 'TERM001'),
    ('Field_Separator_2', ':1C'),
    ('Response Type', 'H0'),
    ('Protocol_Dependent_Trailer', 'OFT')
]

ct = OrderedDict(ct)
hcct = OrderedDict(hcct)

config_response = ''.join(str(x) for x in ct.values())
health_confirm = ''.join(str(x) for x in hcct.values())


def create_store_response(table_name, adict):
    columns = ' varchar(255), '.join(adict.keys()) + ' varchar(255)'
    mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id INT AUTO_INCREMENT PRIMARY KEY, `date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, %s )" % (table_name, columns))
    plachold = ', '.join(['%s'] * len(adict))
    columns = ', '.join(adict.keys())
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table_name, columns, plachold)
    mycursor.execute(sql, adict.values())
    mydb.commit()


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 12345))

    s.listen(5)
    while True:
        c, addr = s.accept()
        print 'Got connection from', addr
        data = c.recv(2048)
        data_loaded = json.loads(data)
        data_session_key = data_loaded.get('session_key', None)
        key = cPickle.loads(str(data_session_key))
        data_clean = data_loaded.get('request', None).split(':1C')
        if data_clean[2] == 'H0':
            print 'received health request'
            print 'session id: %s' % key
            data_string = json.dumps(health_confirm)
            c.send(data_string)
            create_store_response('health_check', data_loaded)
            c.close()
        elif data_clean[2] == '88':
            print 'received config request'
            print 'session id: %s' % key
            data_string = json.dumps(config_response)
            c.send(data_string)
            create_store_response('config_check', data_loaded)
            c.close()
        else:
            print 'nope'
            c.close()

    s.close()



if __name__ == '__main__':
    create_socket()
