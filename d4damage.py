import random
import statistics
import PySimpleGUI as sg

class D4damage():
    __slots__ = ['_skill', '_baseDamageMin','_baseDamageMax', '_mainAttribute', '_additive', '_vulnerability','_criticalChance', '_criticalDamage', '_legendary']
    def __init__(self, skill, baseDamageMin, baseDamageMax, mainAttribute, additive=0, vulnerability=0, criticalChance=0, criticalDamage=0, legendary=0):
        self.skill = skill
        self.baseDamageMin = baseDamageMin
        self.baseDamageMax = baseDamageMax
        self.mainAttribute = mainAttribute
        self.additive = additive
        self.vulnerability = vulnerability
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage
        self.legendary = legendary
    
    @property
    def skill(self):
        return self._skill
    @skill.setter
    def skill(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value <= 0:
            raise ValueError('skill must be >0')
        self._skill = value

    @property
    def baseDamageMin(self):
        return self._baseDamageMin
    @baseDamageMin.setter
    def baseDamageMin(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value <= 0:
            raise ValueError('baseDamageMin must be >0')
        self._baseDamageMin = value

    @property
    def baseDamageMax(self):
        return self._baseDamageMax
    @baseDamageMax.setter
    def baseDamageMax(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value <= 0:
            raise ValueError('baseDamageMax must be >0')
        self._baseDamageMax = value

    @property
    def mainAttribute(self):
        return self._mainAttribute
    @mainAttribute.setter
    def mainAttribute(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value <= 0:
            raise ValueError('mainAttribute must be >0')
        self._mainAttribute = value
    
    @property
    def additive(self):
        return self._additive
    @additive.setter
    def additive(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value < 0:
            raise ValueError('additive must be >=0')
        self._additive = value

    @property
    def vulnerability(self):
        return self._vulnerability
    @vulnerability.setter
    def vulnerability(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value < 0:
            raise ValueError('vulnerability must be >=0')
        self._vulnerability = value

    @property
    def criticalChance(self):
        return self._criticalChance
    @criticalChance.setter
    def criticalChance(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value < 0:
            raise ValueError('criticalChance must be >=0')
        self._criticalChance = value
    
    @property
    def criticalDamage(self):
        return self._criticalDamage
    @criticalDamage.setter
    def criticalDamage(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value < 0:
            raise ValueError('criticalDamage must be >=0')
        self._criticalDamage = value

    @property
    def legendary(self):
        return self._legendary
    @legendary.setter
    def legendary(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError('Expected an int or float')
        if value < 0:
            raise ValueError('legendary must be >=0')
        self._legendary = value

    

    def hit(self):
        hitList = []
        for i in range(100000):
            randomBaseDamage = random.randint(self.baseDamageMin, self.baseDamageMax)
            hit = ((randomBaseDamage * (self.skill/100)) *
                    (1 + self.mainAttribute/1000) *
                    (1 + self.additive/100) *
                    (1 + self.vulnerability/100) *
                    (1+ ((self.criticalChance/100) * (self.criticalDamage/100))) *
                    (1 + self.legendary/100))
            hitList.append(hit)
        return statistics.mean(hitList)
    


layout = [  [sg.Text('D4 Calculator')],
            [sg.Text('Skill %', size=18), sg.InputText(key='skill', enable_events=True, expand_x=True)],
            [sg.Text('Base Damage Min', size=18), sg.InputText(key='baseDamageMin', enable_events=True, expand_x=True), sg.Text('Base Damage Max', size=18), sg.InputText(key='baseDamageMax', enable_events=True, expand_x=True)],            
            [sg.Text('Main Stat', size=18), sg.InputText(key='mainStat', enable_events=True, expand_x=True)],
            [sg.Text('Additive', size=18), sg.InputText(key='additive', enable_events=True, expand_x=True)],
            [sg.Text('Vulnerability', size=18), sg.InputText(key='vulnerability', enable_events=True, expand_x=True)],
            [sg.Text('Critical Chance',size=18), sg.InputText(key='criticalChance', enable_events=True, expand_x=True), sg.Text('Critical Damage', size=18), sg.InputText(key='criticalDamage', enable_events=True, expand_x=True)],
            [sg.Text('Legendary',size=18), sg.InputText(key='legendary', enable_events=True, expand_x=True)],
            [sg.Button('Calculate')]]

# Create the Window
window = sg.Window('D4 Calculator', layout, element_justification='r')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'skill' and values['skill'] and values['skill'][-1] not in ('0123456789'):
        window['skill'].update(values['skill'][:-1])
    
    if event == 'baseDamageMin' and values['baseDamageMin'] and values['baseDamageMin'][-1] not in ('0123456789'):
        window['baseDamageMin'].update(values['baseDamageMin'][:-1])

    if event == 'baseDamageMax' and values['baseDamageMax'] and values['baseDamageMax'][-1] not in ('0123456789'):
        window['baseDamageMax'].update(values['baseDamageMax'][:-1])
    
    if event == 'mainStat' and values['mainStat'] and values['mainStat'][-1] not in ('0123456789'):
        window['mainStat'].update(values['mainStat'][:-1])
    
    if event == 'additive' and values['additive'] and values['additive'][-1] not in ('0123456789'):
        window['additive'].update(values['additive'][:-1])

    if event == 'vulnerability' and values['vulnerability'] and values['vulnerability'][-1] not in ('0123456789'):
        window['vulnerability'].update(values['vulnerability'][:-1])

    if event == 'criticalChance' and values['criticalChance'] and values['criticalChance'][-1] not in ('0123456789'):
        window['criticalChance'].update(values['criticalChance'][:-1])

    if event == 'criticalDamage' and values['criticalDamage'] and values['criticalDamage'][-1] not in ('0123456789'):
        window['criticalDamage'].update(values['criticalDamage'][:-1])

    if event == 'legendary' and values['legendary'] and values['legendary'][-1] not in ('0123456789'):
        window['legendary'].update(values['legendary'][:-1])
    
    if event == 'Calculate':
        d1 = D4damage(float(values['skill']),
                    float(values['baseDamageMin']),
                    float(values['baseDamageMax']),
                    float(values['mainStat']))
        
        if values['additive']:
            d1.additive = float(values['additive'])
        if values['vulnerability']:
            d1.vulnerability = float(values['vulnerability'])
        if values['criticalChance']:
            d1.criticalChance = float(values['criticalChance'])
        if values['criticalDamage']:
            d1.criticalDamage = float(values['criticalDamage'])
        if values['legendary']:
            d1.legendary = float(values['legendary'])

        print('%0.2f' % d1.hit())

window.close()