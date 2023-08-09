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
            plt.plot(x, vulnerability,'c', label='Vuln')
        if criticalChance:
            criticalChance = self.hitPreview(x, 'criticalChance')
            plt.plot(x, criticalChance, 'grey', label='Crit Chance')
        if criticalDamage:
            criticalDamage = self.hitPreview(x, 'criticalDamage')
            plt.plot(x, criticalDamage,'r', label = 'Crit Dmg')
        if overpowerChance:
            overpowerChance = self.hitPreview(x, 'overpowerChance')
            plt.plot(x, overpowerChance, 'grey', label='Ovpw Chance')
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
                              self.overpowerChance,
                              self.overpowerDamage,
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
                        criticalDamage, overpowerChance,
                        overpowerDamage, Legendary):

    damage = D4damage(eval(skill),
                      eval(baseDamageMin),
                      eval(baseDamageMax),
                      eval(mainStat))
        
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
