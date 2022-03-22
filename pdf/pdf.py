from jinja2 import Environment, FileSystemLoader
import pdfkit


class createPdf:
    def __init__(self, exam, tituloExam: str):
        super(createPdf, self).__init__()
        self.env = Environment(loader=FileSystemLoader("pdf"))
        self.template = self.env.get_template("template.html")
        self.html = self.template.render(preguntas=exam)
        option = {
            'page-size': 'A4',
            'margin-top': '0.1in',
            'margin-right': '0.1in',
            'margin-bottom': '0.1in',
            'margin-left': '0.1in',
        }
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

        pdfkit.from_string(self.html, tituloExam + '.pdf', options=option, configuration=config)
