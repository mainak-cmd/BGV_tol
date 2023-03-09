import PySimpleGUI as sg
import Back_ground_from

def All_docs_from():
    layout = [
        [sg.Text('Upload all documents')
         ],

        [[sg.Stretch(), sg.Button('Employment_Documents'),sg.Checkbox('Employment_Documents ', key='Employment_Documents'),sg.Stretch()],

        [sg.Stretch(),sg.Button('BGV_froms'),sg.Checkbox('BGV_froms', key='BGV_froms'),sg.Stretch()],

        [sg.Stretch(),sg.Button('Adress_proof'),sg.Checkbox('Adress_proof', key='Adress_proof'),sg.Stretch()],

         [sg.Stretch(),sg.Button('Id_Proof'),sg.Checkbox('Id_Proof', key='Id_Proof'),sg.Stretch()],

        [sg.Stretch(), sg.Button('Additional_doc'),sg.Checkbox('Additional_doc', key='Additional_doc'),sg.Stretch()],

        [sg.Stretch(),sg.Button('Highest_Education'),sg.Checkbox('Highest_Education', key='Highest_Education'),sg.Stretch()],

        [sg.Stretch(), sg.Button("Submit"), sg.Button('Exit'), sg.Stretch()]]
        ]
    window_bgv = sg.Window('Spreadsheet', layout)

    while True:
        event, values = window_bgv.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if values['Id_Proof3'] == True and event == "Id_Proof":
            Back_ground_from.Id_Proof()
        if values['Employment_Documents0'] == True and event == "Employment_Documents":
            Back_ground_from.Employment_Documents()
        if values['BGV_froms1'] == True and event == "BGV_froms":
            Back_ground_from.BGV_froms()
        if values['Adress_proof2'] == True and event == "Adress_proof":
            Back_ground_from.Adress_proof()
        if values['Additional_doc4'] == True and event == "Additional_doc":
            Back_ground_from.Additional_doc()
        if values['Highest_Education5'] == True and event == "Highest_Education":
            Back_ground_from.Highest_Education()
        if event == "Submit":
            for i in values:
                while True:
                    if not values[i]:
                        sg.popup(f"{i}")
                        break
                    else:
                        if values[i]:
                            sg.Popup(" Uplodeing done for"  +  f"{i}" )
                    break
    return window_bgv.close()


All_docs_from()