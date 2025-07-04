import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        d = self._view._txtInDurata.value
        if d is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun valore inserito", color="red"))
            self._view.update_page()
            return

        try:
            dInt = int(d)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserisci un numero", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(dInt)

        numNodi, numArchi = self._model.graphDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato!"))
        self._view.txt_result.controls.append(ft.Text(f"# Vertici: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"# Archi: {numArchi}"))
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
       albums = self._model.getAllAlbum()
       for a in albums:
           self._view._ddAlbum.options.append(ft.dropdown.Option(key=a, text=a.Title)) #key=oggetto principale, text=cosa mostro)
       self._view.update_page()

        #METODO CLASSICO DA USARE SEMPRE (AGGIUNTA NELLA VIEW)
        #years = self._model.getAllYears()
        #for y in years:
        #   self._view._ddAnno.options.append(ft.dropdown.Option(y))
        #self._view.update_page()

    def getSelectedAlbum(self, e):
        pass

    def handleAnalisiComp(self, e):
        album = self._view._ddAlbum.value
        if album is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun album inserito", color="red"))
            self._view.update_page()
            return

        lunghezzaCC, durata = self._model.getComponenteConnessa(album)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {album} è formata da {lunghezzaCC} album e dura {durata} min"))
        self._view.update_page()


    def handleGetSetAlbum(self, e):
        pass