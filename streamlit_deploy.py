import random
import statistics
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json as js
import csv
import os

class D4damage():
    def __init__(self, skill, baseDamageMin, baseDamageMax, mainAttribute, 
                 additive=0, vulnerability=0, criticalChance=5, 
                 criticalDamage=50, overpowerChance=3, overpowerDamage=50,
                 legendary=0):
        self.skill = skill
        self.baseDamageMin = baseDamageMin
        self.baseDamageMax = baseDamageMax
        self.mainAttribute = mainAttribute
        self.additive = additive
        self.vulnerability = vulnerability
        self.criticalChance = criticalChance
        self.criticalDamage = criticalDamage
        self.overpowerChance = overpowerChance
        self.overpowerDamage = overpowerDamage
        self.legendary = legendary
        self.baseDamage = statistics.mean([baseDamageMin,baseDamageMax])

    def getAffix(self,var):
        affixDict = {'skill': self.skill,
                        'baseDamageMin': self.baseDamageMin,
                        'baseDamageMax': self.baseDamageMax,
                        'mainAttribute': self.mainAttribute,
                        'additive': self.additive,
                        'vulnerability': self.vulnerability,
                        'criticalChance': self.criticalChance,
                        'criticalDamage': self.criticalDamage,
                        'overpowerChance': self.overpowerChance,
                        'overpowerDamage': self.overpowerDamage,
                        'legendary': self.legendary}
        return affixDict[var]

        self.addAffixDict = {'skill': self.addSkill,
                             'mainAttribute': self.addMainAttribute,
                             'additive': self.addAdditive,
                             'vulnerability': self.addVulnerability,
                             'criticalChance': self.addCriticalChance,
                             'criticalDamage': self.addCriticalDamage,
                             'overpowerChance': self.addOverpowerChance,
                             'overpowerDamage': self.addOverpowerDamage,
                             'legendary': self.addLegendary}
    
    def addSkill(self,value):
        self.skill = self.skill + value
        return self.skill
    
    def addMainAttribute(self,value):
        self.mainAttribute = self.mainAttribute + value
        return self.mainAttribute
    
    def addAdditive(self,value):
        self.additive = value
        return self.additive
    
    def addVulnerability(self,value):
        self.vulnerability = self.vulnerability + value
        return self.vulnerability

    def addCriticalChance(self,value):
        self.criticalChance = self.criticalChance + value
        return self.criticalChance

    def addCriticalDamage(self,value):
        self.criticalDamage = self.mainAttribute + value
        return self.mainAttribute

    def addOverpowerChance(self,value):
        self.overpowerChance = self.overpowerChance + value
        return self.overpowerChance
    
    def addOverpowerDamage(self,value):
        self.overpowerDamage = self.overpowerDamage + value
        return self.overpowerDamage

    def addLegendary(self,value):
        self.legendary = self.legendary + value
        return self.legendary

    #This function rolls your hit naturally
    #It does not take averages from your crit and base dmg
    def hitTimes(self,times):
        hitList = []
        critNumber = 0
        overpowerNumber = 0
        for i in range(times):
            randomBaseDamage = random.randint(self.baseDamageMin, 
                                              self.baseDamageMax)
            hit=(((randomBaseDamage * (self.skill/100)) 
                 *(1 + self.mainAttribute/1000) 
                 *(1 + self.additive/100) 
                 *(1 + self.vulnerability/100)  
                 *(1 + self.legendary/100)))
            if random.randint(0,100)<=self.criticalChance:
                critNumber+=1
                hit = hit*(1+self.criticalDamage/100)
            if random.randint(0,100)<=self.overpowerChance:
                overpowerNumber+=1
                hit = hit*(1+self.overpowerDamage/100)
            hitList.append(hit)
        return [sum(hitList), statistics.mean(hitList),
                critNumber, overpowerNumber]
    
    def meanHit(self):
        hit = ((self.baseDamage * (self.skill/100)) 
               *(1 + self.mainAttribute/1000)
               *(1 + self.additive/100) 
               *(1 + self.vulnerability/100) 
               *(1 + ((self.criticalChance/100) * (self.criticalDamage/100)))
               *(1 + ((self.overpowerChance/100) * (self.overpowerDamage/100))) 
               *(1 + self.legendary/100))
        return hit

    def hit(self):
        critical = False
        overpower = False
        randomBaseDamage = random.randint(self.baseDamageMin, 
                                          self.baseDamageMax)
        hit=(((randomBaseDamage * (self.skill/100)) 
                *(1 + self.mainAttribute/1000) 
                *(1 + self.additive/100) 
                *(1 + self.vulnerability/100)  
                *(1 + self.legendary/100)))
        if random.randint(0,100)<=self.criticalChance:
            critical = True
            hit = hit*(1+self.criticalDamage/100)
        if random.randint(0,100)<=self.overpowerChance:
            overpower = True
            hit = hit*(1+self.overpowerDamage/100)
        return hit, critical, overpower
    
    def hitPreview(self, valueArray, affix):
        baseDamage = self.baseDamage
        skill = self.skill
        mainAttribute = self.mainAttribute
        additive = self.additive
        vulnerability = self.vulnerability
        criticalChance = self.criticalChance
        criticalDamage = self.criticalDamage
        overpowerChance = self.overpowerChance
        overpowerDamage = self.overpowerDamage
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
        if affix == 'overpowerChance':
            overpowerChance = self.overpowerChance + valueArray
        if affix == 'overpowerDamage':
            overpowerDamage = self.overpowerDamage + valueArray
        if affix == 'legendary':
            legendary = self.legendary + valueArray


        hit = ((baseDamage * (skill/100)) 
               *(1 + mainAttribute/1000)
               *(1 + additive/100) 
               *(1 + vulnerability/100) 
               *(1 + ((criticalChance/100) * (criticalDamage/100)))
               *(1 + ((overpowerChance/100) * (overpowerDamage/100))) 
               *(1 + legendary/100))
        return hit


    #def graph(self, value, skill, baseDamage, mainAttribute, additive,
    #          vulnerability, criticalChance, criticalDamage,
    #          overpowerChance, overpowerDamage, legendary):
    #    
    #    x = np.linspace(0, value, num=20)
