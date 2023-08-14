import streamlit as st
from d4damage import *

if 'calculate' not in st.session_state:
    st.session_state.calculate = False

def click_calculate():
    st.session_state.calculate = True


st.title('D4Calc')

skill = st.number_input('Skill  :red[*required]', format='%.2f',step=0.5)
col1, col2 = st.columns(2)
baseDamageMin = col1.number_input('Min. Damage', format='%.2f', step=0.5)
baseDamageMax = col2.number_input('Max. Damage', format='%.2f', step=0.5)
mainAttribute = st.number_input('Main Attribute', format='%d',step=1)
additive = st.number_input('Additive', format='%.2f', step=0.5)
vulnerability = st.number_input('Vulnerability', format='%.2f', step=0.5)
col1, col2 = st.columns(2)
criticalChance = col1.number_input('Critical Chance', format='%.2f',step=0.2)
criticalDamage = col2.number_input('Critical Damage', format='%.2f',step=0.5)

st.button('Calculate',on_click=click_calculate)


if st.session_state.calculate:
    st.write('%.2f' % dmg(skill,bdamage))
