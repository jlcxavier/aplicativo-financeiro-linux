import sys
from PyQt5.QtWidgets import QApplication
from design import AppFinanceira

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AppFinanceira()
    janela.show()
    sys.exit(app.exec_())
