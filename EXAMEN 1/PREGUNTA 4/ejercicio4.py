"""
4. Con el uso de librerías en PYTHON, construya la dependencia de Abuelos, 
tios, padres, primos e hijos de su familia.
"""

import toolz
from kanren import Relation, facts, var, run, conde


def Tios(tio, hijo):
    p = var()
    a = var()
    return conde((padre_hijo(a, tio), padre_hijo(a, p), Padres(p, hijo)))


def Abuelos(abuelo, hijo):
    p = var()
    return conde((padre_hijo(abuelo, p), Padres(p, hijo)))


def Padres(padre, hijo):
    return conde([padre_hijo(padre, hijo)])


def Primos(primo, hijo):
    p = var()
    a = var()
    t = var()
    return conde((padre_hijo(t, primo), padre_hijo(a, t), padre_hijo(a, p), Padres(p, hijo)))


def Hijos(padre, hijo):
    return conde([padre_hijo(padre, hijo)])


def Hermanos(hermano, hijo):
    p = var()
    return conde((padre_hijo(p, hermano), Padres(p, hijo))) 


def NoInterseccion(r1, r2):
    conjunto1 = set(r1)
    conjunto2 = set(r2)    
    r2 = conjunto1.symmetric_difference(conjunto2)
    lista = list(r2)
    r2 = "(" + ", ".join("'" + str(elem) + "'" for elem in lista) + ")"
    return r2


print("----------------------------------------------------------")


padre_hijo = Relation()

#La relacion es PADRE - HIJO (padre_hijo)

facts(padre_hijo,
    ("Gutember", "Alcides"),
    ("Gutember", "Alex"),
    ("Benjamin", "Eliab"),
    ("Benjamin", "Eliasim"),
    ("Francisco", "Gutember"),
    ("Francisco", "Benjamin"),
    ("Francisco", "Dario"),
    ("Carlos", "Cecilia"),
    ("Carlos", "Elvira"),
    ("Cecilia", "Alcides"),
    ("Cecilia", "Alex"),
    ("Elvira", "Anahi"),
    ("Noemi", "Eliab"),
    ("Noemi", "Eliasim"),
    ("Angela", "Gutember"),
    ("Angela", "Benjamin"),
    ("Angela", "Dario"),
)


v = var()
susHijosDe = var()
hijo = "Alcides"


#Para hallar la dependencia de padres
r1 = run(0, v, Padres(v, hijo))
print("Padres  :", r1) 
print("----------------------------------------------------------")


#Para hallar la dependencia de tios
r2 = run(0, v, Tios(v, hijo), results_filter=toolz.unique)
r2 = NoInterseccion(r1, r2)
print("Tios    :", r2) 
print("----------------------------------------------------------")


#Para hallar la dependencia de abuelos
r3 = run(0, v, Abuelos(v, hijo))
print("Abuelos :", r3) 
print("----------------------------------------------------------")


#Para hallar la dependencia de hermanos
r4 = run(0, v, Hermanos(v, hijo))
#Para hallar la dependencia de primos
r5 = run(0, v, Primos(v, hijo), results_filter=toolz.unique)
r5 = NoInterseccion(r4, r5)
print("Primos  :", r5) 
print("----------------------------------------------------------")


#Para hallar la dependencia de hijos
r6 = run(0, v, Hijos(susHijosDe,v), results_filter=toolz.unique)
print("Hijos   :", r6)
print("----------------------------------------------------------")




