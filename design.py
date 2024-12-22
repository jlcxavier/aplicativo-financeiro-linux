from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QMessageBox, QTabWidget, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QDate
from dados import adicionar_transacao, carregar_dados
from funcoes_calculo import atualizar_saldo


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class AppFinanceira(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Aplicativo Financeiro")
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        layout = QVBoxLayout()

        # Criar Abas
        self.tabs = QTabWidget()

        # Aba 1: Adicionar Transações
        self.tab_transacoes = QWidget()
        self.init_tab_transacoes()
        self.tabs.addTab(self.tab_transacoes, "Transações")

        # Aba 2: Tabela
        self.tab_tabela = QWidget()
        self.init_tab_tabela()
        self.tabs.addTab(self.tab_tabela, "Tabela")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

        # Saldo Inicial
        self.saldo = 0.0
        self.carregar_transacoes()

        # Aba 3: Relatórios
        self.tab_relatorios = QWidget()
        self.init_tab_relatorios()
        self.tabs.addTab(self.tab_relatorios, " Relatório")

    def init_tab_transacoes(self):
        # Layout para a aba de transações
        layout = QVBoxLayout()

        # Campo de Valor
        valor_layout = QHBoxLayout()
        self.valor_input = QLineEdit(self)
        self.valor_input.setPlaceholderText("Digite o valor")
        self.valor_input.setValidator(QDoubleValidator(0.0, 1000000.0, 2))
        valor_layout.addWidget(QLabel("Valor:"))
        valor_layout.addWidget(self.valor_input)
        layout.addLayout(valor_layout)

        # Campo de Tipo (Entrada ou Saída)
        tipo_layout = QHBoxLayout()
        self.tipo_combobox = QComboBox(self)
        self.tipo_combobox.addItems(["Entrada", "Saída"])
        tipo_layout.addWidget(QLabel("Tipo:"))
        tipo_layout.addWidget(self.tipo_combobox)
        layout.addLayout(tipo_layout)

        # Campo de Data
        data_layout = QHBoxLayout()
        self.data_input = QDateEdit(self)
        self.data_input.setCalendarPopup(True)
        self.data_input.setDate(QDate.currentDate())
        data_layout.addWidget(QLabel("Data:"))
        data_layout.addWidget(self.data_input)
        layout.addLayout(data_layout)

        # Campo de Descrição
        descricao_layout = QHBoxLayout()
        self.descricao_input = QLineEdit(self)
        self.descricao_input.setPlaceholderText("Digite uma descrição")
        descricao_layout.addWidget(QLabel("Descrição:"))
        descricao_layout.addWidget(self.descricao_input)
        layout.addLayout(descricao_layout)

        # Botão de Adicionar
        self.adicionar_button = QPushButton("Adicionar Transação", self)
        self.adicionar_button.clicked.connect(self.salvar_transacao)
        layout.addWidget(self.adicionar_button)

        # Exibir Saldo Atual
        self.saldo_label = QLabel("Saldo Atual: R$ 0.00", self)
        layout.addWidget(self.saldo_label)

        self.tab_transacoes.setLayout(layout)

    def init_tab_tabela(self):
        # Crie o widget para a aba de tela
        self.tab_tabela = QWidget()
        # Layout para a aba de tabela
        layout = QVBoxLayout()

        # Criar tabela
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(
            ["Data", "Entrada", "Saída", "Saldo Total"])

        layout.addWidget(self.tabela)
        self.tab_tabela.setLayout(layout)

    def salvar_transacao(self):
        try:
            # Obter os valores dos campos
            valor = float(self.valor_input.text())
            tipo = self.tipo_combobox.currentText()
            data = self.data_input.date().toString("dd/MM/yyyy")
            descricao = self.descricao_input.text()

            if tipo == "Saída":
                valor = -valor  # Saídas diminuem o saldo

            # Salvar no arquivo JSON
            adicionar_transacao(tipo, valor, data, descricao)

            # Atualizar saldo
            self.saldo += valor
            self.saldo_label.setText(f"Saldo Atual: R$ {self.saldo:.2f}")

            # Atualizar tabela
            self.atualizar_tabela()

            # Exibir mensagem de sucesso
            QMessageBox.information(self, "Transação Adicionada",
                                    f"Transação adicionada com sucesso!\n\nTipo: {tipo}\nData: {data}\nDescrição: {descricao}\nValor: R$ {valor:.2f}")

            # Limpar os campos
            self.valor_input.clear()
            self.descricao_input.clear()
            self.tipo_combobox.setCurrentIndex(0)
            self.data_input.setDate(QDate.currentDate())

        except ValueError:
            QMessageBox.warning(
                self, "Erro", "Por favor, insira um valor válido!")
        self.atualizar_grafico()

    def carregar_transacoes(self):
        """
        Carrega as transações do arquivo JSON e atualiza o saldo e a tabela.
        """
        transacoes = carregar_dados()
        self.saldo = sum([transacao["valor"] for transacao in transacoes])
        self.saldo_label.setText(f"Saldo Atual: R$ {self.saldo:.2f}")
        self.atualizar_tabela()

    def atualizar_tabela(self):
        """
        Atualiza a tabela com os dados das transações.
        """
        transacoes = carregar_dados()

        # Agrupar por data
        agrupado = {}
        for transacao in transacoes:
            data = transacao["data"]
            valor = transacao["valor"]
            if data not in agrupado:
                agrupado[data] = {"entrada": 0, "saida": 0}
            if valor > 0:
                agrupado[data]["entrada"] += valor
            else:
                agrupado[data]["saida"] += abs(valor)

        # Adicionar à tabela
        self.tabela.setRowCount(len(agrupado))
        saldo_acumulado = 0
        for i, (data, valores) in enumerate(sorted(agrupado.items())):
            saldo_acumulado += valores["entrada"] - valores["saida"]
            self.tabela.setItem(i, 0, QTableWidgetItem(data))
            self.tabela.setItem(i, 1, QTableWidgetItem(
                f"R$ {valores['entrada']:.2f}"))
            self.tabela.setItem(i, 2, QTableWidgetItem(
                f"R$ {valores['saida']:.2f}"))
            self.tabela.setItem(i, 3, QTableWidgetItem(
                f"R$ {saldo_acumulado:.2f}"))

    def init_tab_relatorios(self):
        # Layout para a aba relatório
        layout = QVBoxLayout()

        # Criar objeto FigureCanvas (área do gráfico)
        self.canvas = FigureCanvas(Figure(figsize=(8, 6)))

        # Adicionar o canvas ao layout
        layout.addWidget(self.canvas)

        self.tab_relatorios.setLayout(layout)

    def atualizar_grafico(self):
        """
        Atualiza o gráfico de entradas e saídas.
        """
        transacoes = carregar_dados()

        # Agrupar por data
        agrupado = {}
        for transacao in transacoes:
            data = transacao['data']
            valor = transacao['valor']
            if data not in agrupado:
                agrupado[data] = {'entrada': 0, 'saida': 0}
            if valor > 0:
                agrupado[data]['entrada'] += valor
            else:
                agrupado[data]['saida'] += abs(valor)

        # Preparar dados para o gráfico
        datas = sorted(agrupado.keys())
        entradas = [agrupado[data]['entrada'] for data in datas]
        saidas = [agrupado[data]['saida'] for data in datas]

        # Plotar o gráfico
        ax = self.canvas.figure.subplots()
        ax.clear()

        # Índices no eixo X (2 por data)
        indices = range(len(datas))

        # Desenhar as barras
        ax.bar([i - 0.2 for i in indices], entradas,
               width=0.4, color='blue', label='Entradas')
        ax.bar([i + 0.2 for i in indices], saidas,
               width=0.4, color='red', label='Saídas')

        # Configurar o gráfico
        ax.set_xticks(indices)
        ax.set_xticklabels(datas, rotation=45)
        ax.set_title("Relatório de Entradas e Saídas")
        ax.set_xlabel('Datas')
        ax.set_ylabel('Valores')
        ax.legend()
        ax.grid(axis='y')
        self.canvas.draw()
