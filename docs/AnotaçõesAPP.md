## Migrations
- São a conexão entre a estrutura do banco de dados e o script na aplicação, seu objetivo é manter a estrutura do banco sincronizada com a da aplicação, tendo as mesmas tabelas, colunas e etc
- São criadas pelo comando `*python manage.py makemigrations`
- Porem uma migrate é criada a partir de um model e o objeto config precisa estar dentro de INSTALLED_APPS
- Para que todas as migrates sejam efetivamente comitadas utilizamos o comando `python manage.py migrate`

## Forms 
- tem como objetivo definir os modelos de formularios da aplicação pelo django, neste caso foi utilizado o ModelForm, que cria um formulario 
a partir do modelo do banco de dados, sendo assim facilita integrar os dados ao banco de dados
- Existem duas formas principais de criar forms no Django:
Forms baseados em classes (forms.Form).
ModelForms (forms.ModelForm) – baseado em models.

| Tipo              | Descrição                                                         |
|-------------------|-------------------------------------------------------------------|
| forms.Form        | Formulário básico, criado manualmente.                            |
| forms.ModelForm   | Formulário baseado em um model, com menos código necessário.     |
| is_valid()        | Verifica se os dados do formulário são válidos.                   |
| cleaned_data      | Retorna os dados validados do formulário.                         |
| clean()           | Permite adicionar validações personalizadas.                     |



## Models
Serve como molde para estrutura do banco de dados da aplicação. Ele contém os campos e comportamentos essenciais dos dados que você está armazenando. O Django segue o DRY Principle . O objetivo é definir seu modelo de dados em um lugar e derivar coisas dele automaticamente.

1. **Exemplo de Model**
- class Post(models.Model):
    title = models.CharField(max_length=100)  # Título do post
    content = models.TextField()  # Conteúdo do post
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

2. **Tipos de campo**

| Campo          | Descrição                                         |
|----------------|---------------------------------------------------|
| CharField      | Campo de texto com tamanho limitado.              |
| TextField      | Campo de texto sem limite de caracteres.          |
| IntegerField   | Campo numérico (inteiro).                         |
| DateTimeField  | Campo de data e hora.                             |
| BooleanField   | Campo booleano (True/False).                      |
| EmailField     | Campo para e-mails.                               |
| ForeignKey     | Campo de relação com outra tabela (chave estrangeira). |


3. **Metodos Uteis no Model**

| Função                | Objetivo                                     |
|-----------------------|----------------------------------------------|
| objects.all()         | Retorna todos os objetos do model.           |
| objects.filter(**kwargs) | Filtra os objetos com base em critérios.   |
| objects.get(**kwargs) | Retorna um único objeto que corresponde ao critérios. |
| save()                | Salva o objeto no banco de dados.            |
| delete()              | Exclui o objeto do banco de dados.           |


4. **def __str__**
- O método __str__ define como o objeto será representado quando for exibido como texto.

5. **Relacionamento entre Models**

| Relacionamento     | Descrição                              |
|--------------------|----------------------------------------|
| ForeignKey         | Relacionamento de muitos para um.      |
| OneToOneField      | Relacionamento de um para um.          |
| ManyToManyField    | Relacionamento de muitos para muitos.  |



6. **RESUMO MODEL**
✅ Um model no Django é uma representação de uma tabela no banco de dados.
✅ Ele é definido como uma classe Python que herda de models.Model.
✅ Os atributos da classe se tornam colunas na tabela do banco de dados.
✅ Você pode criar, editar, consultar e excluir objetos do banco de dados usando métodos fornecidos pelo Django.
✅ Relacionamentos podem ser criados entre diferentes models para estruturar seus dados.

## URLs
- O arquivo urls define quais páginas o usuário pode acessar no seu site e qual lógica (view) será executada quando cada URL for acessada.
- vamos entender oque cada coisa faz em um urlpattern
- `urlpatterns = [
      path('', views.index, name='index'),  # Mapeia a URL / para a função index
      path('<int:post_id>/', views.detailed_post, name='detailed_post'),  # Mapeia /1/, /2/, etc. para a função detailed_post
      path('new/', views.new_post, name='new_post'),  # Mapeia /new/ para a função new_post
  ]`

| Elemento          | Descrição                                                            |
|-------------------|----------------------------------------------------------------------|
| path()            | Função que conecta uma URL a uma view.                                |
| ''                | Representa a URL raiz (por exemplo, /blog/).                          |
| <int:post_id>/    | Um parâmetro dinâmico que captura um número (por exemplo, /blog/1/).  |
| views.index       | A função na view que será chamada quando a URL for acessada.          |
| name='index'      | Um nome para a rota, usado para referenciar a URL nos templates.       |


