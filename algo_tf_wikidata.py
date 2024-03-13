#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:29:30 2024

@author: paulsevestre
"""
# Connexion à Wikidata
import requests

def fetch_wikidata(params):
    url = 'https://www.wikidata.org/w/api.php'
    try:
        return requests.get(url, params=params)
    except:
        return 'There was and error'
    
import string

#FONCTION D'ANALYSE DU MOT LE PLUS COMMUN DANS LES 
#DESCRIPTIONS WIKIDATA DES DIFFERENTS MOTS

def pt_commun(colonne) :
  dict = {}
  sgn_mots = [] #liste contenant des paires // ex : ['Lyon', 'ville de France']
  for mot in colonne :
    Ltemp = []
    Ltemp.append(mot)
    query = mot
    params = {
          'action': 'wbsearchentities',
          'format': 'json',
          'search': query,
          'language': 'en' }
    data = fetch_wikidata(params)
    data = data.json()
    data
    sgn = data['search'][0]['description']
    Ltemp.append(sgn)
    sgn_mots.append(Ltemp)
  for paire in sgn_mots :
    phrase = paire[1].split()
    for mot in phrase :
      mp = "".join([i for i in mot if i not in string.punctuation])
      mp = mp.lower()
      if mp not in dict :
        dict[mp] =1
      else :
        dict[mp] +=1
  max = 0
  L_max = []
  for keys in dict.keys() :
    if keys not in ['in','of','a','the','as','born','name','family','and'] :
      if dict[keys] == max :
        L_max.append(keys)
      if dict[keys] > max :
        L_max = []
        L_max.append(keys)
        max = dict[keys]

  print(L_max)
  
#TESTS SUR COLONNES DE MOTS

C1 = ['France','Spain','Italy','USA','Germany','UK']
C2 = ['Ronaldo','Messi','Zidane','Griezmann','Dembele','Pogba']
C3 = ['Ramos','Picasso','Salvador Dali']
C4 = ['Rennes','Lyon','Paris','mARSEILLE','Grenoble','Limoges','Roubaix','Nimes']
C5 = ['2010','2011','2012','2014','2015','2019']
ens_C = []
ens_C.append(C1)
ens_C.append(C2)
ens_C.append(C3)
ens_C.append(C4)
ens_C.append(C5)
for col in ens_C :
  print(col)
  pt_commun(col)
