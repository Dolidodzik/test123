# Drawing square function chart


# Instalation

1. Clone this repository
2. Activate your venv
3. Move into repository
4. Install dependencies - `pip3 install -r requirements.txt`
5. Run the code - `python3 main.py`

### How to use / manual
Run `python3 main.py`, if you completed instalation. Program is bassicaly self explanatory - you need to input parameters for command. Here are explanation of parameters:

1. Destination: Is IPv4 address or domain you want to ping - for example "google.com" or "192.168.100.1"
2. Count specify allows you to define how many ICMP packets to send
3. Timeout is the number of seconds you wish to wait for a response, before assuming the target is unreachable
4. is an integer that allows you to specify the size of the ICMP payload you desire - by default is 56, which will result in 64bytes request - after considering ICMP header which size is 8 bytes.

### Docs

Libraries used can be viewed at requirements.txt file.

```
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
```

Is used to create GUI with form.



```
event, values = window.read()
window.close()
```


Next few lines close GUI, and get data from form

```
if values[0] and values[1] and values[2] and values[3]:
    cli_command = "ping " + values[0] + " -n " + values[1] + " -w " + values[2] + " -l " + values[3]
    print("Command to reproduce output ===> "+cli_command)
    output = ping(values[0], count=int(values[1]), timeout=int(values[2]), size=int(values[3]))
    print(output)
else:
    print("provide valid input in order to run ping command")
```

Final part of code produces output - based on data from form. It shows result of ping command, and also throws out CLI command that can be used in windows command prompt.


#### Pseudocode:

1. Initializing GUI, containing form.
2. When user clicks "Submit" button code moves forward (with values given in the form)
3. When user clicks "Cancel" button program stops.
4. Program checks if given data is valid
5. If it isn't, it throws an error
6. If it's valid, program proceeds
7. Program creates cli_command (by concatenating strings of values) and outputs it
8. Programs outputs result of ping command. 
