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

        self._view.update_page()



    def handle_graph(self, e):
        (num_nodi, num_archi) = self._model.createGraph(self._view._ddcolor.value, self._view._ddyear.value)
        self._view.btn_search.disabled = False

        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici {num_nodi}  Numero di archi {num_archi}"))
        top3archi = self._model.getTop3()
        for arco in top3archi:
            self._view.txtOut.controls.append(ft.Text(f"Arco da {arco[0]}  a  {arco[1]}   Peso: {arco[2]['weight']}"))

        ripetuti =  self._model.getNodiRipetuti(top3archi)
        self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {ripetuti}"))

        self._view.update_page()



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
