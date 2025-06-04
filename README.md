"# teste_code_leap" 
"# teste_code_leap" 


POST /create/ </br>
Exemplo de corpo da requisição:</br>
{</br>
"username": "teste username",</br>
"title": "teste title",</br>
"content": "teste contente"</br>
}</br>

GET /list/</br>
Retorna a lista de todos os posts da API pública da CodeLeap.</br>
Não precisa de corpo na requisição.</br>

PATCH /update/<id>/</br>
Atualiza um post existente.</br>
O ID do post deve estar na URL.</br>
Exemplo de corpo do retorno da requisição:</br>
{</br>
"title": "Novo título",</br>
"content": "Novo conteúdo"</br>
}</br>

DELETE /delete/<id>/</br>
Deleta um post existente.</br>
O ID do post deve estar na URL.</br>
Não precisa de corpo na requisição.</br>
