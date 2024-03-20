#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:43:37 2024

@author: paulsevestre
"""

from rdflib import Graph

yago_graph = Graph()


yago_graph.parse("/home/psevestre/YagotinyKB/yago-tiny1000.ttl", format="ttl")

print("Yago graph parse bien executed")