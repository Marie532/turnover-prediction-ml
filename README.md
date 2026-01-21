# turnover-prediction-ml
Mini-projet Data Science : prédiction du turnover des employés
# 📊 Prédiction du Turnover des Employés – Mini Projet Data Science

## 🎯 Objectif du projet
Ce projet a pour objectif de construire un **modèle de Machine Learning** permettant de **prédire le turnover des employés** à partir de données RH fictives.

Ce projet a été réalisé dans un cadre **pédagogique**, afin de démontrer les bases de la Data Science et du Machine Learning.

---

## 🧠 Problématique métier
Le turnover représente un enjeu majeur pour les entreprises :
- coûts de recrutement
- perte de compétences
- impact sur la performance des équipes

👉 L’objectif est d’identifier les **facteurs influençant le départ des employés**.

---

## 🗂️ Données
Les données sont **générées artificiellement** et comprennent :
- Âge
- Ancienneté
- Satisfaction au travail (1 à 5)
- Heures supplémentaires
- Promotion (oui/non)
- Département
- Variable cible : **Turnover (0 = reste, 1 = quitte)**

---

## 🔍 Analyse exploratoire
- Analyse descriptive des variables
- Étude de la corrélation avec le turnover
- Visualisation de la distribution de la satisfaction

---

## 🤖 Modélisation
- Séparation train / test
- Modèle utilisé : **Régression Logistique**
- Évaluation :
  - Matrice de confusion
  - Classification report (précision, rappel, F1-score)

---

## 📈 Interprétation
Les coefficients du modèle permettent d’identifier les variables ayant le plus d’impact sur le turnover, notamment :
- la satisfaction
- l’ancienneté
- les heures supplémentaires

---

## 🛠️ Technologies utilisées
- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn

---

## 🚀 Conclusion
Ce projet démontre la mise en œuvre complète d’un **pipeline Data Science** :
- création des données
- analyse
- modélisation
- interprétation métier

Il s’inscrit dans une démarche de **montée en compétences en Data Science / IA**.
sns.boxplot(x='Turnover', y='Satisfaction', data=data)

