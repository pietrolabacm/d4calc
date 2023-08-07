import random
import statistics
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

class D4damage():
    def __init__(self, skill, baseDamageMin, baseDamageMax, mainAttribute, 
                 additive=0, vulnerability=0, criticalChance=5, 
                 criticalDamage=50, legendary=0):
        self.skill = skill
        self.baseDamageMin = baseDamageMin
        self.baseDamageMax = baseDamageMax
        self.mainAttribute = mainAttribute
        self.additive = additive
        self.vulnerability = vulnerability
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage
        self.legendary = legendary
        self.baseDamage = statistics.mean([baseDamageMin,baseDamageMax])
    
    def hitTimes(self,times):
        hitList = []
        for i in range(times):
            randomBaseDamage = random.randint(self.baseDamageMin, 
                                              self.baseDamageMax)
            hit=((randomBaseDamage * (self.skill/100)) 
                 *(1 + self.mainAttribute/1000) 
                 *(1 + self.additive/100) 
                 *(1 + self.vulnerability/100) 
                 *(1 + ((self.criticalChance/100)*(self.criticalDamage/100))) 
                 *(1 + self.legendary/100))
            hitList.append(hit)
        return statistics.mean(hitList)
    
    def hit(self):
        hit = ((self.baseDamage * (self.skill/100)) 
               *(1 + self.mainAttribute/1000)
               *(1 + self.additive/100) 
               *(1 + self.vulnerability/100) 
               *(1+ ((self.criticalChance/100) * (self.criticalDamage/100))) 
               *(1 + self.legendary/100))
        return hit
    
    def hitPreview(self, valueArray, affix):
        
        baseDamage = self.baseDamage
        skill = self.skill
        mainAttribute = self.mainAttribute
        additive = self.additive
        vulnerability = self.vulnerability
        criticalChance = self.criticalChance
        criticalDamage = self.criticalDamage
        legendary = self.legendary

        if affix == 'baseDamage':
            baseDamage = self.baseDamage + valueArray
        if affix == 'skill':
            skill = self.skill + valueArray
        if affix == 'mainAttribute':
            mainAttribute = self.mainAttribute + valueArray
        if affix == 'additive':
            additive = self.additive + valueArray
        if affix == 'vulnerability':
            vulnerability = self.vulnerability + valueArray
        if affix == 'criticalChance':
            criticalChance = self.criticalChance + valueArray
        if affix == 'criticalDamage':
            criticalDamage = self.criticalDamage + valueArray
        if affix == 'legendary':
            legendary = self.legendary + valueArray

        hit = ((baseDamage * (skill/100)) 
               *(1 + mainAttribute/1000)
               *(1 + additive/100) 
               *(1 + vulnerability/100) 
               *(1+ ((criticalChance/100) * (criticalDamage/100))) 
               *(1 + legendary/100))
        return hit

    def graph(self, value, baseDamage, skill, mainAttribute, additive,
              vulnerability, criticalChance, criticalDamage, legendary):
        
        x = np.linspace(0, value, num=20)

        if baseDamage:
            baseDamage = self.hitPreview(x, 'baseDamage')
            plt.plot(x, baseDamage,'k')
        if skill:
            skill = self.hitPreview(x, 'skill')
            plt.plot(x, skill, 'y')
        if mainAttribute:
            mainAttribute = self.hitPreview(x, 'mainAttribute')
            plt.plot(x, mainAttribute, 'c')
        if additive:
            additive = self.hitPreview(x, 'additive')
            plt.plot(x, additive,'g')
        if vulnerability:
            vulnerability = self.hitPreview(x, 'vulnerability')
            plt.plot(x, vulnerability,'b')
        if criticalChance:
            criticalChance = self.hitPreview(x, 'criticalChance')
            plt.plot(x, criticalChance, 'grey')
        if criticalDamage:
            criticalDamage = self.hitPreview(x, 'criticalDamage')
            plt.plot(x, criticalDamage,'r')
        if legendary:
            legendary = self.hitPreview(x, 'legendary')
            plt.plot(x, legendary, 'orange')

        plt.show()

def readDamageFromInput(skill, baseDamageMin, baseDamageMax, mainStat,
                        additive, vulnerability, criticalChance,
                        criticalDamage, Legendary):
    damage = D4damage(float(skill),
                    float(baseDamageMin),
                    float(baseDamageMax),
                    float(mainStat))
        
    if additive:
        damage.additive = float(additive)
    if vulnerability:
        damage.vulnerability = float(vulnerability)
    if criticalChance:
        damage.criticalChance = float(criticalChance)
    if criticalDamage:
        damage.criticalDamage = float(criticalDamage)
    if Legendary:
        damage.legendary = float(Legendary)

    return damage


