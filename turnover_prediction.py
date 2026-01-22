# Mini-portfolio RH / Machine Learning
# Objectif : prédire le turnover des employés

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# --------------------------
# 1️⃣ Création d'un dataset fictif
# --------------------------
np.random.seed(42)

n = 500
data = pd.DataFrame({
    'Age': np.random.randint(22, 60, n),
    'Anciennete': np.random.randint(0, 15, n),
    'Satisfaction': np.random.randint(1, 6, n),
    'Heures_Sup': np.random.randint(0, 20, n),
    'Promotion': np.random.choice([0,1], n, p=[0.8,0.2]),
    'Departement': np.random.choice(['RH','IT','Ventes','Marketing'], n),
})

# Création d'une variable cible (Turnover)
# Exemple : plus de risque si faible satisfaction et ancienneté courte
data['Turnover'] = ((data['Satisfaction'] < 3) & (data['Anciennete'] < 3)).astype(int)

# --------------------------
# 2️⃣ Analyse descriptive
# --------------------------
print("Statistiques descriptives :\n", data.describe())

# Corrélation
print("\nCorrélation avec Turnover :\n", data.corr()['Turnover'])

# Histogramme satisfaction
plt.figure(figsize=(6,4))
sns.histplot(data['Satisfaction'], bins=5, kde=False)
plt.title('Distribution de la satisfaction')
plt.show()

# --------------------------
# 3️⃣ Préparation pour ML
# --------------------------
# Variables numériques
X = data[['Age','Anciennete','Satisfaction','Heures_Sup','Promotion']]

# Target
y = data['Turnover']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --------------------------
# 4️⃣ Modélisation ML
# --------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Évaluation
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nMatrice de confusion:\n", confusion_matrix(y_test, y_pred))

# --------------------------
# 5️⃣ Interprétation métier
# --------------------------
coeff_df = pd.DataFrame({
    'Variable': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print("\nImportance des variables :\n", coeff_df)
