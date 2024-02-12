import warnings

class Graphe():
	"""Implémente les graphes en python à partir d'un dictionnaire contenant les sommets, leurs voisins et la distance avec leurs voisins ou une liste de sommets ou
	la matrice d'adjacence
	sommets: dict = {"nom_sommet": {"nom_sommet": distance avec lui même, "nom du sommet voisin": distance entre les deux sommets}} ou
	sommets: list = [["nom de sommet 1", distance avec sommet 1, distance avec sommet 2], ["nom de sommet 2", distance avec sommet 1, distance avec sommet 2]]
	sommet: list  = ["sommet 1", "sommet 2"]"""
	def __init__(self: object, sommets: dict or list = None) -> object:
		self.__sommets = dict()
		if sommets != None:
			if type(sommets) == list and self.__contient_un_sous_tableau(sommets):
				# Gère la construction du graphe si sommets est une matrice d'adjacence
				liste_des_sommets: list = []
				for element in sommets:
					liste_des_sommets.append(element[0])
					self.ajouter_sommet(element[0])
					for i in range(1, len(self.__sommets)+1):
						if element[i] != float("inf"):
							self.ajouter_arete(element[0], liste_des_sommets[i-1], element[i])
			elif type(sommets) == list:
				# Gère la construction du graphe si sommets est une liste des sommets
				for element in sommets:
					self.ajouter_sommet(element)
			else:
				# Gère la construction du graphe si sommets est un dictionnaire
				self.__sommets = sommets

	def __repr__(self: object) -> dict:
		return str(self.__sommets)

	def __contient_un_sous_tableau(self: object, tab: list) -> bool:
		for element in tab:
			if isinstance(element, list):
				return True
		return False

	def obtenir_sommet(self: object) -> dict:
		return self.__sommets

	def nombre_de_sommet(self: object) -> int:
		return len(self.__sommets)

	def ajouter_arete(self: object, sommet_1: str, sommet_2: str, distance: float) -> None:
		"""Permet d'ajouter une arrête entre deux sommets exitants du graphe."""
		if sommet_1 in self.__sommets and sommet_2 in self.__sommets:
			self.__sommets[sommet_1][sommet_2] = float(distance)
			self.__sommets[sommet_2][sommet_1] = float(distance)
		else:
			raise ValueError(f"Les 2 sommets fournis sont sensés être des sommets déjà présents dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

	def ajouter_sommet(self: object, sommet: str, debug: bool=False) -> None:
		"""Permet d'ajouter un sommet non existants au graphe."""
		if not (sommet in self.__sommets):
			self.__sommets[sommet] = {sommet: 0.0}
		else:
			if debug:
				warnings.warn(f"Le sommet est déjà présent dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

	def voisins(self: object, sommet: str) -> dict:
		"""Renvoie un dictionnaire avec la liste des voisins."""
		if sommet in self.__sommets:
			return self.__sommets[sommet]
		else:
			raise ValueError(f"Le sommet fournis est sensé être un sommets déjà présents dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

	def distance(self: object, sommet_1: str, sommet_2: str) -> float:
		"""Renvoie la distance entre les 2 sommets s'ils sont voisins, sinon, renvoie l'infini"""
		if sommet_1 in self.__sommets and sommet_2 in self.__sommets:
			if sommet_1 in self.__sommets[sommet_2].keys():
				return float(self.__sommets[sommet_2][sommet_1])
			else:
				return float("inf")
		else:
			raise ValueError(f"Les 2 sommets fournis sont sensés être des sommets déjà présents dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

	def matrice_adjacence(self: object) -> list:
		"""Construis la matrice d'adjacence du graphe et la renvoie"""
		sommets: dict = self.__sommets
		liste_sommets: list = []
		m_adjacence: list = []
		for sommet in sommets.keys():
			liste_sommets.append(sommet)
		for index_sommet_a in range(len(liste_sommets)):
			m_adjacence.append([liste_sommets[index_sommet_a]])
			for sommet_b in liste_sommets:
				m_adjacence[index_sommet_a].append(self.distance(liste_sommets[index_sommet_a], sommet_b))
		return m_adjacence

	def parcours_en_profondeur(self: object, sommet_depart: str, deja_visite: list=[]) -> list:
		if len(deja_visite) == (len(self.__sommets) - 1):
			return [sommet_depart]
		else:
			deja_visite.append(sommet_depart)
			ordre_de_visite = []
			ordre_de_visite.append(sommet_depart)
			voisins: list = list(self.voisins(sommet_depart))
			for voisin in voisins:
				if voisin not in deja_visite:
					ordre_de_visite.extend(self.parcours_en_profondeur(voisin, deja_visite))
			return ordre_de_visite


	def dijkstra(self: object, sommet_depart: str) -> dict:
		"""Implémente l'algorithme de Dijkstra pour trouver la distance de chaque sommet à partir d'un sommet de départ."""
		distances = {sommet: (float('inf'), None) for sommet in self.__sommets}
		distances[sommet_depart] = (0.0, None)

		sommets_non_traites = set(self.__sommets)

		while sommets_non_traites:
			sommet_courant = min(sommets_non_traites, key=lambda s: distances[s][0])
			sommets_non_traites.remove(sommet_courant)

			for voisin, poids in self.voisins(sommet_courant).items():
				nouvelle_distance = distances[sommet_courant][0] + poids
				if nouvelle_distance < distances[voisin][0]:
					distances[voisin] = (nouvelle_distance, sommet_courant)

		return distances

if __name__ == "__main__":
	sommets: dict = {"UwU": {"UwU": 0.0}, "UwU2": {"UwU2": 0.0}}
	graph: Graphe = Graphe(sommets)
	print(graph)
	graph.ajouter_arete("UwU", "UwU2", 3)
	print(graph)
	print(graph.voisins("UwU"))
	print(graph.distance("UwU", "UwU2"))
	graph.ajouter_sommet("UwU3")
	print(graph.distance("UwU", "UwU3"))
	print(graph.matrice_adjacence())
	m_adj = graph.matrice_adjacence()
	print(m_adj)
	graph_matrice_adjacence: Graphe = Graphe(m_adj)
	assert str(graph) == str(graph_matrice_adjacence), "problème dans la construction du graph à partir de la matrice d'adjacence"
	graph_liste_sommets: Graphe = Graphe(["sommet_1", "sommet_2", "j'ai_pas_d'idee_de_nom_de_sommet"])
	print(graph_liste_sommets)
	graph_vide: Graphe = Graphe()
	graph.ajouter_arete("UwU", "UwU3", 2)
	graph.ajouter_sommet("UwU4")
	graph.ajouter_arete("UwU2", "UwU4", 4)
	print(graph.parcours_en_profondeur("UwU"))
	print(graph.dijkstra("UwU"))
	print(graph.voisins("UwU4"))