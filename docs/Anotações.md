# URL (fora do APP)
- Esse arquivo tem como função centralizar e gerenciar as rotas principais da aplicação
- Define como as URLs serão distribuidas entre os apps e outras funcionalidades do projeto

Ele realiaza as seguintes ações
1. inclui URLs de um app
- encaminha todas as urls com o `/nome_app` para o arquivo urls **dentro** do app
- Isso permite que a estrutura seja mais modularizada e organizada pois cada app tem suas proprias urls definidas
2. Administração do Django
- A linha path('admin/', admin.site.urls) define a URL para o painel de administração do Django, que será acessível através da URL admin/. 
- Isso é essencial para gerenciar o conteúdo e a configuração do seu projeto Django via interface gráfica.

RESUMO
o arquivo de URLs fora do app serve como um ponto central para incluir e organizar as rotas de diferentes apps e funções, facilitando a manutenção e escalabilidade do projeto.
# SETTINGS

## INSTALLED APP
A configuração INSTALLED_APPS em um projeto Django é uma lista que contém os aplicativos (apps) que foram instalados e são parte integrante do seu projeto Django. Cada item na lista é uma string que representa o caminho de importação do aplicativo. 

