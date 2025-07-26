import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Pokemon.csv')
df.rename(columns={'Sp. Atk': 'Sp_Atk', 'Sp. Def': 'Sp_Def', '#':'ID'}, inplace=True)
df['Type 2'].fillna('None', inplace=True)
df['Variants'] = df.groupby(df['ID']).cumcount()

st.title('Pokémon Dataset Analysis')

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.dataframe(df)

st.subheader('Distribution of Attack')
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.histplot(df['Attack'], kde=True, bins=30, color='skyblue', ax=ax1)
ax1.set_title('Distribution of Attack')
ax1.set_xlabel('Attack')
ax1.set_ylabel('Count')
st.pyplot(fig1)

st.subheader('Total Stats: Legendary vs Non-Legendary')
fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.boxplot(data=df, x='Legendary', y='Total', palette='Set2',ax=ax2)
ax2.set_title('Total Stats: Legendary vs Non-Legendary')
ax2.set_xticklabels(['Non-Legendary', 'Legendary'])
st.pyplot(fig2)

st.subheader('Count of Pokémon by Primary Type')
fig3, ax3 = plt.subplots(figsize=(10, 7))
sns.countplot(data=df, y='Type 1', order=df['Type 1'].value_counts().index, palette='viridis',ax=ax3)
ax3.set_title('Count of Pokémon by Primary Type')
ax3.set_xlabel('Count')
ax3.set_ylabel('Type 1')
st.pyplot(fig3)

st.subheader('Top 10 Fastest Pokémon')
top_speed = df.sort_values(by='Speed',ascending=False).head(10)[['Name', 'Speed', 'Legendary']]
top_speed.reset_index(inplace=True)
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_speed, x='Speed', y='Name', hue='Legendary', palette='Set1', ax=ax4)
ax4.set_title("Top 10 Fastest Pokémon")
ax4.set_xlabel('Speed')
ax4.set_ylabel('Pokémon Name')
ax4.legend(title='Legendary Status')
st.pyplot(fig4)

st.subheader("Top10 Pokémon by Total Stats")
strongest = df.sort_values(by='Total', ascending=False).head(10)[['Name', 'Total', 'Legendary']]
strongest.reset_index(inplace=True)
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(data=strongest, x='Total',y='Name', hue='Legendary', palette='Set1',ax=ax5)
ax5.set_title("Top 10 Strongest Pokémon by Total Stats")
ax5.set_xlabel('Total Stats')
ax5.set_ylabel('Pokémon Name')
st.pyplot(fig5)

st.subheader("Legendary Pokémon Count by Type")
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.countplot(data=df, x='Legendary', hue='Type 1', palette='Set1',ax=ax6)
ax6.set_title("Legendary Pokémon Count by Type")
ax6.set_xlabel('Legendary Status')  
ax6.set_ylabel('Count')
st.pyplot(fig6)

st.subheader("Top 10 Pokémon by Total Attack")
df['total_attack'] = df['Attack'] + df['Sp_Atk']
best_attackers = df.sort_values(by='total_attack', ascending=False).head(10)[['Name', 'total_attack', 'Legendary']]
best_attackers.reset_index(inplace=True)
fig7, ax7 = plt.subplots(figsize=(10, 6))
sns.barplot(data=best_attackers, x='total_attack', y='Name', hue='Legendary', palette='Set1',ax=ax7)
ax7.set_title("Top 10 Pokémon by Total Attack")
ax7.set_xlabel('Total Attack')
ax7.set_ylabel('Pokémon Name')
st.pyplot(fig7)


st.subheader("Top 10 Pokémon by Total Defense")
df['total_defense'] = df['Defense'] + df['Sp_Def']
best_defenders = df.sort_values(by='total_defense', ascending=False).head(10)[['Name', 'total_defense', 'Legendary']]
best_defenders.reset_index(inplace=True)
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.barplot(data = best_defenders, x='total_defense', y='Name', hue='Legendary', palette='Set1',ax=ax8)
ax8.set_title("Top 10 Pokémon by Total Defense")
ax8.set_xlabel('Total Defense')
ax8.set_ylabel('Pokémon Name')
st.pyplot(fig8)
