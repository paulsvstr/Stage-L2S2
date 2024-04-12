from rdflib import Graph
yago_graph = Graph(store="BerkeleyDB")
yago_graph.open("yago.db")
print("yago.db bien open")

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
    results = yago_graph.query(query)
    print(results)
    # Récupérer et retourner le type du mot
    types = [row["type"] for row in results]
    return types

# Mot à rechercher
mot_a_rechercher = input() #"Strategy_video_game"  Vous pouvez changer le mot ici

# Trouver et afficher le type du mot
types = trouver_type_mot(mot_a_rechercher)
print(types)
if types:
    print(f"Le type de '{mot_a_rechercher}' est : {types}")
else:
    print(f"Le type de '{mot_a_rechercher}' n'a pas été trouvé dans la base de données YAGO Tiny.")