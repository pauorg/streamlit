import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')

df_kart2 = df_kart[['Body','Weight','Acceleration','On-Road traction','Off-Road Traction','Ground Speed']]

#st.dataframe(df_kart)

st.dataframe(df_kart2.style
             .highlight_max(color='lightgreen', axis=0,subset=['Weight','Acceleration','On-Road traction','Off-Road Traction','Ground Speed'])
             .highlight_min(color='red', axis=0,subset=['Weight','Acceleration','On-Road traction','Off-Road Traction','Ground Speed'])
)

st.write("10 Fastest Bodies by Acceleration")
x = 10 
df_kart_fastest = df_kart[['Body', 'Weight','Acceleration','On-Road traction','Off-Road Traction', 'Ground Speed']].sort_values("Acceleration",ascending=False).iloc[0:x]
st.line_chart(df_kart_fastest, x='Body', y=['Weight','Acceleration','On-Road traction','Off-Road Traction', 'Ground Speed'])


st.write("Aggregate Stats of 7 Heaviest Karts")
x2 = 7
df_kart_heaviest = df_kart[['Body','Weight','Acceleration','On-Road traction','Off-Road Traction','Mini-Turbo','Ground Speed','Water Speed','Anti-Gravity Speed','Air Speed','Ground Handling','Water Handling','Anti-Gravity Handling','Air Handling']].sort_values("Weight",ascending=False).iloc[0:x2]
st.bar_chart(df_kart_heaviest, x='Body',y=['Acceleration','On-Road traction','Off-Road Traction','Mini-Turbo','Ground Speed','Water Speed','Anti-Gravity Speed','Air Speed','Ground Handling','Water Handling','Anti-Gravity Handling','Air Handling'])

chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]

df_unp_kart = df_single_kart.unstack().rename_axis(['Body','row number']).reset_index().drop(columns='row number').rename({0:'Strength'}, axis=1)
st.bar_chart(df_unp_kart, x='Body', y='Strength')