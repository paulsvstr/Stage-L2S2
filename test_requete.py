#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:47:02 2024

@author: paulsevestre
"""

from rdflib import Graph
test_graph = Graph(store="BerkeleyDB")
print("commande graph... ok")
test_graph.open("ftest.db")
print("ftest bien open")

def trouver_type_mot(mot):
    # Requête SPARQL pour trouver le type du mot donné
    query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX yago: <http://yago-knowledge.org/resource/>
        
        SELECT DISTINCT ?type
        WHERE {
            ?subject ?predicate ?type .
        }
    """

    # Exécuter la requête SPARQL
    results = test_graph.query(query)

    # Récupérer et retourner le type du mot
    types = [row["type"] for row in results]
    return types

# Mot à rechercher
mot_a_rechercher = "Strategy_video_game"  # Vous pouvez changer le mot ici

# Trouver et afficher le type du mot
types = trouver_type_mot(mot_a_rechercher)
if types:
    print(f"Le type de '{mot_a_rechercher}' est : {types}")
else:
    print(f"Le type de '{mot_a_rechercher}' n'a pas été trouvé dans la base de données YAGO Tiny.")