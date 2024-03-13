#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:15:04 2024

@author: paulsevestre
"""

from brick_graph import Graph
print('ok0')
# Initialiser une instance de Brick Graph avec BerkeleyDB comme backend de stockage
brick_graph = Graph("yago.db")
print('ok1')
# Charger le fichier RDF directement dans BerkeleyDB
brick_graph.load("/home/psevestre/YagotinyKB/yago-tiny.ttl", format="ttl")
print('ok2')
# Définir les préfixes pour les namespaces utilisés dans YAGO
brick_graph.bind("yago", "http://yago-knowledge.org/resource/")
print("ok3")
# Fonction pour trouver le type d'un mot donné
def trouver_type_mot(mot):
    # Requête SPARQL pour trouver le type du mot donné
    query = f"""
        SELECT DISTINCT ?type
        WHERE {{
            yago:{mot} rdf:type ?type .
        }}
    """

    # Exécuter la requête SPARQL sur la base de données BerkeleyDB
    results = brick_graph.query(query)

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