#
    #    if baseDamage:
    #        baseDamage = self.hitPreview(x, 'baseDamage')
    #        baseDamage = plt.plot(x, baseDamage,'k', label='B Dmg')
    #    if skill:
    #        skill = self.hitPreview(x, 'skill')
    #        skill = plt.plot(x, skill, 'y', label='Skill')
    #    if mainAttribute:
    #        mainAttribute = self.hitPreview(x, 'mainAttribute')
    #        plt.plot(x, mainAttribute, 'lightGreen', label='Main Att')
    #    if additive:
    #        additive = self.hitPreview(x, 'additive')
    #        plt.plot(x, additive,'g', label='Add')
    #    if vulnerability:
    #        vulnerability = self.hitPreview(x, 'vulnerability')
    #        plt.plot(x, vulnerability,'c', label='Vuln')
    #    if criticalChance:
    #        criticalChance = self.hitPreview(x, 'criticalChance')
    #        plt.plot(x, criticalChance, 'grey', label='Crit Chance')
    #    if criticalDamage:
    #        criticalDamage = self.hitPreview(x, 'criticalDamage')
    #        plt.plot(x, criticalDamage,'r', label = 'Crit Dmg')
    #    if overpowerChance:
    #        overpowerChance = self.hitPreview(x, 'overpowerChance')
    #        plt.plot(x, overpowerChance, 'lightBlue', label='Ovpw Chance')
    #    if overpowerDamage:
    #        overpowerDamage = self.hitPreview(x, 'overpowerDamage')
    #        plt.plot(x, overpowerDamage,'b', label = 'Ovpw Dmg')
    #    if legendary:
    #        legendary = self.hitPreview(x, 'legendary')
    #        plt.plot(x, legendary, 'orange', label='Legendary')
