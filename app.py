import streamlit as st
import pandas as pd
import datetime

# Titre Page général
cycliste_link="data/fontenay-cyclistes.xlsx"
pietons_link="data/fontenay-pietons.xlsx"

cycliste_data=pd.read_excel(cycliste_link)
pietons_data=pd.read_excel(pietons_link)

add_selectbox = st.sidebar.selectbox("Choisir la rubrique",("Infos","Piétons","Cycliste"))

if add_selectbox=="Infos":
    st.title('Accident de la route - Fontenay-sous-bois')

    # Nombre d'accidents
    st.write("Nombre d'accidents de piétons",pietons_data.shape[0],"dont",75,"mineurs")
    st.write("Nombre d'accidents à vélo:",cycliste_data.shape[0],"dont",13,"mineurs")

if add_selectbox=="Cycliste":
    st.title("Accidents cyclistes")
    #Carte
    st.header('Carte')
    latlong = cycliste_data[["Latitude","Longitude"]]
    latlong=latlong.dropna()
    latlong.rename(columns={"Latitude":"latitude"},inplace=True)
    latlong.rename(columns={"Longitude":"longitude"},inplace=True)
    latlong["latitude"]=pd.to_numeric(latlong["latitude"])
    latlong["longitude"]=pd.to_numeric(latlong["longitude"])
    st.map(latlong)

    st.header('Statistiques')
    #Accidents par sexe
    st.caption("Nombres d'accidents hommes/femmes")
    cat_personne = cycliste_data.groupby(["Sexe"])["Catégorie de personne"].count()
    st.bar_chart(cat_personne)

    #Accidents par gravité
    st.caption("Nombres d'accidents en fonction de la gravité")
    cat = cycliste_data.groupby(["Gravité"])["Catégorie de personne"].count()
    st.bar_chart(cat)


    #Accidents par année
    st.caption("Nombres d'accidents par année")
    cycliste_data["year"]=pd.DatetimeIndex(cycliste_data['Date']).year
    year_date = cycliste_data.groupby(["year"])["Catégorie de personne"].count()
    st.line_chart(year_date)
    with st.expander("See explanation"):
     st.write("Attention les données ne prennent pas en compte l'année 2022")

    st.header('Tableau')
    agree = st.checkbox("Voir le tableau")
    if agree:
        st.write(cycliste_data)

if add_selectbox=="Piétons":
    st.title("Accidents piétons")
    #Carte
    st.header('Carte')
    latlong_pietons = pietons_data[["Latitude","Longitude"]]
    latlong_pietons=latlong_pietons.dropna()
    latlong_pietons.rename(columns={"Latitude":"latitude"},inplace=True)
    latlong_pietons.rename(columns={"Longitude":"longitude"},inplace=True)
    latlong_pietons["latitude"]=pd.to_numeric(latlong_pietons["latitude"])
    latlong_pietons["longitude"]=pd.to_numeric(latlong_pietons["longitude"])
    st.map(latlong_pietons)

    st.header('Statistiques')
    #Accidents par sexe
    st.caption("Nombres d'accidents hommes/femmes")
    cat_personne = pietons_data.groupby(["Sexe"])["Catégorie de personne"].count()
    st.bar_chart(cat_personne)

    #Accidents par gravité
    st.caption("Nombres d'accidents en fonction de la gravité")
    cat = pietons_data.groupby(["Gravité"])["Catégorie de personne"].count()
    st.bar_chart(cat)

    #Accidents par type de véhicule
    st.caption("Nombres d'accidents en fonction du véhicule qui a heuté le piéton")
    vehicule = pietons_data.groupby(["Véhicule qui a heurté le piéton"])["Catégorie de personne"].count()
    st.bar_chart(vehicule)

    #Accidents par année
    st.caption("Nombres d'accidents par année")
    pietons_data["year"]=pd.DatetimeIndex(pietons_data['Date']).year
    year_date = pietons_data.groupby(["year"])["Catégorie de personne"].count()
    st.line_chart(year_date)
    with st.expander("See explanation"):
     st.write("Attention les données ne prennent pas en compte l'année 2022")

    st.header('Tableau')
    agree = st.checkbox("Voir le tableau")
    if agree:
        st.write(pietons_data)
