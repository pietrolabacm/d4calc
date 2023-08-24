import random
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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


    def graph(self, value, skill, baseDamage, mainAttribute, additive,
              vulnerability, criticalChance, criticalDamage,
              overpowerChance, overpowerDamage, legendary):
        
        x = np.linspace(0, value, num=20)

        if baseDamage:
            baseDamage = self.hitPreview(x, 'baseDamage')
            baseDamage = plt.plot(x, baseDamage,'k', label='B Dmg')
        if skill:
            skill = self.hitPreview(x, 'skill')
            skill = plt.plot(x, skill, 'y', label='Skill')
        if mainAttribute:
            mainAttribute = self.hitPreview(x, 'mainAttribute')
            plt.plot(x, mainAttribute, 'lightGreen', label='Main Att')
        if additive:
            additive = self.hitPreview(x, 'additive')
            plt.plot(x, additive,'g', label='Add')
        if vulnerability:
            vulnerability = self.hitPreview(x, 'vulnerability')
            plt.plot(x, vulnerability,'c', label='Vuln')
        if criticalChance:
            criticalChance = self.hitPreview(x, 'criticalChance')
            plt.plot(x, criticalChance, 'grey', label='Crit Chance')
        if criticalDamage:
            criticalDamage = self.hitPreview(x, 'criticalDamage')
            plt.plot(x, criticalDamage,'r', label = 'Crit Dmg')
        if overpowerChance:
            overpowerChance = self.hitPreview(x, 'overpowerChance')
            plt.plot(x, overpowerChance, 'lightBlue', label='Ovpw Chance')
        if overpowerDamage:
            overpowerDamage = self.hitPreview(x, 'overpowerDamage')
            plt.plot(x, overpowerDamage,'b', label = 'Ovpw Dmg')
        if legendary:
            legendary = self.hitPreview(x, 'legendary')
            plt.plot(x, legendary, 'orange', label='Legendary')

        plt.ylabel('Damage')
        plt.xlabel('Affix Variance')
        plt.grid(True)
        plt.legend()
        plt.ticklabel_format(scilimits=(-5, 8))
        #yaxis = plt.gca().get_yticks()
        #plt.gca().set_yticklabels(['{:,.0f}'.format(i) for i in yaxis])
        plt.show()

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



def readDamageFromInput(skill, baseDamageMin, baseDamageMax, mainAttribute,
                        additive, vulnerability, criticalChance,
                        criticalDamage, overpowerChance,
                        overpowerDamage, Legendary):

    damage = D4damage(eval(skill),
                      eval(baseDamageMin),
                      eval(baseDamageMax),
                      eval(mainAttribute))
    
    if additive:
        damage.additive = eval(additive)
    if vulnerability:
        damage.vulnerability = eval(vulnerability)
    if criticalChance:
        damage.criticalChance = eval(criticalChance)
    if criticalDamage:
        damage.criticalDamage = eval(criticalDamage)
    if Legendary:
        damage.legendary = eval(Legendary)
    if overpowerChance:
        damage.overpowerChance = eval(overpowerChance)
    if overpowerDamage:
        damage.overpowerDamage = eval(overpowerDamage)

    return damage

##############################################################################
#                          STREAMLIT STARTS HERE
##############################################################################

import streamlit as st

if 'calculate' not in st.session_state:
    st.session_state.calculate = False
if 'mean' not in st.session_state:
    st.session_state.mean = False
if 'graph' not in st.session_state:
    st.session_state.graph = False

def click_calculate():
    st.session_state.calculate = True

def click_mean():
    if st.session_state.mean:
        st.session_state.mean=False
    else:
        st.session_state.mean=True

def click_graph():
    if st.session_state.graph:
        st.session_state.graph=False
    else:
        st.session_state.graph=True


st.title('D4Calc')

skill = st.number_input('Skill    :red[*required]', format='%.2f',step=0.5)
col1, col2 = st.columns(2)
baseDamageMin = col1.number_input('Min. Damage    :red[*required]', 
                                  format='%.2f', step=0.5)
baseDamageMax = col2.number_input('Max. Damage    :red[*required]', 
                                  format='%.2f', step=0.5)
mainAttribute = st.number_input('Main Attribute    :red[*required]', 
                                format='%d',step=1)
additive = st.number_input('Additive', format='%.2f', step=0.5)
vulnerability = st.number_input('Vulnerability', format='%.2f', step=0.5)
col1, col2 = st.columns(2)
criticalChance = col1.number_input('Critical Chance', format='%.2f',step=0.2,
                                   value=5.0)
criticalDamage = col2.number_input('Critical Damage', format='%.2f',step=0.5,
                                   value=50.0)
overpowerChance = col1.number_input('Overpower Chance', format='%.2f',step=0.2,
                                    value=3.0)
overpowerDamage = col2.number_input('Overpower Damage', format='%.2f',step=0.5,
                                    value=50.0)
legendary = st.number_input('Legendary', format='%.2f', step=0.5)

buttonCol1, buttonCol2, buttonCol3 = st.columns(3)
buttonCol1.button('Calculate',on_click=click_calculate, use_container_width=True)
buttonCol2.button('Mean', on_click=click_mean, use_container_width=True)
buttonCol3.button('Graph', on_click=click_graph, use_container_width=True)


affixValue = st.slider('Affix Value',0,100)

col1, col2, col3, col4 = st.columns(4)
skillCheck = col1.checkbox('Skill')
baseDamageCheck = col2.checkbox('Base Damage')
mainAttributeCheck = col3.checkbox('Main Attribute')
additiveCheck = col4.checkbox('Additive')

vulnerabilityCheck = col1.checkbox('Vulnerability')
criticalChanceCheck = col2.checkbox('Critical Chance')
criticalDamageCheck = col3.checkbox('Critical Damage')
overpowerChanceCheck = col4.checkbox('Overpower Chance')

overpowerDamageCheck = col1.checkbox('Overpower Damage')
legendaryCheck = col2.checkbox('Legendary')

if st.session_state.calculate:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                   vulnerability, criticalChance, criticalDamage, 
                   overpowerChance, overpowerDamage)
    hit, critical, overpower = dmg.hit()
    color = ':black'

    if critical:
        color = ':red'
    if overpower:
        color = ':blue'
    if critical and overpower:
        color = ':orange'
    buttonCol1.write('%s[%.2f]' % (color,hit))

if st.session_state.mean:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                   vulnerability, criticalChance, criticalDamage, 
                   overpowerChance, overpowerDamage)
    meanHit = dmg.meanHit()
    buttonCol2.write('%.2f' % meanHit)

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