#
    #    plt.ylabel('Damage')
    #    plt.xlabel('Affix Variance')
    #    plt.grid(True)
    #    plt.legend()
    #    plt.ticklabel_format(scilimits=(-5, 8))
    #    #yaxis = plt.gca().get_yticks()
    #    #plt.gca().set_yticklabels(['{:,.0f}'.format(i) for i in yaxis])
    #    plt.show()

    def graphDf(self, value, skill, baseDamage, mainAttribute, additive,
                    vulnerability, criticalChance, criticalDamage,
                    overpowerChance, overpowerDamage, legendary):
        
        linesDict = {}
        indexDict = {}
        x = np.linspace(0, value, num=20,dtype=int)
        indexDict['x'] = x

        if baseDamage:
            baseDamage = self.hitPreview(x, 'baseDamage')
            linesDict['Base Damage'] = baseDamage
        if skill:
            skill = self.hitPreview(x, 'skill')
            linesDict['Skill'] = skill
        if mainAttribute:
            mainAttribute = self.hitPreview(x, 'mainAttribute')
            linesDict['Main Attribute'] = mainAttribute
        if additive:
            additive = self.hitPreview(x, 'additive')
            linesDict['Additive'] = additive
        if vulnerability:
            vulnerability = self.hitPreview(x, 'vulnerability')
            linesDict['Vulnerability'] = vulnerability
        if criticalChance:
            criticalChance = self.hitPreview(x, 'criticalChance')
            linesDict['Critical Chance'] = criticalChance
        if criticalDamage:
            criticalDamage = self.hitPreview(x, 'criticalDamage')
            linesDict['Critical Damage'] = criticalDamage
        if overpowerChance:
            overpowerChance = self.hitPreview(x, 'overpowerChance')
            linesDict['Overpower Chance'] = overpowerChance
        if overpowerDamage:
            overpowerDamage = self.hitPreview(x, 'overpowerDamage')
            linesDict['Overpower Damage'] = overpowerDamage
        if legendary:
            legendary = self.hitPreview(x, 'legendary')
            linesDict['Legendary'] = legendary

        df = pd.DataFrame(linesDict, index=indexDict['x'])
        return(df)
    

    def equip(self, equipment):
        self.mainAttribute = self.mainAttribute + equipment.mainAttribute
        self.vulnerability = self.vulnerability + equipment.vulnerability
        self.criticalChance = self.criticalChance + equipment.criticalChance
        self.criticalDamage = self.criticalDamage + equipment.criticalDamage
        self.overpowerChance = self.overpowerChance + equipment.overpowerChance
        self.overpowerDamage = self.overpowerDamage + equipment.overpowerDamage
        self.legendary = self. legendary + equipment.legendary
        self.additive = self.additive + equipment.additive
    
    def remove(self, equipment):
        self.mainAttribute = self.mainAttribute - equipment.mainAttribute
        self.vulnerability = self.vulnerability - equipment.vulnerability
        self.criticalChance = self.criticalChance - equipment.criticalChance
        self.criticalDamage = self.criticalDamage - equipment.criticalDamage
        self.overpowerChance = self.overpowerChance - equipment.overpowerChance
        self.overpowerDamage = self.overpowerDamage - equipment.overpowerDamage
        self.legendary = self. legendary - equipment.legendary
        self.additive = self.additive - equipment.additive

    def compare(self,equip1,equip2):
        base = self.meanHit()

        self.equip(equip1)
        hit1 = self.meanHit()
        self.remove(equip1)

        self.equip(equip2)
        hit2 = self.meanHit()
        self.remove(equip2)

        return base, hit1, hit2

        

class Equipment():
    def __init__(self,name,*affixes):
        self.name = name
        #main attribute
        self.mainAttribute = 0
        self.allStats = 0

        self.vulnerability = 0
        self.criticalChance = 0
        self.criticalDamage = 0
        self.overpowerChance = 0
        self.overpowerDamage = 0
        self.legendary = 0

        #additive
        self.damage = 0
        self.damageSlow = 0
        self.damageBurning = 0

        for i in affixes:
            setattr(self,i[0],int(i[1]))
        
        mainAttributeList = [self.mainAttribute, self.allStats]
        additiveList = [self.damage, self.damageSlow, self.damageBurning]
        
        self.mainAttribute = sum(mainAttributeList)
        self.additive = sum(additiveList)

##############################################################################
#                          STREAMLIT STARTS HERE
##############################################################################

import streamlit as st
from streamlit import *

if 'calculate' not in st.session_state:
    st.session_state.calculate = False
if 'graph' not in st.session_state:
    st.session_state.graph = False
if 'load' not in st.session_state:
    st.session_state.load = False

widget_values = {}

