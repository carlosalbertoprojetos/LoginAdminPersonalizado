# LoginAdminPersonalizado

Este repositório contém um **pequeno projeto de estudo** com foco na criação de um sistema de login personalizado utilizando o framework Django. O objetivo principal deste projeto é servir como uma **base prática** para o **aperfeiçoamento de conhecimentos** em Django, especialmente em relação à personalização de sistemas de autenticação.

## 💡 **Sobre o Projeto**

O **LoginAdminPersonalizado** foi desenvolvido com o propósito de explorar como customizar o sistema de autenticação padrão do Django. Ele demonstra:

- A implementação de um modelo de usuário personalizado (`CustomUser`).
- A configuração de um formulário de autenticação específico.
- A personalização da página de login para o Django Admin.
- Boas práticas na configuração do sistema de autenticação.

Este projeto é ideal para desenvolvedores que estão iniciando no estudo de **autenticação em Django** e desejam entender como adaptar o comportamento padrão para atender a requisitos específicos.

## 🚀 **Principais Funcionalidades**

- Modelo de usuário customizado com campos adicionais (quando necessário).
- Formulário de login estilizado e funcional.
- Total integração com o painel administrativo padrão do Django.
- Base para expandir a funcionalidade de autenticação.

## 🛠️ **Tecnologias Utilizadas**

- [Python](https://www.python.org/) 3.9+
- [Django](https://www.djangoproject.com/) 4.x
- Banco de dados SQLite (padrão para estudos)

## 🗂️ **Estrutura do Projeto**

```plaintext
LoginAdminPersonalizado/
│
├── login/                 # App principal do projeto
│   ├── forms.py           # Formulários personalizados
│   ├── models.py          # Modelo de usuário personalizado
│   ├── views.py           # Lógica das views
│   └── templates/         # Templates HTML customizados
│       └── login.html     # Página de login personalizada
│
├── manage.py              # Comando principal do Django
├── db.sqlite3             # Banco de dados SQLite
└── settings.py            # Configurações do projeto
```

## ⚙️ **Configuração e Execução**

1. Clone o repositório:
   ```bash
   git clone https://github.com/carlosalbertoprojetos/LoginAdminPersonalizado.git
   cd LoginAdminPersonalizado
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

4. Crie um superusuário para acessar o admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse o projeto em seu navegador:
   - Página de login: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
   - Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📚 **Propósito Educacional**

Este projeto é **exclusivamente para fins de aprendizado**. Ele não é uma solução completa de autenticação para produção, mas sim um ponto de partida para entender os conceitos de personalização no Django.

## 🌟 **Próximos Passos**

- Adicionar validações de segurança avançadas.
- Implementar recuperação e alteração de senha.
- Expandir para incluir autenticação por e-mail.

## 📄 **Licença**

Este projeto é disponibilizado sob a [Licença MIT](LICENSE). Sinta-se à vontade para utilizá-lo, adaptá-lo e aprimorá-lo conforme necessário.

---

💻 Desenvolvido por [Carlos Alberto Medeiros](https://www.linkedin.com/in/carlos-alberto-medeiros-29aa6258/)  
🌟 Explore e contribua para os estudos em Django!