1. **COMO DJANGO PROCESSA UMA REQUISISÃO**
- Quando um usuário acessa uma URL no navegador, o Django verifica o urls.py para encontrar uma correspondência.
- Se uma URL corresponder a um dos caminhos definidos no urlpatterns, o Django executa a view associada.
- A view faz o trabalho necessário (por exemplo, buscar dados do banco de dados) e devolve uma resposta HTML para o usuário

2. **URL Dinamica**
- exemplo `path('<int:post_id>/', views.detailed_post, name='detailed_post')`
- Se o usuário acessa /blog/1/, o Django captura o 1 como post_id e passa para a função detailed_post.
- Isso permite que você exiba detalhes específicos de um post.

3. ***name*** nas ROTAS
- usado para identificar as rotas de forma mais facil e reutilizavel

4. RESUMO DO URLs
✅ Mapeia as URLs do site para as views que devem ser chamadas.
✅ Organiza a navegação do site, definindo quais páginas estão disponíveis.
✅ Permite usar nomes amigáveis para as rotas, facilitando a manutenção e evitando links "quebrados".
✅ Facilita a criação de URLs dinâmicas, passando parâmetros para as views.

## Templates 
Um template Django é um arquivo que define a estrutura e o visual das páginas web de um aplicativo, permitindo inserir dados dinâmicos em HTML. Os templates são uma parte fundamental da framework web Django e são utilizados para criar interfaces dinâmicas. 

# View
- Views são funções e classes que recebem requisições HTTP e retornam respostas HTTP
- São responsaveis pela lógica de processamento da requisição, como acessar banco de daddos, manipular dados e definir respostas para o usuario 
- Podem rendereizar templetes HTML, Interagir com modelos de Dados (Models), processar formularios e etc

**TIPOS DE VIEWS**
- FBVs (Views baseadas em funções): São funções simples que recebem uma requisição e retornam uma resposta
- CBVs (Views baseadas em Classes): Classes que fornecem flexibilidade e reutilização de codigo para manipular as requisições

**FBVs**
Vamos ver alguns exemplos de views

**View FBV Simples**
```
from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá, Mundo!")
```
retorna uma resposta HTTP simples

**Exibindo um Template com uma View**
```
from django.shortcuts import render

def minha_view(request):
    return render(request, 'blog/minha_view.html')
```
utiliza o render() para rendereizar um template e retorna a resposta HTTP com o conteudo gerado

**View com Formulario**
```
from django.shortcuts import render
from .forms import ContatoForm

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            print(form.cleaned_data)
            return render(request, 'blog/success.html')
    else:
        form = ContatoForm()
    return render(request, 'blog/contato.html', {'form': form})
```
🧩 Explicação:
`request.method == 'POST'` – Verifica se o formulário foi enviado.
`form.is_valid()` – Valida os dados do formulário.
`form.cleaned_data` – Dados validados prontos para uso.

🧩 Explicação else:
else é executado quando o método da requisição não é POST, ou seja, quando a página está sendo acessada com o método HTTP padrão GET (que ocorre, por exemplo, quando um usuário acessa a página de contato pela primeira vez ou recarrega a página).
Sendo assim, o else é usado para renderizar o formulário vazio para o usuário quando acessa a pagina para preenche-lo

**View com Redirecionamento**
```
from django.shortcuts import redirect

def minha_view(request):
    return redirect('outra_url')
```
`redirect()` – Redireciona o usuário para a URL indicada.
o `HttpResponseRedirect` tem uma funcionalidade parecida

**CBVs**
Vamos ver um exemplo de Classes baseadas em views
```
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
```

template do exemplo:"
```
<ul>
    {% for post in object_list %}
        <li>{{ post.title }}</li>
    {% endfor %}
</ul>
```
🧩 Explicação:
ListView – Uma view genérica para exibir uma lista de objetos do model especificado.

**RESUMO SOBRE VIEW**
| Tipo        | Descrição                                                           |
|-------------|---------------------------------------------------------------------|
| views       | Funções ou classes que processam as requisições e retornam respostas HTTP. |
| render()    | Função usada para renderizar templates com dados.                   |
| HttpResponse| Retorna uma resposta HTTP simples.                                  |
| redirect()  | Redireciona para outra URL.                                        |
| ListView    | View genérica para exibir uma lista de objetos.                    |
