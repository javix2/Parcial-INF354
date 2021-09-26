# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:32:42 2021

@author: javier
"""

from kanren import Relation, facts,var,run, conde,lall
from kanren.constraints import neq
x = var()
es_padre = Relation()
facts(es_padre,("Fausto","Javier"),
              ("Fausto","JuanC"),
              ("Tomasa","Javier"),
              ("Fausto","lola"),
              ("Tomasa","lola"),
              ("Tomasa","JuanC"),
              ("Bartolome","Tomasa"),
              ("Bartolome","Martha"),
              ("Salome","Tomasa"),
              ("Salome","Martha"),
              ("Martha","Sergio"),
              ("Jorge","Lorena"),
              ("Victor","Jorge"),
              ("Victor","Fausto"))

def es_abueloa(A,B):
    X = var()
    return conde((es_padre(A,X),es_padre(X,B)))

def es_hermanoa(A,B):
    X = var()
    return conde((es_padre(X,A),es_padre(X,B), neq(A,B)))
                 
def es_tioa(A,B):
    X = var()
    return conde((es_hermanoa(A,X), es_padre(X,B), neq(A,B)))

def es_primo(A,B):
    X = var()
    Y = var()
    return lall(es_padre(X,A),es_padre(Y,B), es_hermanoa(X,Y) ,neq(X,Y))

def es_hijo(A,B):
    return lall(es_padre(B,A))


#print(run(3, x, es_padre("Fausto", x)))
print(run(5, x, es_abueloa("Salome", x)))
#print(run(4, x, es_hermanoa("lola", x)))
#print(run(8, x, es_tioa("Martha", x)))
#print(run(8, x, es_primo("Javier", x)))
#print(run(8, x, es_hijo("Martha", x)))




