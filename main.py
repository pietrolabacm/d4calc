from d4damage import *

def main():
    textBoxSize = 11
    affixList = ['skill','baseDamageMin','baseDamageMax','mainStat','additive',
                'vulnerability', 'criticalChance', 'criticalDamage',
                'overpowerChance','overpowerDamage','legendary']

    inputList = affixList+['graphSize','multiHit']
    equipList = [['Helm','Chest','Gloves','Pants','Boots','Amulet','Ring1',
                'Ring2']]
    helm = Equipment()

    menu_equipment = ['Equipment',equipList]
    menu_file = ['File',['Save','Load']]
    menu_def=[menu_file,menu_equipment]

    layout=[[sg.Menu(menu_def)],
            #[sg.Text('D4 Calculator')],
            [sg.Text('Skill %', size=textBoxSize), 
            sg.InputText(key='skill', enable_events=True, expand_x=True),
            sg.Checkbox('',key='skillCheck',enable_events=True)],
            [sg.Text('B. Dmg Min', size=textBoxSize), 
            sg.InputText(key='baseDamageMin',enable_events=True,expand_x=True), 
            sg.Text('B. Dmg Max', size=textBoxSize), 
            sg.InputText(key='baseDamageMax',enable_events=True, 
                         expand_x=True),
            sg.Checkbox('',key='baseDamageCheck', enable_events=True)],            
            [sg.Text('Main Stat', size=textBoxSize), 
            sg.InputText(key='mainStat', enable_events=True, expand_x=True),
            sg.Checkbox('',key='mainStatCheck', enable_events=True)],
            [sg.Text('Additive', size=textBoxSize), 
            sg.InputText(key='additive', enable_events=True, expand_x=True),
            sg.Checkbox('',key='additiveCheck', enable_events=True)],
            [sg.Text('Vulnerability', size=textBoxSize), 
            sg.InputText(key='vulnerability', enable_events=True,
                         expand_x=True),
            sg.Checkbox('',key='vulnerabilityCheck', enable_events=True)],
            [sg.Text('Crit. Chance',size=textBoxSize), 
            sg.InputText(key='criticalChance', enable_events=True,
                         expand_x=True),
            sg.Checkbox('',key='criticalChanceCheck', enable_events=True), 
            sg.Text('Crit. Damage', size=textBoxSize), 
            sg.InputText(key='criticalDamage',enable_events=True,
                         expand_x=True),
            sg.Checkbox('',key='criticalDamageCheck', enable_events=True)],
            [sg.Text('Ovpw. Chance',size=textBoxSize), 
            sg.InputText(key='overpowerChance', enable_events=True,
                         expand_x=True),
            sg.Checkbox('',key='overpowerChanceCheck', enable_events=True), 
            sg.Text('Ovpw. Damage', size=textBoxSize), 
            sg.InputText(key='overpowerDamage',enable_events=True,
                         expand_x=True),
            sg.Checkbox('',key='overpowerDamageCheck', enable_events=True)],
            [sg.Text('Legendary',size=textBoxSize), 
            sg.InputText(key='legendary', enable_events=True, expand_x=True),
            sg.Checkbox('',key='legendaryCheck', enable_events=True)],
            [sg.Button('Calculate', disabled=True),
            sg.Text('', size = 8,key='calculate', relief='raised', 
                    justification='r'),
            sg.Button('Mean', disabled=True),
            sg.Text('', size = 8,key='mean', relief='raised', 
                    justification='r'),  
            sg.Button('Graph', disabled=True),
            sg.InputText(key='graphSize', enable_events=True, size= 3)],
            [sg.InputText(key='multiHit',enable_events=True,size=3),
            sg.Button('Multi Hit', disabled=True),
            sg.Text('',key='multiHitText',expand_x=True, size=(30,2), 
                    relief='raised',justification='l')]]

    checkBoxList = ['skillCheck','baseDamageCheck','mainStatCheck',
                    'additiveCheck','vulnerabilityCheck',
                    'criticalChanceCheck','criticalDamageCheck',
                    'overpowerChanceCheck','overpowerDamageCheck',
                    'legendaryCheck']

    # Create the Window
    window = sg.Window('D4 Calculator', layout, element_justification='l',
                    default_element_size=(7,200))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break

        for i in inputList:
            if (event == i and values[i] and values[i][-1] 
                    not in ('0123456789+-*/')):
                window[i].update(values[i][:-1])

        minimalAffixInput = (values['skill'] and values['baseDamageMin'] 
                            and ['baseDamageMax'] and values['mainStat'])

        if ((minimalAffixInput
                and values['skillCheck'] or values['baseDamageCheck'] 
                or values['mainStatCheck'] or values['additiveCheck']
                or values['vulnerabilityCheck'] 
                or values['criticalChanceCheck']
                or values['criticalDamageCheck'] 
                or values['legendaryCheck']
                or values['overpowerChanceCheck'] 
                or values['overpowerDamageCheck'])
                and values['graphSize']):
            window['Graph'].update(disabled=False)
        else:
            window['Graph'].update(disabled=True)
        

        if minimalAffixInput:
            window['Calculate'].update(disabled=False)
            window['Mean'].update(disabled=False)
        else:
            window['Calculate'].update(disabled=True)
            window['Mean'].update(disabled=True)

        if minimalAffixInput and values['multiHit']:
            window['Multi Hit'].update(disabled=False)
        else:
            window['Multi Hit'].update(disabled=True)

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
                window.write_event_value('Calculate',0)
                window.write_event_value('Mean',0)

        if event == 'Calculate':
            window['calculate'].update(text_color='white')
            dmg1 = readDamageFromInput(values['skill'], 
                                       values['baseDamageMin'],
                                       values['baseDamageMax'], 
                                       values['mainStat'],
                                       values['additive'], 
                                       values['vulnerability'],
                                       values['criticalChance'],
                                       values['criticalDamage'],
                                       values['overpowerChance'],
                                       values['overpowerDamage'], 
                                       values['legendary'])
            hit, critical, overpower = dmg1.hit()
            if critical:
                window['calculate'].update(text_color='yellow')
            if overpower:
                window['calculate'].update(text_color='blue')
            if critical and overpower:
                window['calculate'].update(text_color='orange')
            window['calculate'].update(f'{int(hit):,}')

        if event == 'Mean':
            dmg1 = readDamageFromInput(values['skill'], 
                                       values['baseDamageMin'],
                                       values['baseDamageMax'], 
                                       values['mainStat'],
                                       values['additive'], 
                                       values['vulnerability'],
                                       values['criticalChance'],
                                       values['criticalDamage'],
                                       values['overpowerChance'],
                                       values['overpowerDamage'], 
                                       values['legendary'])
            hit = dmg1.meanHit()
            window['mean'].update(f'{int(hit):,}')

        if event == 'Graph':
            dmg1 = readDamageFromInput(values['skill'], 
                                       values['baseDamageMin'],
                                       values['baseDamageMax'], 
                                       values['mainStat'],
                                       values['additive'], 
                                       values['vulnerability'],
                                       values['criticalChance'],
                                       values['criticalDamage'],
                                       values['overpowerChance'],
                                       values['overpowerDamage'], 
                                       values['legendary'])
            
            dmg1.graph(int(values['graphSize']), 
                           values['skillCheck'],
                           values['baseDamageCheck'], 
                           values['mainStatCheck'], 
                           values['additiveCheck'],
                           values['vulnerabilityCheck'], 
                           values['criticalChanceCheck'],
                           values['criticalDamageCheck'],
                           values['overpowerChanceCheck'],
                           values['overpowerDamageCheck'], 
                           values['legendaryCheck'])
            
            window['Graph'].update(disabled=False)
        
        if event == 'Multi Hit':
            dmg1 = readDamageFromInput(values['skill'], 
                                       values['baseDamageMin'],
                                       values['baseDamageMax'], 
                                       values['mainStat'],
                                       values['additive'], 
                                       values['vulnerability'],
                                       values['criticalChance'],
                                       values['criticalDamage'],
                                       values['overpowerChance'],
                                       values['overpowerDamage'], 
                                       values['legendary'])
            
            total, meanHit, critical, overpower = dmg1.hitTimes(
                int(values['multiHit']))
            window['multiHitText'].update(
                f'Total: {int(total):,}    Mean: {int(meanHit):,}\n'\
                f'Critical Strikes: {critical}    Overpowers: {overpower}')  

        if event == 'Helm':
            helm = equipmentWindow(helm)

    window.close()

def equipmentWindow(helm):
    affixInputList = list((vars(helm).keys()))
    layout = [[sg.InputCombo(affixInputList,key='affix1'),
                sg.Input(key='affix1Value')],
                [sg.InputCombo(affixInputList,key='affix2'),
                sg.Input(key='affix2Value')],
                [sg.InputCombo(affixInputList,key='affix3'),
                sg.Input(key='affix3Value')],
                [sg.InputCombo(affixInputList,key='affix4'),
                sg.Input(key='affix4Value')],
                [sg.Button('Ok'),sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Equipment', layout, modal=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == 'Ok':
            affix = ['affix1','affix2','affix3','affix4']
            affixVal = ['affix1Value','affix2Value','affix3Value',
                        'affix4Value']
            affixArgs = []

            for a, v in zip(affix, affixVal):
                if bool(values[a]) and bool(values[v]):
                    affixArgs.append((values[a],int(values[v])))
            window.close()
            return Equipment(*affixArgs)
            
        
        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
            
    window.close()

if __name__ == '__main__':
    main()