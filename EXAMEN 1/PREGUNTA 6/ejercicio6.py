import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.tree import export_text


# Load libraries

from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('obesidad.csv', sep=",")


encoder = LabelEncoder()
df['Sexo_'] = encoder.fit_transform(df['Sexo'])


X = df[['Edad', 'Sexo_', 'Altura', 'Peso', 'IMC', 'ActividadFisica']]
y = df['CategoriaObesidad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Se crea un modelo de árbol de decisión utilizando Scikit-learn

#1) Crear objeto clasificador de arbol de decision
clf = DecisionTreeClassifier()

#2) Entrenar clasificador de arbol de decision
clf = clf.fit(X_train,y_train)

#3) Predecir la respuesta para el conjunto de datos de prueba
y_pred = clf.predict(X_test)


print("Precision del modelo: ",metrics.accuracy_score(y_test, y_pred))
print("\n==============ARBOL DE DECISION==============")

#Mostramos el arbol de decision
columns = ['Edad', 'Sexo_', 'Altura', 'Peso', 'IMC', 'ActividadFisica']

r = export_text(clf, feature_names=columns)
print(r)

plt.figure(figsize=(10, 8), dpi=300)  
plot_tree(clf, feature_names=columns, filled=True)
plt.show()

