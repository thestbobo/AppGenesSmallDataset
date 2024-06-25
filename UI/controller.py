import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente.\n"
                                                      f"numero nodi: {len(self._model._myGraph.nodes)}\n"
                                                      f"numero archi: {len(self._model._myGraph.edges)}\n"))
        self._view.update_page()
        pass

    def handle_countedges(self, e):
        # effettuare controllo input
        soglia = float(self._view.txt_name.value)
        maggiori, minori = self._model.getEdgesSoglia(soglia)
        self._view.txt_result2.controls.append(ft.Text(f"Soglia: {soglia}\n"
                                                       f"Numero archi con peso maggiore della soglia: {maggiori}\n"
                                                       f"Numero archi con peso minore della soglia: {minori}\n"))
        self._view.update_page()
        pass

    def handle_search(self, e):
        path, weight = self._model.getPath(float(self._view.txt_name.value))
        self._view.txt_result3.controls.append(ft.Text(f"Percorso trovato:\n"
                                                       f"- Peso totale (massimo): {weight}\n"
                                                       f"- Lunghezza percorso: {len(path)}\n"
                                                       f"Tappe:"))
        for n in range(len(path) - 1):
            self._view.txt_result3.controls.append(ft.Text(f"Chromosomes: {path[n]} -> {path[n+1]} ({self._model._getEdgeWeight(path[n], path[n+1])})"))

        self._view.update_page()

        pass