textBoxSize = 10

layout=[[sg.Text('D4 Calculator')],
        [sg.Text('Skill %', size=textBoxSize), 
         sg.InputText(key='skill', enable_events=True, expand_x=True),
         sg.Checkbox('',key='skillCheck')],
        [sg.Text('B. Dmg Min', size=textBoxSize), 
         sg.InputText(key='baseDamageMin', enable_events=True, expand_x=True), 
         sg.Text('B. Dmg Max', size=textBoxSize), 
         sg.InputText(key='baseDamageMax',enable_events=True, expand_x=True),
         sg.Checkbox('',key='baseDamageCheck')],            
        [sg.Text('Main Stat', size=textBoxSize), 
         sg.InputText(key='mainStat', enable_events=True, expand_x=True),
         sg.Checkbox('',key='mainStatCheck')],
        [sg.Text('Additive', size=textBoxSize), 
         sg.InputText(key='additive', enable_events=True, expand_x=True),
         sg.Checkbox('',key='additiveCheck')],
        [sg.Text('Vulnerability', size=textBoxSize), 
         sg.InputText(key='vulnerability', enable_events=True,expand_x=True),
         sg.Checkbox('',key='vulnerabilityCheck')],
        [sg.Text('Crit. Chance',size=textBoxSize), 
         sg.InputText(key='criticalChance', enable_events=True,expand_x=True),
         sg.Checkbox('',key='criticalChanceCheck'), 
         sg.Text('Crit. Damage', size=textBoxSize), 
         sg.InputText(key='criticalDamage',enable_events=True,expand_x=True),
         sg.Checkbox('',key='criticalDamageCheck')],
        [sg.Text('Legendary',size=textBoxSize), 
         sg.InputText(key='legendary', enable_events=True, expand_x=True),
         sg.Checkbox('',key='legendaryCheck')],
        [sg.Button('Calculate'), sg.Button('Graph')]]

# Create the Window
window = sg.Window('D4 Calculator', layout, element_justification='l',
                   default_element_size=(7,200))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    
    if (event == 'skill' and values['skill'] and values['skill'][-1] 
            not in ('0123456789')):
        window['skill'].update(values['skill'][:-1])
    
    if (event == 'baseDamageMin' and values['baseDamageMin'] 
            and values['baseDamageMin'][-1] not in ('0123456789')):
        window['baseDamageMin'].update(values['baseDamageMin'][:-1])

    if (event == 'baseDamageMax' and values['baseDamageMax'] 
            and values['baseDamageMax'][-1] not in ('0123456789')):
        window['baseDamageMax'].update(values['baseDamageMax'][:-1])
    
    if (event == 'mainStat' and values['mainStat'] 
            and values['mainStat'][-1] not in ('0123456789')):
        window['mainStat'].update(values['mainStat'][:-1])
    
    if (event == 'additive' and values['additive'] 
            and values['additive'][-1] not in ('0123456789')):
        window['additive'].update(values['additive'][:-1])

    if (event == 'vulnerability' and values['vulnerability'] 
            and values['vulnerability'][-1] not in ('0123456789')):
        window['vulnerability'].update(values['vulnerability'][:-1])

    if (event == 'criticalChance' and values['criticalChance'] 
            and values['criticalChance'][-1] not in ('0123456789')):
        window['criticalChance'].update(values['criticalChance'][:-1])

    if (event == 'criticalDamage' and values['criticalDamage'] 
            and values['criticalDamage'][-1] not in ('0123456789')):
        window['criticalDamage'].update(values['criticalDamage'][:-1])

    if (event == 'legendary' and values['legendary'] 
            and values['legendary'][-1] not in ('0123456789')):
        window['legendary'].update(values['legendary'][:-1])
    
    if event == 'Calculate':
        dmg1 = readDamageFromInput(values['skill'], values['baseDamageMin'],
                                   values['baseDamageMax'], values['mainStat'],
                                   values['additive'], values['vulnerability'],
                                   values['criticalChance'],
                                   values['criticalDamage'], 
                                   values['legendary'])

        print('%0.2f' % dmg1.hit())

    if event == 'Graph':
        dmg1 = readDamageFromInput(values['skill'], values['baseDamageMin'],
                            values['baseDamageMax'], values['mainStat'],
                            values['additive'], values['vulnerability'],
                            values['criticalChance'],
                            values['criticalDamage'], 
                            values['legendary'])
        dmg1.graph(20, values['skillCheck'], values['baseDamageCheck'],
                   values['mainStatCheck'], values['additiveCheck'],
                   values['vulnerabilityCheck'], values['criticalChanceCheck'],
                   values['criticalDamageCheck'], values['legendaryCheck'])

window.close()

