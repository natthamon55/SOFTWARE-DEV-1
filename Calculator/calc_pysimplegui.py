#Student ID : 6201012620139
#Name : Natthamon Bunnithi
#ref1 : https://github.com/israel-dryer/PyDataMath-II
#ref2 : http://myblogmysoftware.blogspot.com/2018/09/pysimplegui-based-basic-calculator.html
#------------------------Calculator with  PySimpleGUI-------------------------------#

import PySimpleGUI as sg 
#-------------------------Interface Calculator-----------------------------------#
# color in hex
White = '#ffffff'
Black = '#000000'
DarkGreen = '#99c5c0'
LightGreen = '#a2eee3'

#set backgroung color
sg.theme('BrightColors') 
# display caption, buttons size and enable to grab anywhere
form = sg.FlexForm('CALCULATOR', default_button_element_size=(8, 4), auto_size_buttons=False, grab_anywhere=True)

#create gui interface with input,button,color,size
layout = [
            [sg.Text('INPUT YOUR MATH :)', size=(23,1), justification='left', text_color='Black', font=('Franklin Gothic Book', 14, 'bold'))],
            [sg.Input(size=(45,10), do_not_clear=True, justification='right', key='input')],
            [sg.ReadFormButton('CE',button_color=(Black,DarkGreen)), sg.ReadFormButton('DEL',button_color=(Black,DarkGreen)),sg.ReadFormButton('(',button_color=(Black,DarkGreen)), sg.ReadFormButton(')',button_color=(Black,DarkGreen))], 
            [sg.ReadFormButton('7',button_color=(Black,LightGreen)), sg.ReadFormButton('8',button_color=(Black,LightGreen)), sg.ReadFormButton('9',button_color=(Black,LightGreen)), sg.ReadFormButton('/',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('4',button_color=(Black,LightGreen)), sg.ReadFormButton('5',button_color=(Black,LightGreen)), sg.ReadFormButton('6',button_color=(Black,LightGreen)), sg.ReadFormButton('*',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('1',button_color=(Black,LightGreen)), sg.ReadFormButton('2',button_color=(Black,LightGreen)), sg.ReadFormButton('3',button_color=(Black,LightGreen)), sg.ReadFormButton('-',button_color=(Black,DarkGreen))],
            [sg.ReadFormButton('0',button_color=(Black,LightGreen)), sg.ReadFormButton('.',button_color=(Black,DarkGreen)), sg.ReadFormButton('=',button_color=(Black,DarkGreen)), sg.ReadFormButton('+',button_color=(Black,DarkGreen))],
        ]

form.Layout(layout)
# for input
keys_entered = '' 

#---------------------------Running Program-----------------------------------#
running = True
while running:
    button, values = form.Read( )
    operator = '+-*/'
    operand  = '1234567890().'

    if button == None:  
        break

    # clear all element 
    if button == 'CE':    
        keys_entered = ''  

    # delete the last number or operator  
    elif button == 'DEL':            
        if keys_entered != '':
            keys_entered = keys_entered[:-1]

    elif button in operand :      
        keys_entered = values['input']  
        keys_entered += button  

    elif button in operator : 
        #if button is  operator = '+-*/'    
        if keys_entered[-1:] == '+' or keys_entered[-1:] == '-' or keys_entered[-1:] == '*' or keys_entered[-1:] == '/':
            keys_entered = keys_entered[:-1]
            keys_entered += button    

        # cannot use + or * or / operator in a first input
        elif keys_entered == '':          
            if button not in '+*/':
                keys_entered = values['input']
                keys_entered += button    
        else:
            keys_entered = values['input']
            keys_entered += button

    # SUM 
    elif button in '=':  
    
        if '/0' in keys_entered:
            keys_entered = 'ERROR by division zero'
        elif ('(' in keys_entered and ')' not in keys_entered) or (')' in keys_entered and '(' not in keys_entered):
            keys_entered = 'ERROR by not completed bracket'
        elif '..' in keys_entered:
            keys_entered = 'ERROR by points'
        else :
            keys_entered = str(eval(keys_entered))
            # delete .0 from number
            if keys_entered[-2:] == '.0':   
                keys_entered = keys_entered[:-2]

    form.FindElement('input').Update(keys_entered)
