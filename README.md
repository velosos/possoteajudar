# possoteajudar

App de integração das knowledge base (Kbs) da ServiceNow para ser usado como base de ajuda em uma App interna do cliente.

Feita em Python/Django, trata-se de um buscador que consome a ServiceNow e imprime o resultado em uma outra App.

Prints de Exemplo:





Na views.py, faço um get na api da ServiceNow, que me retorna os resultados em formato JSON, onde posso manipular em rotas, quais informações desejo receber e onde desejo imprimir:



