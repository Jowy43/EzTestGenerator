class Preguntas:
    """Crear preguntas"""

    def __init__(self, tituloPregunta: str, resA: str, resB: str):
        super(Preguntas, self).__init__()
        self.titulo = tituloPregunta
        self.resA = resA
        self.resB = resB
