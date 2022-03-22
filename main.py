import sys

from PySide2.QtWidgets import *

from UIclass.SplashScreen import SplashScreen

if __name__ == "__main__":
    app = QApplication()
    main = SplashScreen()
    sys.exit(app.exec_())
