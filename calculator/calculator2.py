#Student ID : 6201012620139
#Name : Natthamon Bunnithi
#ref1 : https://github.com/israel-dryer/PyDataMath-II
#ref2 : http://myblogmysoftware.blogspot.com/2018/09/pysimplegui-based-basic-calculator.html
#-------------------- Calculator with  PySimpleGUI and update time ------------------------#

import PySimpleGUI as sg 
from datetime import datetime
#-------------------------Interface Calculator-----------------------------------#
# color in hex
bt = {'size':(7,2), 'font':('Franklin Gothic Book', 18), 'button_color':("black",'#a2eee3')}
bw = {'size':(7,2), 'font':('Franklin Gothic Book', 18), 'button_color':("black",'#99c5c0')}
bw2 = {'size':(8,2), 'font':('Franklin Gothic Book', 14), 'button_color':("black",'#f2f22e')}
Black = '#000000'
Blue = '#05426c'

#set backgroung color
sg.theme('BrightColors') 

#create gui interface with input,button,color,size

layout = [
            [sg.Text('INPUT YOUR MATH :)', size=(23,1), justification='left', text_color='Black', font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Input(size=(55,1), do_not_clear=True, justification='right', key = 'input')],
            [sg.Text('Ans : ', size=(15, 1), font=('Segoe UI', 14), text_color='Blue')],[sg.Text('', size=(15, 1), font=('Segoe UI', 18), text_color='Black', key='out')],
            [sg.Button('CE',**bw), sg.Button('DEL',**bw),sg.Button('(',**bw),sg.Button(')',**bw)], 
            [sg.Button('7',**bt), sg.Button('8',**bt), sg.Button('9',**bt), sg.Button('/',**bw)],
            [sg.Button('4',**bt), sg.Button('5',**bt), sg.Button('6',**bt), sg.Button('*',**bw)],
            [sg.Button('1',**bt), sg.Button('2',**bt), sg.Button('3',**bt), sg.Button('-',**bw)],
            [sg.Button('.',**bw), sg.Button('0',**bt), sg.Button('SUBMIT',**bw), sg.Button('+',**bw)],
            [sg.Button('DateTime',**bw2), sg.Text('Time : ', size=(8,2), font=('Segoe UI', 18),text_color='Blue'), sg.Text('', size=(10, 1), font=('Segoe UI', 18), text_color='Black', key='time')]
        
        ]

# display caption, buttons size 
window = sg.Window('CALCULATOR', layout ,auto_size_buttons=False)
# for input
keys_input = '' 

#---------------------------Running Program-----------------------------------#
running = True
while running:
    button, values = window.Read() # read the form 
    try:
        if button == 'SUBMIT':  
            keys_input = values['input']  
            sum = eval(keys_input)  #calculate value of input
            window['out'].Update(sum)  

    except ZeroDivisionError:  # if /0 will error
        window['out'].Update('Error') 

    except SyntaxError:  #if syntax error
        window['out'].Update('Error')  

    if button == None: # if the X button clicked, just exit  
        break  

    if button == 'CE': # clear all element 
        keys_input = ''  

    elif button == 'DEL':  # delete the last number or operator 
        keys_input = values['input']  
        keys_input = keys_input[:-1]  

    elif button in '()1234567890./*-+' :  # if is operator or operand
        keys_input = values['input']   
        keys_input += button 
    
    elif button == 'DateTime' :
        now = datetime.now().time() # time object
        window['time'].Update(now)

    # change the form to reflect current key string 
    window['input'].Update(keys_input)
