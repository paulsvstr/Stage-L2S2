#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:09:26 2024

@author: paulsevestre
"""
from rdflib import Graph
print('programme bien lancé et modif')
# Charger la base de données YAGO Tiny
yago_graph = Graph(store="BerkeleyDB")
print("commande graph... ok")
yago_graph.open("yago.db",create=True)
print('accès à yagodb OK')
yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny.ttl", format="ttl")
print('yago_graph.parse OK')

def trouver_type_mot(mot):
    # Requête SPARQL pour trouver le type du mot donné
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        
        SELECT DISTINCT ?type
        WHERE {{
            yago:{mot} rdf:type ?type.
            OPTIONAL {{ yago:{mot} <http://yago-knowledge.org/resource/birthDate> ?date. }}
        }}
    """

    # Exécuter la requête SPARQL
    results = yago_graph.query(query)

    # Récupérer et retourner le type du mot
    types = [row["type"] for row in results]
    return types

# Mot à rechercher
mot_a_rechercher = "Elvis_Presley"  # Vous pouvez changer le mot ici

# Trouver et afficher le type du mot
types = trouver_type_mot(mot_a_rechercher)
if types:
    print(f"Le type de '{mot_a_rechercher}' est : {types}")
else:
    print(f"Le type de '{mot_a_rechercher}' n'a pas été trouvé dans la base de données YAGO Tiny.")

