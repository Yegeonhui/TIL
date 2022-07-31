import PySimpleGUI as sg  
import random
import string

# 데이터 word()는 컬럼헤더, number()는 랜덤 데이터 1000개, make_talbe()함수는 테이블에 들어갈 데이터셋을 만든다.

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def number(max_val = 1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

data = make_table(num_rows = 15, num_cols = 6)
headings = [str(data[0][x]) for x in range(len(data[0]))]

# 테이블
layout = [
          [sg.Table(values = data[1:][:], 
                    headings = headings, 
                    max_col_width = 25, 
                    background_color = 'lightblue',
                    auto_size_columns = True,
                    display_row_numbers= True,
                    justification = 'right',
                    num_rows = 20,
                    alternating_row_color = 'lightyellow',
                    key = '-TABLE-',
                    tooltip = 'This is a table')]
          ]
window = sg.Window('The Table Element', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values = data)
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors = ((8, 'white', 'red'), (9, 'green')))

window.close()