import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv('obesidad.csv')
print("\n-------------------------------------MI CONJUNTO DE DATOS-------------------------------------\n")
print(df)


#SE APLICA ONEHOTENCODER A DOS COLUMNAS DE MI DATASET

#Inicializamos LabelEncoder y OneHotEncoder
label_encoder = LabelEncoder()
onehot_encoder = OneHotEncoder()

# 1) Aplicamos LabelEncoder a la columna Sexo
df['Sexo_encoder'] = label_encoder.fit_transform(df['Sexo'])

# 2) Aplicamos LabelEncoder a la columna CategoriaObesidad
df['CategoriaObesidad_encoder'] = label_encoder.fit_transform(df['CategoriaObesidad'])

#Aplicamos OneHotEncoder a las etiquetas generadas por LabelEncoder
sexo_encoder = df['Sexo_encoder'].values.reshape(-1, 1)
categoriaObesidad_encoder = df['CategoriaObesidad_encoder'].values.reshape(-1, 1)
onehotEncoder1_sexo = onehot_encoder.fit_transform(sexo_encoder)
onehotEncoder2_categoriObesidad = onehot_encoder.fit_transform(categoriaObesidad_encoder)

#Convertimos las salidas de OneHotEncoder a un DataFrame de pandas
df1 = pd.DataFrame(onehotEncoder1_sexo.toarray(), columns=['Sexo_F', 'Sexo_M'])
df2 = pd.DataFrame(onehotEncoder2_categoriObesidad.toarray(), columns=['PesoBajo', 'PesoNormal', 'ExcesoPeso', 'Obeso'])

#Concatenamos el DataFrame original con el DataFrame de características codificadas
df = pd.concat([df, df1], axis=1)
df = pd.concat([df, df2], axis=1)

#Eliminamos las columnas originales que ya han sido codificadas
df.drop(['Sexo', 'Sexo_encoder', 'CategoriaObesidad', 'CategoriaObesidad_encoder'], axis=1, inplace=True)

pd.set_option('display.max_columns', None)

print("\n----------------------DESPUES DE APLICAR ONEHOTENCODER----------------------\n")
print(df)



#SE APLICA ESCALADO, NORMALIZACION Y  SIMPLEIMPUTER DE MI DATASET

# 3) SimpleImputer
imputador = SimpleImputer(strategy='mean')
df_imputado = pd.DataFrame(imputador.fit_transform(df[['Altura', 'Peso']]), columns=['Altura', 'Peso'])
df_eliminar = df.drop(['Altura', 'Peso'], axis=1)
df = pd.concat([df_imputado, df_eliminar], axis=1)




# 4) Normalizer
normalizador = Normalizer()
df_normalizado = pd.DataFrame(normalizador.fit_transform(df_imputado), columns=['Altura', 'Peso'])
df_eliminar = df.drop(['Altura', 'Peso'], axis=1)
df = pd.concat([df_normalizado, df_eliminar], axis=1)



# 5) Escalado
escalador = StandardScaler()
df_escalado = pd.DataFrame(escalador.fit_transform(df_normalizado), columns=['Altura', 'Peso'])
df_eliminar = df.drop(['Altura', 'Peso'], axis=1)
df = pd.concat([df_escalado, df_eliminar], axis=1)



# Mostramos el DataFrame final
print("\n------------------DESPUES DE APLCIAR ESCALADO, IMPUTER, NORMALIZER------------------\n")
print(df)


