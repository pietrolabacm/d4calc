from d4damage import *

def main():
    textBoxSize = 11
    affixList = ['skill','baseDamageMin','baseDamageMax','mainAttribute',
                 'additive','vulnerability', 'criticalChance', 
                 'criticalDamage','overpowerChance','overpowerDamage',
                 'legendary']

    inputList = affixList+['graphSize','multiHit']

    helm = Equipment('helm')
    chest = Equipment('chest')
    gloves = Equipment('gloves')
    pants = Equipment('pants')
    boots = Equipment('boots')
    amulet = Equipment('amulet')
    ring1 = Equipment('ring1')
    ring2 = Equipment('ring2')
    equipDict = {'Helm': helm,'Chest': chest, 'Gloves': gloves,'Pants': pants,
                 'Boots': boots,'Amulet': amulet,'Ring1': ring1,'Ring2':ring2}

    path=''
    
    def dmgInputList():
        dmgInput = [values['skill'], 
                values['baseDamageMin'],
                values['baseDamageMax'], 
                values['mainAttribute'],
                values['additive'], 
                values['vulnerability'],
                values['criticalChance'],
                values['criticalDamage'],
                values['overpowerChance'],
                values['overpowerDamage'], 
                values['legendary']]
        return dmgInput

    def mainWindowSave():
        dmg1 = readDamageFromInput(*dmgInputList())
        for i in affixList:
            sg.user_settings_set_entry(i,dmg1.getAffix(i))
        return path

    def mainWindowLoad():
        for i in affixList:
            window[i].update(sg.user_settings_get_entry(i,))
        return path

    menu_equipment = ['Equipment',[list(equipDict.keys())]]
    menu_file = ['File',['Save','Load']]
    menu_compare = ['Compare',['Compare']]
    menu_def=[menu_file,menu_equipment,menu_compare]

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
            sg.InputText(key='mainAttribute', enable_events=True, 
                         expand_x=True),
            sg.Checkbox('',key='mainAttributeCheck', enable_events=True)],
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

    checkBoxList = ['skillCheck','baseDamageCheck','mainAttributeCheck',
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
                            and ['baseDamageMax'] and values['mainAttribute'])

        if ((minimalAffixInput
                and values['skillCheck'] or values['baseDamageCheck'] 
                or values['mainAttributeCheck'] or values['additiveCheck']
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
                mainWindowSave()

        if event == 'Load':
            path = sg.popup_get_file('Load',no_window=True,
                            file_types=(('JSON','*.json'),))
            if path:
                sg.user_settings_filename(filename=path)
                mainWindowLoad()
                window.write_event_value('Calculate',0)
                window.write_event_value('Mean',0)


        for e in list(equipDict.keys()):
            if event == e:
                if path:
                    dmg1 = readDamageFromInput(*dmgInputList())
                    dmg1.remove(equipDict[e])
                    equipDict[e] = equipmentWindow(equipDict[e], path)
                    dmg1.equip(equipDict[e])
                    for i in affixList:
                        sg.user_settings_set_entry(i,dmg1.getAffix(i))
                    mainWindowLoad()
                else:
                    selectChar()
                    window.write_event_value('Load',0)


        if event == 'Calculate':
            window['calculate'].update(text_color='white')
            dmg1 = readDamageFromInput(*dmgInputList())
            hit, critical, overpower = dmg1.hit()
            if critical:
                window['calculate'].update(text_color='yellow')
            if overpower:
                window['calculate'].update(text_color='blue')
            if critical and overpower:
                window['calculate'].update(text_color='orange')
            window['calculate'].update(f'{int(hit):,}')

        if event == 'Mean':
            dmg1 = readDamageFromInput(*dmgInputList())
            hit = dmg1.meanHit()
            window['mean'].update(f'{int(hit):,}')

        if event == 'Graph':
            dmg1 = readDamageFromInput(*dmgInputList())
            
            dmg1.graph(int(values['graphSize']), 
                           values['skillCheck'],
                           values['baseDamageCheck'], 
                           values['mainAttributeCheck'], 
                           values['additiveCheck'],
                           values['vulnerabilityCheck'], 
                           values['criticalChanceCheck'],
                           values['criticalDamageCheck'],
                           values['overpowerChanceCheck'],
                           values['overpowerDamageCheck'], 
                           values['legendaryCheck'])
            
            window['Graph'].update(disabled=False)
        
        if event == 'Multi Hit':
            dmg1 = readDamageFromInput(*dmgInputList())
            
            total, meanHit, critical, overpower = dmg1.hitTimes(
                int(values['multiHit']))
            window['multiHitText'].update(
                f'Total: {int(total):,}    Mean: {int(meanHit):,}\n'\
                f'Critical Strikes: {critical}    Overpowers: {overpower}') 

        if event == 'Compare':
            compareWindow(dmg1) 


    window.close()

def selectChar():
    layout = [[sg.Text('Load your character or save a new one')],
              [sg.Button('Load'),sg.Button('Save')]]
    window = sg.Window('Select Character', layout, modal=True,
                       element_justification='c')

    while True:
        event, values = window.read()

        if event == 'Load':
            window.close()
            return
            
        if event == 'Save':
            path = sg.popup_get_file('Save',no_window=True, save_as=True,
                            file_types=(('JSON','*.json'),))
            if path:
                window.close()
                return path
        
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break

    window.close()

def equipmentWindow(equipment, path):

    affix = ['affix1','affix2','affix3','affix4']
    affixVal = ['affix1Value','affix2Value','affix3Value','affix4Value']
    affixInputList = list((vars(equipment).keys()))
    affixInputList[0]=''

    layout = [[sg.Combo(affixInputList,key='affix1',readonly=True),
               sg.Input(key='affix1Value')],
               [sg.Combo(affixInputList,key='affix2',readonly=True),
               sg.Input(key='affix2Value')],
               [sg.Combo(affixInputList,key='affix3',readonly=True),
               sg.Input(key='affix3Value')],
               [sg.Combo(affixInputList,key='affix4',readonly=True),
               sg.Input(key='affix4Value')],
               [sg.Button('Ok'),sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Equipment', layout, modal=True, finalize=True)

    sg.user_settings_filename(filename=path)
    for a, v in zip(affix, affixVal):
        #try:
        window[a].update(
            sg.user_settings_get_entry(equipment.name+a,))
        window[v].update(
            sg.user_settings_get_entry(equipment.name+v,))
        #except:
         #   continue

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == 'Ok':
            sg.user_settings_filename(filename=path)
            affixArgs = []

            for a, v in zip(affix, affixVal):
                if bool(values[a]) and bool(values[v]):
                    affixArgs.append((values[a],values[v]))
                sg.user_settings_set_entry(
                    equipment.name+a,values[a])
                sg.user_settings_set_entry(
                    equipment.name+v,values[v])
                    
            window.close()
            return Equipment(equipment.name,*affixArgs)
                    
        
        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return equipment
        
def compareWindow(damage):

    dummyEquip = Equipment('dummy')
    item1Affix = ['affix1','affix2','affix3','affix4']
    item1affixVal = ['affix1Value','affix2Value','affix3Value','affix4Value']

    item2Affix = ['2affix1','2affix2','2affix3','2affix4']
    item2affixVal = ['2affix1Value','2affix2Value','2affix3Value','2affix4Value']

    affixInputList = list((vars(dummyEquip).keys()))
    affixInputList[0]=''

    layout = [[sg.Text('Item1',justification='c')],
               [sg.Combo(affixInputList,key='affix1',readonly=True),
               sg.Input(key='affix1Value')],
               [sg.Combo(affixInputList,key='affix2',readonly=True),
               sg.Input(key='affix2Value')],
               [sg.Combo(affixInputList,key='affix3',readonly=True),
               sg.Input(key='affix3Value')],
               [sg.Combo(affixInputList,key='affix4',readonly=True),
               sg.Input(key='affix4Value')],
               [sg.Text('', size = 8,key='item1', relief='raised',
                        justification = 'c')],
               [sg.Text('Item2',justification='c')],
               [sg.Combo(affixInputList,key='2affix1',readonly=True),
               sg.Input(key='2affix1Value')],
               [sg.Combo(affixInputList,key='2affix2',readonly=True),
               sg.Input(key='2affix2Value')],
               [sg.Combo(affixInputList,key='2affix3',readonly=True),
               sg.Input(key='2affix3Value')],
               [sg.Combo(affixInputList,key='2affix4',readonly=True),
               sg.Input(key='2affix4Value')],
               [sg.Text('', size = 8,key='item2', relief='raised',
                        justification = 'c')],
               [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window('Compare', layout, modal=True, finalize=True)

    while True:
        event, values = window.read()

        if event == 'Ok':
            item1AffixArgs=[]
            item2AffixArgs=[]
            for a, v in zip(item1Affix, item1affixVal):
                if bool(values[a]) and bool(values[v]):
                    item1AffixArgs.append((values[a],values[v]))
                item1 = Equipment('item1',*item1AffixArgs)

            for a, v in zip(item2Affix, item2affixVal):
                if bool(values[a]) and bool(values[v]):
                    item2AffixArgs.append((values[a],values[v]))
                item2 = Equipment('item2',*item2AffixArgs)

            _,dmg1,dmg2 = damage.compare(item1,item2)
            
            window['item1'].update(f'{int(dmg1):,}')
            window['item2'].update(f'{int(dmg2):,}')
                                
        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break


if __name__ == '__main__':
    main()