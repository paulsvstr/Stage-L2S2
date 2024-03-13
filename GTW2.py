#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:18:07 2024

@author: paulsevestre
"""

from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery

# Charger la base de données YAGO Tiny depuis un fichier Turtle
print("tout est bien importén et modif #1")

yago_graph = Graph()

print("Graph() executed")

yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny.ttl", format="ttl")

print("Yago graph parse bien executed")

# Définir les préfixes pour les namespaces utilisés dans YAGO
YAGO = Namespace("http://yago-knowledge.org/resource/")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

print("pref bien def")

def trouver_type_mot(mot):
    # Requête SPARQL pour trouver le type du mot donné
    query = prepareQuery(
        """
        SELECT DISTINCT ?type
        WHERE {
            YAGO:%s rdf:type ?type .
        }
        """ % mot,
        initNs={"YAGO": YAGO, "RDF": RDF}
    )

    # Exécuter la requête SPARQL
    results = yago_graph.query(query)

    # Récupérer et retourner le type du mot
    types = [row.type for row in results]
    return types

# Mot à rechercher
mot_a_rechercher = "Elvis_Presley"  # Vous pouvez changer le mot ici

# Trouver et afficher le type du mot
types = trouver_type_mot(mot_a_rechercher)
if types:
    print(f"Le type de '{mot_a_rechercher}' est : {types}")
else:
    print(f"Le type de '{mot_a_rechercher}' n'a pas été trouvé dans la base de données YAGO Tiny.")
