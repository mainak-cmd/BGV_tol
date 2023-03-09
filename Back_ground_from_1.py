import PySimpleGUI as sg
import Back_end_logic
import shutil
import os

def Highest_Education():
    layout = [
    [sg.Text('Highest Education', size=(9, 0)),
     sg.Checkbox(' Mark sheets (all Semesters) ', key='Mark sheets'),
     sg.Checkbox('Degree certificate', key='Degree certificate '),
     [sg.Stretch(),sg.Text("Choose  files: "),sg.Input(key='_HE_'),sg.FileBrowse(),sg.Stretch()],
     [sg.Stretch(),sg.Button("Submit"), sg.Button("clear"),sg.Button('Exit'),sg.Stretch()]]]
    Win_HE=sg.Window('Simple data entry form', layout)
    while True:
        event, values = Win_HE.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Height_education')
            path=Back_end_logic.Upload_files('Highest Education')
            try:
                shutil.copy2(str(values['_HE_']),str(path))
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,Win_HE)
    return Win_HE.close()



def Employment_Documents():
    layout = [
    [sg.Text('Employment Documents', size=(9, 0)),
    sg.Text('Exxpirience', size=(15, 1)), sg.Combo(['<5yr', '>5yr'])],

    [sg.Text("Choose  files: "), sg.Input(key='_EMP_'),sg.FileBrowse()],

    [sg.Stretch(),sg.Button("Submit"), sg.Button('Exit'),sg.Button('clear'),sg.Stretch()]]

    window=sg.Window('Simple data entry form', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Submit":
            Back_end_logic.data_frame(values, 'Employment Documents')
            New_path=Back_end_logic.Upload_files('Employment Documents')
            try:
                shutil.copy(str(values['_EMP_']), str(New_path))
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,window)
    return window.close()





def BGV_froms():
    layout = [

    [sg.Stretch(),
     sg.Text("HSBC_ONBOARDING_RESUME: "),
     sg.Input(key='_HOR_'), sg.FileBrowse()],

    [sg.Stretch(),
     sg.Text("New_Cv_summary: "),
     sg.Input(key='_NCm_'), sg.FileBrowse()],

    [sg.Stretch(),
     sg.Text("BGV_From: "),
     sg.Input(key='_BF_'), sg.FileBrowse()],

    [sg.Stretch(),
     sg.Text("COI: "),
     sg.Input(key='_COI_'), sg.FileBrowse()],

    [sg.Stretch(),
     sg.Text("IRF: "),
     sg.Input(key='_IRF_'), sg.FileBrowse()],

    [sg.Stretch(),
     sg.Button("Submit"), sg.Button('Exit')]

     ]

    WINDOW_bgv=sg.Window('Simple data entry form', layout, size=(800, 200), grab_anywhere=True)
    while True:
        event, values = WINDOW_bgv.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        while event == "Submit":
            try:
                path=Back_end_logic.Upload_files('BGV_FROM')
                shutil.copy(str(values['_IRF_']), path)
                shutil.copy(str(values['_COI_']), path)
                shutil.copy(str(values['_BF_']), path)
                shutil.copy(str(values['_NCm_']), path)
                shutil.copy(str(values['_HOR_']), path)
                sg.Cancel()
            except:
                sg.popup("Select any file")
            break
    return WINDOW_bgv.close()

"""def Right_to_work():
    layout = [
    [sg.Text('Right to work', size=(8, 0)),
     sg.Checkbox('Valid Passport', key='Valid Passport'),
     sg.Checkbox('Voters Identity Card', key='Voters Identity Card'),
     sg.Text("Choose a file: "), sg.Input(key='_RTW_'), sg.FileBrowse(),
     sg.Button("Submit"), sg.Button('Exit'), sg.Button('clear')]]
    window_rtw=sg.Window('Simple data entry form', layout)
    while True:
        event, values = window_rtw.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Right_to_work')
            path=Back_end_logic.Upload_files('Right_to_work')
            try:
                shutil.copy(str(values['_RTW_']), path)
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,window_rtw)
    return window_rtw.close()"""

