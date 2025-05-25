# Explicação: EmailBackend

Este documento explica o funcionamento do backend de autenticação personalizado `EmailBackend` criado em `prototipo_tcc/src/mysite/usuarios/backends.py`.

---

## O que são backends no Django?

No Django, backends são componentes que permitem personalizar e expandir funcionalidades essenciais do framework. Eles são usados para definir como certas operações são realizadas, como autenticação, autorização, armazenamento de arquivos, cache, sessões, envio de e-mails, entre outros.

**Exemplos de backends no Django:**
- **Autenticação:** Define como os usuários são autenticados (por username, e-mail, LDAP, OAuth, etc).
- **Autorização:** Controla como permissões são verificadas.
- **Cache backend:** Define onde e como o cache é armazenado (memória, Redis, Memcached, etc).
- **Session backend:** Define onde as sessões dos usuários são salvas (cookies, banco de dados, cache, arquivos, etc).
- **Storage backend:** Define onde arquivos enviados são armazenados (local, S3, Google Cloud, etc).
- **Email backend:** Define como e-mails são enviados (SMTP, console, arquivo, serviços externos).
- **Database backend:** Permite usar diferentes bancos de dados (PostgreSQL, MySQL, SQLite, Oracle).

Esses backends tornam o Django flexível e extensível, permitindo que você adapte o framework às necessidades do seu projeto.

---

## Sobre o backend de autenticação por e-mail que você construiu

Você criou um backend chamado **EmailBackend**. Ele permite que os usuários façam login usando o e-mail cadastrado, em vez do nome de usuário padrão. Isso é útil em sistemas onde o e-mail é o identificador principal do usuário.

### Funcionamento detalhado:

- **Herança de ModelBackend:**  
  Sua classe herda de `ModelBackend`, aproveitando funcionalidades já existentes, como a verificação da senha e do status do usuário.

- **Método `authenticate`:**
  - Recebe o e-mail (no lugar do username) e a senha.
  - Se o username não for informado, tenta pegar o e-mail dos argumentos adicionais (`kwargs`).
  - Busca no banco de dados um usuário cujo campo `email` seja igual ao valor informado.
  - Se encontrar, verifica se a senha está correta (`check_password`) e se o usuário está ativo (`user_can_authenticate`).
  - Se tudo estiver certo, retorna o objeto do usuário autenticado.
  - Se não encontrar o usuário ou a senha estiver errada, retorna `None`.

- **Configuração:**  
  Para usar esse backend, você precisa adicioná-lo à lista `AUTHENTICATION_BACKENDS` no seu `settings.py`.  
  Isso diz ao Django para tentar autenticar usando seu backend antes (ou depois) do backend padrão.

---

## Como funciona o EmailBackend?

- Permite login usando o e-mail do usuário.
- Busca o usuário no banco de dados pelo campo `email`.
- Verifica se a senha está correta e se o usuário está ativo.
- Retorna o usuário autenticado ou `None` se falhar.

### Trecho principal do código:

```python
try:
    # Busca o usuário pelo campo de e-mail
    user = UserModel.objects.get(email=username)
except UserModel.DoesNotExist:
    # Retorna None se o usuário não existir
    return None
else:
    # Verifica se a senha está correta
    # e se o usuário está ativo (user_can_authenticate)
    if user.check_password(password) and self.user_can_authenticate(user):
        return user
# Retorna None caso a autenticação falhe
return None
```

---

## Como configurar?

Adicione no seu `settings.py`:

```python
AUTHENTICATION_BACKENDS = [
    'prototipo_tcc.src.mysite.usuarios.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

---

## Vantagens

- Permite login por e-mail, que é mais amigável para o usuário.
- Pode ser combinado com outros backends (por exemplo, permitir login tanto por e-mail quanto por username).
- Facilita integração com sistemas onde o e-mail é obrigatório e único.

---

## Segurança

- Usa métodos seguros do Django para verificar a senha.
- Respeita a política de usuários ativos/inativos.
- Não expõe informações sensíveis em caso de falha.

---

## Resumindo

- Backends no Django são mecanismos para personalizar operações importantes do framework, como autenticação, cache, sessões, armazenamento, etc.
- O backend que você construiu permite login por e-mail, tornando o sistema mais flexível e moderno.
- Ele é seguro, reutiliza funcionalidades do Django e pode ser combinado com outros métodos de autenticação.
- O conceito de backend é fundamental para adaptar o Django a diferentes necessidades e integrações, tornando-o um framework robusto e versátil.

---

Para mais detalhes, consulte o código-fonte em `usuarios/backends.py`.