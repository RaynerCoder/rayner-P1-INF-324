import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn import tree
from sklearn.tree import export_text
from sklearn.preprocessing import LabelEncoder


df = pd.read_excel('obesidad_estetizado.xlsx')


encoder = LabelEncoder()
df['Edad_'] = encoder.fit_transform(df['Edad'])
df['Sexo_'] = encoder.fit_transform(df['Sexo'])
df['Altura_'] = encoder.fit_transform(df['Altura'])
df['IMC_'] = encoder.fit_transform(df['IMC'])
df['ActividadFisica_'] = encoder.fit_transform(df['ActividadFisica'])


X = df[['Edad_', 'Sexo_', 'Altura_', 'Peso', 'IMC_', 'ActividadFisica_']]
y = df['CategoriaObesidad']


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
r = export_text(clf, feature_names=['Edad_', 'Sexo_','Altura_', 'Peso', 'IMC_', 'ActividadFisica_'])
print(r)

#tree.plot_tree(clf)

plt.figure(figsize=(10, 8), dpi=300)  
plot_tree(clf, feature_names=['Edad_', 'Sexo_','Altura_', 'Peso', 'IMC_', 'ActividadFisica_'], filled=True)
plt.show()