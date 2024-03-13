from rdflib import Graph, Namespace
from rdflib.plugins.stores import sparqlstore
from rdflib.plugins.stores.sparqlstore import SPARQLStore
print("ok")
# Initialiser un objet Graph avec BerkeleyDB comme backend de stockage
store = SPARQLStore('berkeley', config = {'dataset_path': 'yago.db'})
rdf_graph = Graph(store)
print("ok")
# Définir les préfixes pour les namespaces utilisés dans YAGO
YAGO = Namespace("http://yago-knowledge.org/resource/")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
print("ok")
# Fonction pour charger le fichier RDF dans BerkeleyDB
def charger_rdf_dans_berkeleydb(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Ignorer les lignes de commentaire et les lignes vides
            if not line.startswith("#") and line.strip():
                rdf_graph.parse(data=line, format="ttl")
print("ok")
# Charger le fichier RDF directement dans BerkeleyDB
charger_rdf_dans_berkeleydb("yago-tiny.ttl")

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
    results = rdf_graph.query(query)

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
