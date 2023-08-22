import streamlit as st
from d4damage import *

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
col1, col2, col3 = st.columns(3)
col1.button('Calculate',on_click=click_calculate, use_container_width=True)
col2.button('Mean', on_click=click_mean, use_container_width=True)
col3.button('Graph', on_click=click_graph, use_container_width=True)
rangeValue = col3.slider('Affix Range',0,60,format=int)


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
    col1.write('%s[%.2f]' % (color,hit))

if st.session_state.mean:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                   vulnerability, criticalChance, criticalDamage, 
                   overpowerChance, overpowerDamage)
    meanHit = dmg.meanHit()
    col2.write('%.2f' % meanHit)

if st.session_state.graph:
    dmg = D4damage(skill, baseDamageMin, baseDamageMax, mainAttribute,additive,
                   vulnerability, criticalChance, criticalDamage, 
                   overpowerChance, overpowerDamage)
    col3.write(rangeValue)
    graph = dmg.graph(rangeValue,True,True,False,False,False,False,False,False,False,False)
    st.plotly_chart(graph)
