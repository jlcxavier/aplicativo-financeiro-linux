
# Aplicativo Financeiro

Um aplicativo financeiro simples desenvolvido em Python utilizando PyQt5. Ele permite gerenciar entradas e saídas financeiras, visualizar gráficos de desempenho e acompanhar o histórico de transações.

## Funcionalidades

- Adicionar transações com descrição, valor, tipo (entrada/saída) e data.
- Visualizar:
  - Gráfico com entradas e saídas por dia.
  - Tabela com resumo diário de entradas, saídas e saldo acumulado.
  - Histórico detalhado de transações.
- Excluir transações diretamente do histórico.
- Armazenar as transações em um arquivo JSON.

---

## Capturas de Tela

> Fazer em um segundo momento
---

## Requisitos

- Python 3.8 ou superior
- PyQt5
- Matplotlib

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/aplicativo-financeiro-linux.git
   cd aplicativo-financeiro-linux
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso

1. Execute o aplicativo:
   ```bash
   python main.py
   ```

2. Use as abas para:
   - **Transações:** Adicionar novas transações.
   - **Relatório:** Visualizar o gráfico de entradas e saídas.
   - **Resumo:** Consultar entradas, saídas e saldo acumulado por dia.
   - **Histórico:** Acompanhar todas as transações e excluir as desejadas.

---

## Estrutura do Projeto

```plaintext
aplicativo-financeiro-linux/
├── main.py               # Arquivo principal que executa a aplicação
├── design.py             # Arquivo que gerencia a interface gráfica
├── funcoes_calculo.py    # Funções de cálculo (ex.: saldo, relatórios financeiros)
├── campos_validacao.py   # Funções para validação e manipulação de campos
├── utils.py              # Funções auxiliares (ex.: formatação de números, datas)
├── dados.py              # Funções para manipulação de dados (carregar/salvar json)
├── transacoes.json       # Armazenamento das transações
├── assets/               # Recursos estáticos (ex.: imagens, ícones)
└── tests/                # Testes automatizados
    ├── test_calculos.py  # Testes para funções de cálculo
    └── test_validacao.py # Testes para validações
```

---

## Como Contribuir

1. Faça um fork do repositório.
2. Crie uma branch com a sua feature/bugfix:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Descrição da alteração"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se livre para usá-lo, modificá-lo e distribuí-lo como desejar.

---

## Autor

Desenvolvido por **José Luís**. Entre em contato para dúvidas ou sugestões!
