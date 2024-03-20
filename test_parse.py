#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:43:37 2024

@author: paulsevestre
"""
import time
from rdflib import Graph

yago_graph = Graph()

start = time.time()

yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny50000.ttl", format="ttl")

end = time.time()

print("Yago graph parse bien executed")

elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.2}s')