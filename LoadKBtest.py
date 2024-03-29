#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:24:24 2024

@author: paulsevestre
"""

from rdflib import Graph

# Charger la base de données YAGO Tiny
test_graph = Graph(store="BerkeleyDB")
print("ok1")
test_graph.open("ftest.db",create=True)
print('accès à ftest.db OK')
test_graph.parse("/home/psevestre/YagotinyKB/yago-tiny50000.ttl", format="ttl")
print('test_graph.parse OK')
test_graph.commit()
test_graph.close()

