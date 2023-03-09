import PySimpleGUI as sg
import Back_end_logic
import Froms_tab_mod_1
import MYC_BGV_genarator
import os
from pathlib import Path

def Myc_BGv():
    layout = [
        [sg.Text('Please fill out the following fields:')],

        [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],

        [sg.Text('BGV - Project Name', size=(15, 1)), sg.InputText(key='BGV - Project Name')],

        [sg.Text('Personal Email id ', size=(15, 1)), sg.InputText(key='Personal Email id')],

        [sg.Text('CG Employee ID', size=(15, 1)), sg.InputText(key='CG Employee ID')],

        [sg.Text('Candidate ID', size=(15, 1)), sg.InputText(key='CAN ID')],

        [sg.Text('Capgemini Email ID', size=(15, 1)), sg.InputText(key='Employee Capgemini Email ID')],

        [sg.Text('Date of Joining Capgemini', size=(15, 0)), sg.InputText(key='Date of Joining Capgemini')],

        [sg.Text('Work/Joining Location', size=(15, 0)), sg.InputText(key='Work/Joining Location')],

        [sg.Text('Capgemini Entity', size=(15, 1)), sg.Combo(['ACIS', 'FS', 'BSV', 'NILL'], key='Capgemini Entity')],

        [sg.Text('Hire Type', size=(15, 1)), sg.Combo(['Offered', 'Existing'], key='Hire Type')],

        [sg.Button("Submit"), sg.Button('Exit'), sg.Button('clear'),sg.Button('Next')]]

    window_bgv = sg.Window('Spreadsheet', layout)
    while True:
        event, values = window_bgv.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Submit":
            for i in values:
                while True:
                    if not values[i]:
                        sg.popup(f"{i}")
                        break
                    else:
                        Back_end_logic.data_frame(values, 'Myc_Bgv')

                        MYC_BGV_genarator.myc_bgv_doc(str(values['Hire Type']),
                                                      str(values['Name']),
                                                      str(values['CG Employee ID']),
                                                      str(values['CAN ID']),
                                                      str(values['Employee Capgemini Email ID']),
                                                      str(values['Date of Joining Capgemini']),
                                                      str(values['Work/Joining Location']),
                                                      str(values['Capgemini Entity']))
                        break
        if event == "clear":
            Back_end_logic.clear_input(values, window_bgv)
        if event == "Next":
            Froms_tab_mod_1.All_docs_from()
    return window_bgv.close()


Myc_BGv()