def make_recording_widget(f):

    def wrapper(label, *args, **kwargs):
        widget_value = f(label, *args, **kwargs)
        widget_values[label] = widget_value
        return widget_value
    
    return wrapper

numInput = make_recording_widget(st.number_input)

def load():
    if st.session_state.load:
        st.session_state.load = False
    else:
        st.session_state.load = True

def click_calculate():
    st.session_state.calculate = True

def click_graph():
    if st.session_state.graph:
        st.session_state.graph=False
    else:
        st.session_state.graph=True


st.title('D4Calc', False)

superCol1, superCol2 = st.columns(2)

#with superCol1 as scol1:
#    skill = st.empty()
#    colBDmg1, colBdmg2 = st.columns(2)
#    with colBDmg1:
#        baseDamageMin = st.empty()
#    with colBdmg2:
#        baseDamageMax = st.empty()
#    mainAttribute = st.empty()
#    additive = st.empty
#    vulnerability = st.empty
#    colChance1, colChance2 = st.columns(2)
#    with colChance1:
#        criticalChance = st.empty()
#        overpowerChance = st.empty()
#    with colChance2:
#        criticalDamage = st.empty()
#        overpowerDamage = st.empty()
#    legendary = st.empty()    

if not st.session_state.load:
    with superCol1:
        skill = numInput('Skill :red[*required]', 
                    format='%.2f', 
                    step=0.5)

        col1, col2 = st.columns(2)
        with col1:
            baseDamageMin = numInput('Min. Damage :red[*required]', 
                                    format='%d', 
                                    step=1)
        with col2:
            baseDamageMax = numInput('Max. Damage :red[*required]', 
                                    format='%d', 
                                    step=1)
            
        mainAttribute = numInput('Main Attribute :red[*required]', 
                                        format='%d',
                                        step=1)
        additive = numInput('Additive', 
                                format='%.2f', 
                                step=0.5,
                                key='additive')
        vulnerability = numInput('Vulnerability', 
                                        format='%.2f', 
                                        step=0.5,
                                        key='vulnerability')
        col1, col2 = st.columns(2)
        with col1:
            criticalChance = numInput('Critical Chance', 
                                            format='%.2f',
                                            step=0.2,
                                            value=5.0,
                                            key='criticalChance')
            
            overpowerChance = numInput('Overpower Chance', 
                                            format='%.2f',
                                            step=0.2,
                                            value=3.0,
                                            key='overpowerChance')
        
        with col2:
            criticalDamage = numInput('Critical Damage', 
                                            format='%.2f',
                                            step=0.5,
                                            value=50.0,
                                            key='criticalDamage')
            
            overpowerDamage = numInput('Overpower Damage', 
                                                format='%.2f',
                                                step=0.5,
                                                value=50.0,
                                                key='overpowerDamage')
        legendary = numInput('Legendary', 
                                    format='%.2f', 
                                    step=0.5,
                                    key='legendary')
        
with superCol2 as scol2:
    download = st.empty()
    fileUpload = st.file_uploader('Upload:file_folder:',type = 'json', 
                                  on_change = load)

    st.button('Calculate',
                            on_click=click_calculate, 
                            use_container_width=True)
    st.button('Graph', 
                            on_click=click_graph, 
                            use_container_width=True)
    
    textOut1, textOut2 = st.columns(2)

    affixValue = st.slider('Affix Value',0,100)

    col1, col2 = st.columns(2)
    skillCheck = col1.checkbox('Skill')
    baseDamageCheck = col2.checkbox('Base Damage')

    mainAttributeCheck = col1.checkbox('Main Attribute')
    additiveCheck = col2.checkbox('Additive')

    vulnerabilityCheck = col1.checkbox('Vulnerability')
    criticalChanceCheck = col2.checkbox('Critical Chance')

    criticalDamageCheck = col1.checkbox('Critical Damage')
    overpowerChanceCheck = col2.checkbox('Overpower Chance')

    overpowerDamageCheck = col1.checkbox('Overpower Damage')
    legendaryCheck = col2.checkbox('Legendary')
        

