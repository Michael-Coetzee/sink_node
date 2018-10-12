config_response = 'STXH0.BANK001:1CTERM001:1C------:1C...:1C---:1C---:1C---:1C---:1C---:1C------:1C------OFT'
health_confirm = 'STXH0.BANK001:1CTERM001:1CH0OFT'

config_response_dict = {
    'Protocol_Dependent_Header': 'VAR',
    'Record_Format': 'H',
    'Application_Type': '0',
    'Message_Delimiter': '.',
    'Bank_ID_Number': '---',
    'Terminal_ID': '---',
    'Response_Type': '88',
    'Local_Date': '---',
    'Local_Time': '---',
    'Health_Message_Timer_Value': '...',
    'TDES_Working_Key_Part_1': '---',
    'Surcharge_Amount': '---',
    'BIN_List_Enable_Flag': '---',
    'TDES_Working_Key_Part_2': '---',
    'TDES_Working_Key_Part_1': '---',
    'AID_Information': '---',
    'AID_List': '---',
    'CA_Public_Key_Information': '---',
    'CA_Public_Key_List': '---',
    'Protocol_Dependent_Trailer': 'VAR',
}

health_check_confirm_dict = {
    'Protocol_Dependent_Header': 'STX',
    'Record_Format': 'H',
    'Application_Type': '0',
    'Message_Delimiter': '.',
    'Bank_ID_Number': 'BANK001',
    'Terminal_ID': 'TERM001',
    'Response Type': 'H0',
    'Protocol_Dependent_Trailer': 'OFT'
}