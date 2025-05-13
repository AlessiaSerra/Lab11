import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        for a in range(2015,2019):
            self._view._ddyear.options.append(ft.dropdown.Option(a))

        colori = self._model.getColori()

        self._view._ddcolor.options.append(ft.dropdown.Option("Unspecified"))

        for colour in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(colour))



    def handle_graph(self, e):
        self._model.createGraph(self._view._ddcolor.value, self._view._ddyear.value)
        self._view.btn_search.disabled = False




    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
