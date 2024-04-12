#load+parseKBTEST
from rdflib import Graph

# Charger la base de données YAGO Tiny
test_graph = Graph(store="BerkeleyDB")
print("ok1")
test_graph.open("ftest.db",create=True)
print('accès à ftest.db OK')
test_graph.parse("/home/psevestre/YagotinyKB/yago-tiny50000.ttl", format="ttl")
print('test_graph.parse OK')
test_graph.commit()
#test_graph.close()

def trouver_type_mot(mot):
    # Requête SPARQL pour trouver le type du mot donné
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX yago: <http://yago-knowledge.org/resource/>
        
        SELECT DISTINCT ?type
        WHERE {{
            yago:{mot} rdf:type ?type.
        }}
    """

    # Exécuter la requête SPARQL
    results = test_graph.query(query)

    # Récupérer et retourner le type du mot
    types = [row["type"] for row in results]
    return types

# Mot à rechercher
mot_a_rechercher = input()  # Vous pouvez changer le mot ici

# Trouver et afficher le type du mot
types = trouver_type_mot(mot_a_rechercher)
if types:
    print(f"Le type de '{mot_a_rechercher}' est : {types}")
else:
    print(f"Le type de '{mot_a_rechercher}' n'a pas été trouvé dans la base de données YAGO Tiny.")
