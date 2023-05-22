import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

con = mysql.connector.connect(
    host='localhost', database='projeto1', user='root', password='****')
if con.is_connected():
    cursor = con.cursor()
    cursor.execute("""
    SELECT
    C.NOME,
    J.NOME_JOGO,
    P.PLATAFORMA,
    J.PRECO_ALUGUEL,
    A.DATA_ALUGUEL,
    A.NOTA
    FROM ALUGUEL A
    INNER JOIN CLIENTES C
    ON A.ID_CLIENTE = C.IDCLIENTE
    INNER JOIN JOGOS J
    ON A.ID_JOGO = J.IDJOGO
    INNER JOIN PLATAFORMA P
    ON A.ID_PLATAFORMA = P.IDPLATAFORMA
    ORDER BY J.NOME_JOGO;
""")
    linha = cursor.fetchall()

    dados = pd.DataFrame(linha)

    dados = dados[[1, 5]].groupby(1).median()

    dados.plot(kind='barh', color='k')
    plt.title("Relação de Jogos com sua Média de Avaliação")
    plt.xlabel("Notas")

    plt.show()


if con.is_connected():
    cursor.close()  # type:ignore
    con.close()
