import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from design import AppFinanceira


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_financeira = AppFinanceira()
        self.setCentralWidget(self.app_financeira)
        # Instala o event filter para capturar eventos
        self.installEventFilter(self)

        def eventFilter(self, source, event):
            # Verifica se o evento é uma tecla pressionada
            if event.type() == event.KeyPress and event.key() == Qt.Key_Escape:
                print("ESC pressionado. Fechando o aplicativo...")
                QApplication.instace().quit()  # Fecha o aplicativo
            return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AppFinanceira()
    janela.show()
    sys.exit(app.exec_())
