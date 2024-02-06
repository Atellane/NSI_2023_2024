class Graphe():
	"""Implémente les graphes en python
	sommets: dict = {"nom_sommet": {"nom du sommet voisin": distance entre les deux sommets}}"""
	def __init__(self: object, sommets: dict) -> object:
		self.__sommets = sommets

	def __repr__(self: object) -> dict:
		return str(self.__sommets)

	def ajouter_arete(self: object, sommet_1: str, sommet_2: str, distance: int) -> None:
		"""Permet d'ajouter une arrête entre deux sommets exitants du graphe."""
		if sommet_1 in self.__sommets and sommet_2 in self.__sommets:
			self.__sommets[sommet_1][sommet_2] = distance
			self.__sommets[sommet_2][sommet_1] = distance
		else:
			raise ValueError(f"Les 2 sommets fournis sont sensés être des sommets déjà présents dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

	def ajouter_sommet(self: object, sommet: str) -> None:
		"""Permet d'ajouter un sommet non existants au graphe."""
		if not (sommet in self.__sommets):
			self.__sommets[sommet] = {sommet: 0}
		else:
			raise ValueError("Le sommet est déjà présent dans le graphe.\nPour l'instant, le graphe est le suivant :\n{self}")

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
			m_adjacence.append([])
			for sommet_b in liste_sommets:
				m_adjacence[index_sommet_a].append(self.distance(liste_sommets[index_sommet_a], sommet_b))
		return m_adjacence

if __name__ == "__main__":
	sommets: dict = {"UwU": dict(), "UwU2": dict()}
	graph: object = Graphe(sommets)
	print(graph)
	graph.ajouter_arete("UwU", "UwU2", 3)
	print(graph)
	print(graph.voisins("UwU"))
	print(graph.distance("UwU", "UwU2"))
	graph.ajouter_sommet("UwU3")
	print(graph.distance("UwU", "UwU3"))
	print(graph.matrice_adjacence())