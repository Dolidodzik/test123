import PySimpleGUI as sg
from pythonping import ping

output = None
cli_command_equivalent = None

# preparing layout/GUI
sg.theme('GreenTan')
layout = [
    [sg.Text('Enter parameters for ping:')],
    [sg.Text('Destination (ip)', size =(15, 1)), sg.InputText(default_text="127.0.0.1")],
    [sg.Text('Count', size =(15, 1)), sg.InputText(default_text="4")],
    [sg.Text('Timeout', size =(15, 1)), sg.InputText(default_text="10")],
    [sg.Text('Size of payload', size =(15, 1)), sg.InputText(default_text="56")],
    [sg.Submit(), sg.Cancel()],
]


window = sg.Window('Ping GUI', layout)

# getting values
event, values = window.read()
window.close()


# Producing output
if values[0] and values[1] and values[2] and values[3]:
    cli_command = "ping " + values[0] + " -n " + values[1] + " -w " + values[2] + " -l " + values[3]
    print("Command to reproduce output ===> "+cli_command)
    output = ping(values[0], count=int(values[1]), timeout=int(values[2]), size=int(values[3]))
    print(output)
else:
    print("provide valid input in order to run ping command")
