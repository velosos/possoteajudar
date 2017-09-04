# possoteajudar

App de integração das knowledge base (Kbs) da ServiceNow para ser usado como base de ajuda em uma App interna do cliente.

Feita em Python/Django, trata-se de um buscador que consome a ServiceNow e imprime o resultado em uma outra App.

Exemplos:

*Página com o buscador:*

Na **views.py** crio uma *def* onde faço um GET na api da ServiceNow, que me retorna os resultados em formato JSON, a partir dai, em outras *def*, consigo manipular as rotas com os resultados esperados.

Veja o exemplo:

```
def resultado(request,texto):

    texto = request.POST.get('texto')
    url = 'https://instance.service-now.com/api/now/table/kb_knowledge?sysparm_query=short_descriptionLIKE' + texto

    user = 'yourUser'
    pwd = 'password'

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    response = requests.get(url, auth=(user, pwd), headers=headers )

    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()

    return render(request, 'resultado.html',{'obj':data['result']})    
    
```

![alt text](https://github.com/velosos/possoteajudar/blob/master/getKbs/staticfiles/img/Captura%20de%20Tela%202017-09-04%20%C3%A0s%2011.07.51.png)


Página que imprime os resultados:

![alt text](https://github.com/velosos/possoteajudar/blob/master/getKbs/staticfiles/img/Captura%20de%20Tela%202017-09-04%20%C3%A0s%2011.08.05.png)

Página que consome o artigo selecionado nos resultados: 

![alt text](https://github.com/velosos/possoteajudar/blob/master/getKbs/staticfiles/img/Captura%20de%20Tela%202017-09-04%20%C3%A0s%2011.08.37.png)

Para mais informações sobre:

Django: https://www.djangoproject.com/

Bootstrap: http://getbootstrap.com/

ServiceNow: http://wiki.servicenow.com/index.php?title=Main_Page


