import PySimpleGUI as sg

sg.theme("LightBlue")

layout =[
         [sg.Text("Enter start value", font = "Lucida"), sg.Input(key = 'stVal', size = (3,1)), sg.Text("Enter end value", font = "Lucida"), sg.Input(key = 'enVal', size = (3,1))],
         [sg.Slider(orientation = 'horizontal', key = 'stSlider', range = (1, 100)), sg.Slider(orientation = 'horizontal', key = 'endSlider', range = (1, 100))],
         [sg.ProgressBar(50, orientation = 'h', size = (20, 20), border_width = 4, key = 'progbar', bar_color = ['Red', 'Green'])],
         [sg.Spin(values = ['January', 'February', 'March     ', 'April     ', 'May      ', 'June     '], key = 'spnMnt')],
         [sg.Submit(key = 'btnSubmit'), sg.Cancel()]        
]

window = sg.Window("Progress Bar and Slider Functioning", layout)
while True:
    event, values = window.read()
    print(event, values)

    window['stVal'].update(int(values['stSlider']))
    window['enVal'].update(int(values['endSlider']))

    i = int(values['stVal'])
    k = int(values['enVal'])
    window['btnSubmit'].set_focus()
    print(window['btnSubmit'])
    val = 0

    for i in range(k):
        event, values = window.read(timeout = 100)
        val = val + 100 / (k - i)
        window['progbar'].update_bar(val)

    if event in (None,'Exit'):
        break
window.close()