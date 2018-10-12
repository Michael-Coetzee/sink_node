import sys
import json
import socket

config_request = 'STXH0.BANK001:1CTERM001:1C88:1C3OFT'
health_check  =  'STXH0.BANK001:1CTERM001:1CH0:1C------:1C---:1C---:1C---:1C---:1C---:1C...:1C---OFT'

config_request_dict = {
    'Protocol_Dependent_Header': 'STX',
    'Record_Format': 'H',
    'Application_Type': '0',
    'Message_Delimiter': '.',
    'Bank_ID_Number': 'BANK001',
    'Terminal_ID': 'TERM001',
    'Request_Type': '88',
    'Unknown_Value_Field': '3',
    'Protocol_Dependent_Trailer': 'OFT'
}


health_check_request = {
    'Protocol_Dependent_Header': 'STX',
    'Record_Format': 'H',
    'Application_Type': '0',
    'Message_Delimiter': '.',
    'Bank_ID_Number': 'BANK001',
    'Terminal_ID': 'TERM001',
    'Response_Type': 'H0',
    'ATM_Date': '---',
    'ATM_Time': '---',
    'Bill_Count_1': '---',
    'Bill_Count_2': '---',
    'Bill_Count_3': '---',
    'Bill_Count_4': '---',
    'Mode_Type': '---',
    'Error_Code': 'VAR',
    'New_Journal_Count': 'VAR',
    'Protocol_Dependent_Trailer': 'OFT'
}

def prepare_dict(dict_n, config):
    dict_n['request'] = config
    global data_string
    data_string = json.dumps(dict_n)


def create_socket(data_string):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect(('localhost', 12345))
    s.sendall(data_string)
    data = s.recv(1024).split(':1C')
    print 'reply recieved from server %s' % data
    s.close()

def main(args):
    if len(args) == 1:
        if sys.argv[1] == 'health':
            prepare_dict(health_check_request, health_check)
            create_socket(data_string)
        elif sys.argv[1] == 'config':
            prepare_dict(config_request_dict, config_request)
            create_socket(data_string)
        else:
            print 'Usage: python %s <config> | <health>' % sys.argv[0]
    else:
        print 'Usage: python %s <config> | <health>' % sys.argv[0]


if __name__ == '__main__':
    main(sys.argv[1:])