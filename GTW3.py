#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:00:10 2024

@author: paulsevestre
"""

from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery
print("ok0")

def trouver_type_mot(mot):
    # Créer un nouvel objet Graph
    yago_graph = Graph()
    print("ok1")
    # Charger uniquement les triples pertinents pour la requête
    yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny.ttl", format="ttl", publicID=Namespace("http://yago-knowledge.org/resource/{}".format(mot)))
    print("ok2")
    # Définir les préfixes pour les namespaces utilisés dans YAGO
    YAGO = Namespace("http://yago-knowledge.org/resource/")
    RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

    # Requête SPARQL pour trouver le type du mot donné
    query = prepareQuery(
        """
        SELECT DISTINCT ?type
        WHERE {
            ?s rdf:type ?type .
        }
        """,
        initNs={"YAGO": YAGO, "RDF": RDF}
    )

    # Exécuter la requête SPARQL sur le sous-graphe chargé
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
