import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Calculez votre retour sur investissement potentiel")

# Entrée utilisateur pour le nombre de factures avec un slider
nombre_factures = st.slider("Sélectionnez le nombre de factures fournisseurs reçues par an", min_value=0, max_value=10000, value=100)

# Coûts au format papier par facture
cout_saisie_papier = 1.40
cout_validation_papier = 5.40
cout_archivage_papier = 1.50
cout_global_papier = cout_saisie_papier + cout_validation_papier + cout_archivage_papier

# Coûts au format électronique par facture
cout_saisie_electronique = 0.80
cout_validation_electronique = 0.40
cout_archivage_electronique = 0.80
cout_global_electronique = cout_saisie_electronique  + cout_archivage_electronique

# Calcul des coûts totaux en fonction du nombre de factures
cout_total_papier = cout_global_papier * nombre_factures
cout_total_electronique = cout_global_electronique * nombre_factures

# Calcul de l'économie potentielle
economie_potentielle = cout_total_papier - cout_total_electronique

# Création d'un DataFrame pour afficher les résultats sous forme de tableau
data = {
    "Type de coût": ["Coût au format papier", "Coût au format électronique", "Économie potentielle"],
    "Valeur": [cout_total_papier, cout_total_electronique, economie_potentielle]
}
df = pd.DataFrame(data)

# Affichage des résultats sous forme de tableau
st.table(df)

# Affichage des coûts par facture
st.write("Coûts par facture :")
st.write(f"Coût au format papier : {cout_global_papier} EUR")
st.write(f"Coût au format électronique : {cout_global_electronique} EUR")

