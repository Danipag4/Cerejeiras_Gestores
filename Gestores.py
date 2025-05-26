import streamlit as st 
import pandas as pd 
import plotly_express as px 
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#color = st.color_picker("Pick A Color", "#00f900")
#st.write("The current color is", color)

df = pd.read_csv("Teste.csv", sep=",")


df=df.sort_values("Nome")

df["Colab"] = df["Nome"]
df["Compet"] = df["Competencia"]
df["Setor"] = df["Nivel avaliação"]
df["Setorial"] = df["Nivel avaliação"]
df["Comenta"] = df["Comentário"]


st.write("""
# Cerejeiras - Análise de Competências
""" )
aval = ["Autoavaliação","Gestor","Pares","Liderados"]

Nome = st.sidebar.selectbox("Colaboradores",df["Colab"].unique())

df_filtered = df[df["Colab"] == Nome]
#df_filtered
df_Média = df_filtered.groupby("Compet")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_Média

aval = ["Autoavaliação","Gestor","Pares","Liderados"]
#----------------------------------------------------------------------

Avaliado = str(Nome)
st.write("""
## Competências
""" ), Avaliado

fig_comp = px.bar(df_Média, y=aval, x="Compet", barmode='group', color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_comp.update_layout(xaxis_title="Competências", yaxis_title="Médias")

fig_comp

#df_filtered

#-------------------------------------------------------------------------------------------

st.write("""
## Análise das Perguntas
""" ), Nome

aval1 = ["Liderados","Pares", "Gestor", "Autoavaliação"]

#df["CompetUniqx"] = df_filtered["Competencia"]
#df["CompetUniqx"]
df_CompetUniq = df_filtered["Competencia"].dropna().reset_index(drop = True)

unica_Competencia = st.selectbox("Escolha a Competência",df_CompetUniq.unique(),index=1)

df_filtered2 = df_filtered[df["Compet"] == unica_Competencia]

fig_Perg = px.bar(df_filtered2, y="Pergunta", x=aval1, orientation="h", barmode='group', color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_Perg.update_layout(xaxis_title="Médias", yaxis_title="Perguntas")
fig_Perg

coment = st.checkbox("Comentários")
df_filtered3 = df_filtered[df["Comentário"] == "Sim"]
#df_Comenta = df_filtered[df["Compet"] == "Comentário"].reset_index()
#df_Comenta = df_filtered["Comentários"].dropna().reset_index(drop = True)
#df_Comenta
if coment:
    #df_filtered3
  
    df_coment = df_filtered3.iloc[:,6]
    df_coment




#-----------------------------------------------------------------------------------------

st.write("""
## Desempenho Geral por Competência no Setor
""" )
#col1, col2 = st.columns(2)

#with col1:
#Compet_Setor = st.selectbox("Defina o Setor",df["Nivel avaliação"].unique(),index=1)
#df_filtered4 = df[df["Setor"] == Compet_Setor]
#df_Comp = df_filtered4["Compet"].dropna().reset_index(drop = True)

#with col2:
Compet_Desemp = st.selectbox("Defina a Competência",df["Compet"].unique(),index=1)
df_filtered5 = df[df["Compet"] == Compet_Desemp]

df_MédiaGeral = df_filtered5.groupby("Nome")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_MédiaGeral

fig_DesenvGeral = px.bar(df_MédiaGeral, y=aval, x="Nome", barmode='group',color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_DesenvGeral.update_layout(xaxis_title="Colaboradores do Setor", yaxis_title="Médias")
fig_DesenvGeral

#---------------------------------------------------------------------------------

st.write("""
## Desempenho Carel das Competência por Setor
""" )
#df["Nivel avaliação"]
#df["Setorial"]

unico_Setor = st.selectbox("Defina o Setor",df["Setorial"].unique())

#setorial = st.selectbox("Defina o Setor",df["Nivel avaliação"].unique(),index=1)

df_filtered7 = df[df["Setor"] == unico_Setor]
#df_filtered7



df_MédiaSetor = df_filtered7.groupby("Competencia")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_MédiaSetor

fig_DesenvSetor = px.bar(df_MédiaSetor, y=aval, x="Competencia", barmode='group',color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_DesenvSetor.update_layout(xaxis_title="Competência", yaxis_title="Médias")
fig_DesenvSetor

#---------------------------------------------------------------------------------
