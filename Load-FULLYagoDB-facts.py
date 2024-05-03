#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:24:24 2024

@author: paulsevestre
"""

from rdflib import Graph

# Charger la base de données YAGO Tiny
yago_graph = Graph(store="BerkeleyDB")
print("ok1")
yago_graph.open("yago.db",create=True)
print('accès à yago.db OK')
yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny.ttl", format="ttl")
print('yago_graph.parse OK')
yago_graph.commit()
yago_graph.close()

