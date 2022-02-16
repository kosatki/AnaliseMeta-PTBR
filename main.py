import pandas as pd

from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC6d4eb38f8c9e8e5cff21f68e22ab4942"
# Your Auth Token from twilio.com/console
auth_token = "5c7b281b5719bcf1736f00afce23dddf"
client = Client(account_sid, auth_token)


# Arquivos em Excel com Pandas
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} encontramos alguém com mais de 55000. {vendedor} vendeu um total de {vendas} reais.')
        message = client.messages.create(
            to="numero_de_telefone",
            from_="++19378724027",
            body=f'O vendedor {vendedor} alcançou a meta no mês de {mes}, vendendo um total de {vendas} reais!')
        print(message.sid)
