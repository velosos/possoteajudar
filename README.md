# possoteajudar

ServiceNow's knowledge base integration (Kbs) app to be used as a help base in an internal customer app.

Made in Python / Django, it is a search engine that consumes a ServiceNow and prints the result in another App.

Examples:

Page with the search engine:

In views.py I create a def where I do a GET in the ServiceNow api, which returns the results in JSON format, from there, in other defs, I can manipulate the routes with the expected results.

See the example:

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


