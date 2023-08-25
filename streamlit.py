from d4damage import *
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
    color = 'black'

    if critical:
        color = '#ebdb34'
    if overpower:
        color = 'blue'
    if critical and overpower:
        color = 'orange'
    #buttonCol1.write('%s[%.2f]' % (color,hit))
    buttonCol1.write('<div style="text-align: center;color:%s;"> %.2f </div>' % (color,hit), unsafe_allow_html=True)

if st.session_state.mean:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                   vulnerability, criticalChance, criticalDamage, 
                   overpowerChance, overpowerDamage)
    meanHit = dmg.meanHit()
    #buttonCol2.write('%.2f' % meanHit)
    buttonCol2.write('<div style="text-align: center"> %.2f </div>' % (meanHit), unsafe_allow_html=True)

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
