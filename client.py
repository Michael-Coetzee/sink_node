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
    'ATM Date': '---',
    'ATM Time': '---',
    'Bill Count 1': '---',
    'Bill Count 2': '---',
    'Bill Count 3': '---',
    'Bill Count 4': '---',
    'Mode Type': '---' ,
    'Error Code': 'VAR',
    'New Journal Count': 'VAR',
    'Protocol Dependent Trailer': 'OFT'
}