import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.tree import export_text


df = pd.read_csv('obesidad.csv', sep=",")


X = df[['Altura', 'Peso', 'IMC', 'ActividadFisica']]
y = df['CategoriaObesidad']


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
r = export_text(clf, feature_names=['Altura', 'Peso', 'IMC', 'ActividadFisica'])
print(r)

#tree.plot_tree(clf)

plt.figure(figsize=(10, 8), dpi=300)  
plot_tree(clf, feature_names=['Altura', 'Peso', 'IMC', 'ActividadFisica'], filled=True)
plt.show()