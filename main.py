from d4damage import *

textBoxSize = 10
affixList = ['skill','baseDamageMin','baseDamageMax','mainStat','additive',
             'vulnerability', 'criticalChance', 'criticalDamage','legendary']

menu_def=[['File',['Save','Load']]]

layout=[[sg.Menu(menu_def)],
        [sg.Text('D4 Calculator')],
        [sg.Text('Skill %', size=textBoxSize), 
         sg.InputText(key='skill', enable_events=True, expand_x=True),
         sg.Checkbox('',key='skillCheck',enable_events=True)],
        [sg.Text('B. Dmg Min', size=textBoxSize), 
         sg.InputText(key='baseDamageMin', enable_events=True, expand_x=True), 
         sg.Text('B. Dmg Max', size=textBoxSize), 
         sg.InputText(key='baseDamageMax',enable_events=True, expand_x=True),
         sg.Checkbox('',key='baseDamageCheck', enable_events=True)],            
        [sg.Text('Main Stat', size=textBoxSize), 
         sg.InputText(key='mainStat', enable_events=True, expand_x=True),
         sg.Checkbox('',key='mainStatCheck', enable_events=True)],
        [sg.Text('Additive', size=textBoxSize), 
         sg.InputText(key='additive', enable_events=True, expand_x=True),
         sg.Checkbox('',key='additiveCheck', enable_events=True)],
        [sg.Text('Vulnerability', size=textBoxSize), 
         sg.InputText(key='vulnerability', enable_events=True,expand_x=True),
         sg.Checkbox('',key='vulnerabilityCheck', enable_events=True)],
        [sg.Text('Crit. Chance',size=textBoxSize), 
         sg.InputText(key='criticalChance', enable_events=True,expand_x=True),
         sg.Checkbox('',key='criticalChanceCheck', enable_events=True), 
         sg.Text('Crit. Damage', size=textBoxSize), 
         sg.InputText(key='criticalDamage',enable_events=True,expand_x=True),
         sg.Checkbox('',key='criticalDamageCheck', enable_events=True)],
        [sg.Text('Legendary',size=textBoxSize), 
         sg.InputText(key='legendary', enable_events=True, expand_x=True),
         sg.Checkbox('',key='legendaryCheck', enable_events=True)],
        [sg.Button('Calculate'),
         sg.Text('', size = 9,key='calculate', relief='raised', 
                 justification='r'), 
         sg.Button('Graph', disabled=True),
         sg.InputText(key='graphSize', enable_events=True, size= 3)]]

# Create the Window
window = sg.Window('D4 Calculator', layout, element_justification='l',
                   default_element_size=(7,200))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    
    for i in affixList:
        if(event == i) and values[i] and values[i][-1] not in ('0123456789'):
            window[i].update(values[i][:-1])

    if ((event == 'graphSize' or event =='skillCheck' 
            or event=='baseDamageCheck' or event =='mainStatCheck'
            or event=='additiveCheck' or event=='vulnerabilityCheck'
            or event=='criticalChanceCheck' or event=='criticalDamageCheck'
            or event=='legendaryCheck') 
            and
            (values['skillCheck'] or values['baseDamageCheck'] 
            or values['mainStatCheck'] or values['additiveCheck']
            or values['vulnerabilityCheck'] or values['criticalChanceCheck']
            or values['criticalDamageCheck'] or values['legendaryCheck'])
            and 
            values['graphSize']):
        window['Graph'].update(disabled=False)
    else:
        window['Graph'].update(disabled=True)

    if event == 'Save':
        path = sg.popup_get_file('Save',no_window=True, save_as=True,
                          file_types=(('JSON','*.json'),))
        if path:
            sg.user_settings_filename(filename=path)
            for i in affixList:
                sg.user_settings_set_entry(i,values[i])

    if event == 'Load':
        path = sg.popup_get_file('Save',no_window=True,
                          file_types=(('JSON','*.json'),))
        if path:
            sg.user_settings_filename(filename=path)
            for i in affixList:
                window[i].update(sg.user_settings_get_entry(i,))

    if event == 'Calculate':
        dmg1 = readDamageFromInput(values['skill'], values['baseDamageMin'],
                                   values['baseDamageMax'], values['mainStat'],
                                   values['additive'], values['vulnerability'],
                                   values['criticalChance'],
                                   values['criticalDamage'], 
                                   values['legendary'])

        window['calculate'].update('%0.0f' % dmg1.hit())

    if event == 'Graph':
        dmg1 = readDamageFromInput(values['skill'], 
                                   values['baseDamageMin'],
                                   values['baseDamageMax'], 
                                   values['mainStat'],
                                   values['additive'], 
                                   values['vulnerability'],
                                   values['criticalChance'],
                                   values['criticalDamage'], 
                                   values['legendary'])
        
        dmg1.graph(int(values['graphSize']), 
                   values['skillCheck'],
                   values['baseDamageCheck'], 
                   values['mainStatCheck'], 
                   values['additiveCheck'],
                   values['vulnerabilityCheck'], 
                   values['criticalChanceCheck'],
                   values['criticalDamageCheck'], 
                   values['legendaryCheck'])
        
        window['Graph'].update(disabled=False)

window.close()