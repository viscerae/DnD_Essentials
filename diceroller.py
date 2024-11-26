import FreeSimpleGUI as sg

sg.theme('dark')
layout = [
    [sg.Text("Hi", justification="center", size=40, font=("Helvetica", 12, "bold"), text_color="#8c03fc")]
    [sg.Button('d4'), sg.Button('d6'), sg.Button('d8')]
    [sg.Button('d10'), sg.Button('d12'), sg.Button('d20')]
]
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()