if st.session_state.load and fileUpload is not None:
    widget_values = js.loads(fileUpload.getvalue())
    skillDefault = widget_values['Skill :red[*required]']
    baseDamageMinDefault = widget_values['Min. Damage :red[*required]']
    baseDamageMaxDefault = widget_values['Max. Damage :red[*required]']
    mainAttributeDefault = widget_values['Main Attribute :red[*required]']
    additiveDefault = widget_values['Additive']
    vulnerabilityDefault = widget_values['Vulnerability']
    criticalChanceDefault = widget_values['Critical Chance']
    overpowerChanceDefault = widget_values['Overpower Chance']
    criticalDamageDefault = widget_values['Critical Damage']
    overpowerDamageDefault = widget_values['Overpower Damage']
    legendaryDefault = widget_values['Legendary']

    with superCol1:
        skill = numInput('Skill :red[*required]', 
                    format='%.2f', 
                    step=0.5,
                    value=skillDefault)

        col1, col2 = st.columns(2)
        with col1:
            baseDamageMin = numInput('Min. Damage :red[*required]', 
                                    format='%d', 
                                    step=1,
                                    value=baseDamageMinDefault)
        with col2:
            baseDamageMax = numInput('Max. Damage :red[*required]', 
                                    format='%d', 
                                    step=1,
                                    value=baseDamageMaxDefault)
            
        mainAttribute = numInput('Main Attribute :red[*required]', 
                                        format='%d',
                                        step=1,
                                        value=mainAttributeDefault)
        additive = numInput('Additive', 
                                format='%.2f', 
                                step=0.5,
                                key='additive',
                                value = additiveDefault)
        vulnerability = numInput('Vulnerability', 
                                        format='%.2f', 
                                        step=0.5,
                                        key='vulnerability',
                                        value = vulnerabilityDefault)
        col1, col2 = st.columns(2)
        with col1:
            criticalChance = numInput('Critical Chance', 
                                            format='%.2f',
                                            step=0.2,
                                            key='criticalChance',
                                            value=criticalChanceDefault)
            
            overpowerChance = numInput('Overpower Chance', 
                                            format='%.2f',
                                            step=0.2,
                                            key='overpowerChance',
                                            value=overpowerChanceDefault)
        
        with col2:
            criticalDamage = numInput('Critical Damage', 
                                            format='%.2f',
                                            step=0.5,
                                            key='criticalDamage',
                                            value=criticalDamageDefault)
            
            overpowerDamage = numInput('Overpower Damage', 
                                                format='%.2f',
                                                step=0.5,
                                                key='overpowerDamage',
                                                value=overpowerDamageDefault)
        legendary = numInput('Legendary', 
                                    format='%.2f', 
                                    step=0.5,
                                    key='legendary',
                                    value = legendaryDefault)


if st.session_state.calculate:
    if baseDamageMin>baseDamageMax:
        baseDamageMax=baseDamageMin
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
            vulnerability, criticalChance, criticalDamage, 
            overpowerChance, overpowerDamage)
    hit, critical, overpower = dmg.hit()


try:
    hit, critical, overpower = dmg.hit()
    meanHit = dmg.meanHit()
except:
    hit,critical, overpower = (0.0,False,False)
    meanHit = 0.0

color = 'white'

if critical:
    color = '#ebdb34'
if overpower:
    color = 'blue'
if critical and overpower:
    color = 'orange'


textOut1.write('<div style="text-align: center">Damage</div>', 
                unsafe_allow_html=True)
textOut1.write('<div style="text-align: center;color:%s;"> %.2f </div>' 
                % (color,hit), unsafe_allow_html=True)

textOut2.write('<div style="text-align: center">Mean Damage</div>', 
                unsafe_allow_html=True)
textOut2.write('<div style="text-align: center"> %.2f </div>' % (meanHit), 
                unsafe_allow_html=True)


if st.session_state.graph:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                vulnerability, criticalChance, criticalDamage, 
                overpowerChance, overpowerDamage)
    df = dmg.graphDf(affixValue,skillCheck,baseDamageCheck,mainAttributeCheck,
                    additiveCheck, vulnerabilityCheck, criticalChanceCheck,
                    criticalDamageCheck, overpowerChanceCheck, 
                    overpowerDamageCheck, legendaryCheck)
    
    tab1, tab2 = st.tabs(['Graph','Data'])
    tab1.line_chart(df)
    tab2.write(df)

download.download_button('Save:floppy_disk:',
                                  js.dumps(widget_values),
                                  'build.json',
                                  use_container_width=True)