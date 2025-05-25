# Projeto TCC - Sistema de Gestão Financeira

Este projeto é um sistema web desenvolvido em Django para controle e gestão financeira, com autenticação personalizada por e-mail.

## Funcionalidades

- Cadastro de usuários com e-mail obrigatório
- Login e logout de usuários
- Autenticação personalizada usando e-mail
- Cadastro e gerenciamento de informações financeiras (exemplo: receitas, despesas)
- Interface amigável e segura

## Estrutura do Projeto

```
prototipo_tcc/
│
├── src/
│   └── mysite/
│       ├── gest_financeira/   # App de gestão financeira
│       ├── usuarios/          # App de autenticação e usuários
│       └── mysite/            # Configurações principais do projeto
│
├── docs/                      # Documentação do projeto
├── manage.py
└── README.md
```

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd prototipo_tcc
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Configuração de autenticação por e-mail

O projeto utiliza um backend customizado para permitir login usando o e-mail do usuário.  
Veja detalhes em `docs/explicacao_backends.md`.

## Documentação

A documentação detalhada está disponível na pasta `docs/`.

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

---

**Desenvolvido para Trabalho de Conclusão de Curso (TCC).**