def Additional_doc():
    layout = [
        [sg.Text(' Additional documents', size=(10, 0)),
         sg.Checkbox('Bank Statement', key='Bank Statement'),
         sg.Checkbox('Payslip', key='Payslip'),
         sg.Checkbox('PF Passbook or letter ', key='PF Passbook or letter'),
         sg.Checkbox('Form – 16 Part A ', key='Form – 16 Part A '),
         sg.Checkbox('PF Details', key='PF Details'),
         sg.Text("Choose a file: "), sg.Input(key='_AD_'), sg.FileBrowse(),
         sg.Button("Submit"), sg.Button('Exit'),sg.Button('clear')]]
    Add_docs=sg.Window('Simple data entry form', layout)
    while True:
        event, values = Add_docs.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Additional documents')
            path=Back_end_logic.Upload_files('Additional documents')
            try:
                shutil.copy(str(values['_AD_']), path)
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,Add_docs)
    return Add_docs.close()


def Additional_doc_1():
    layout = [
        [sg.Text(' Additional documents', size=(10, 0)),
         sg.Checkbox('Bank Statement', key='Bank Statement'),
         sg.Checkbox('Payslip', key='Payslip'),
         sg.Checkbox('PF Passbook or letter ', key='PF Passbook or letter'),
         sg.Checkbox('Form – 16 Part A ', key='Form – 16 Part A '),
         sg.Checkbox('PF Details', key='PF Details'),
         sg.Text("Choose a file: "), sg.Input(key='_AD_'), sg.FileBrowse(),sg.Button("Submit")
         sg.Button("Submit"), sg.Button('Exit'),sg.Button('clear')]]
    Add_docs=sg.Window('Simple data entry form', layout)
    while True:
        event, values = Add_docs.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Additional documents')
            path=Back_end_logic.Upload_files('Additional documents')
            try:
                shutil.copy(str(values['_AD_']), path)
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,Add_docs)
    return Add_docs.close()


Additional_doc_1()





def Adress_proof():
    layout = [
    [sg.Stretch(),
    sg.Text('Address Proof', size=(9, 0)),
    sg.Checkbox('Bank Statement', key='Bank Statement'),
    sg.Checkbox('Electricity bill', key='Electricity bill'),
    sg.Checkbox('Telephone bill', key='Telephone bill'),
    sg.Checkbox('Credit Card Statement', key='Credit Card Statement'),
    sg.Stretch()],

    [sg.Stretch(),sg.Checkbox('Valid Passport', key='Valid Passport'),
    sg.Checkbox('Voters Identity Card', key='Voters Identity Card'),sg.Stretch()],

    [sg.Stretch(),sg.Text("Choose a file: "),sg.Input(key='_AP_'), sg.FileBrowse(),sg.Stretch()],

    [sg.Stretch(),sg.Button("Submit"), sg.Button('Exit'),sg.Button('clear'),sg.Stretch()]

    ]

    Add_prf= sg.Window('Simple data entry form', layout,grab_anywhere=True)
    while True:
        event, values = Add_prf.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Address Proof')
            path=Back_end_logic.Upload_files('Address Proof')
            try:
                shutil.copy(str(values['_AP_']),path)
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,Add_prf)
    return Add_prf.close()

def Id_Proof():
    layout = [
    [sg.Text('ID Proof', size=(9, 0)),
     sg.Checkbox(' Pan Card ', key=' Pan Card'),
     sg.Checkbox('CG ID ', key=' CG ID')],

    [sg.Stretch(),sg.Text("Choose a file: "), sg.Input(key='_ID_'), sg.FileBrowse(),sg.Stretch()],
    [sg.Button("Submit"), sg.Button('Exit'),sg.Button('clear'),sg.Stretch()]]
    Id_win= sg.Window('Simple data entry form', layout)
    while True:
        event, values = Id_win.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == 'Submit':
            Back_end_logic.data_frame(values, 'Id_Proof')
            path=Back_end_logic.Upload_files('Id_Proof')
            try:
                shutil.copy(str(values['_ID_']), path)
            except:
                sg.popup("Select any file")
        if event == "clear":
            Back_end_logic.clear_input(values,Id_win)
    return Id_win.close()

