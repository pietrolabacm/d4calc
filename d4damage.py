import random
import statistics
import PySimpleGUI as sg
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
    
    def toDict(self):
        dmgDict = {}
        dmgDict['skill'] = self.skill
        dmgDict['baseDamageMin'] = self.baseDamageMin
        dmgDict['baseDamageMax'] = self.baseDamageMax
        dmgDict['mainAttribute'] = self.mainAttribute
        dmgDict['additive'] = self.additive
        dmgDict['vulnerability'] = self.vulnerability
        dmgDict['criticalChance'] = self.criticalChance
        dmgDict['criticalDamage'] = self.criticalDamage
        dmgDict['overpowerChance'] = self.overpowerChance
        dmgDict['overpowerDamage'] = self.overpowerDamage
        


        

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