import random
import statistics
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

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

    def graph(self, value, skill, baseDamage, mainAttribute, additive,
              vulnerability, criticalChance, criticalDamage, legendary):
        
        x = np.linspace(0, value, num=20)

        if baseDamage:
            baseDamage = self.hitPreview(x, 'baseDamage')
            plt.plot(x, baseDamage,'k', label='B Dmg')
        if skill:
            skill = self.hitPreview(x, 'skill')
            plt.plot(x, skill, 'y', label='Skill')
        if mainAttribute:
            mainAttribute = self.hitPreview(x, 'mainAttribute')
            plt.plot(x, mainAttribute, 'c', label='Main Att')
        if additive:
            additive = self.hitPreview(x, 'additive')
            plt.plot(x, additive,'g', label='Add')
        if vulnerability:
            vulnerability = self.hitPreview(x, 'vulnerability')
            plt.plot(x, vulnerability,'b', label='Vuln')
        if criticalChance:
            criticalChance = self.hitPreview(x, 'criticalChance')
            plt.plot(x, criticalChance, 'grey', label='Crit Chance')
        if criticalDamage:
            criticalDamage = self.hitPreview(x, 'criticalDamage')
            plt.plot(x, criticalDamage,'r', label = 'Crit Dmg')
        if legendary:
            legendary = self.hitPreview(x, 'legendary')
            plt.plot(x, legendary, 'orange', label='Legendary')

        plt.ylabel('Damage')
        plt.xlabel('Affix Variance')
        plt.grid(True)
        plt.legend()
        plt.show()

    def saveDamage(self, fileName, path):
        with open(os.path.join(path,'%s.csv' % fileName)
                  ,'w', newline='') as file:
            writter = csv.writer(file)
            writter.writerow([self.skill,
                              self.baseDamageMin,
                              self.baseDamageMax,
                              self.mainAttribute,
                              self.additive,
                              self.vulnerability,
                              self.criticalChance,
                              self.criticalDamage,
                              self.legendary])
    
    def loadDamage(fileName, path):
        with open(os.path.join(path,fileName)) as file:
            reader = csv.reader(file)
            row = next(reader)
            row = [int(i) for i in row]
            damage = D4damage(*row)
        return damage

            
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
