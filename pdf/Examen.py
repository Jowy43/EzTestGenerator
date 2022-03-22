from pdf.Preguntas import Preguntas
from pdf.pdf import createPdf


class Examen:
    """Se encarga de generar el mapa para crear el pdf"""

    def __init__(self, lPreguntas: [], titulo: str):
        super(Examen, self).__init__()
        self.lPreguntas: Preguntas = lPreguntas
        exam = {}
        cont = 1
        for x in self.lPreguntas:
            exam[str(cont)] = {"titulo": x.titulo, "resA": x.resA, "resB": x.resB}
            cont += 1
        createPdf(exam, titulo)
