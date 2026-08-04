import requests as req
from dotenv import load_dotenv
from django.shortcuts import render
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

# Criar uma forma de armazenar tudo em um DB e atualizar de tempos em tempos
def extrairProjetos():
    response = req.get("https://api.github.com/users/Lcs154/repos")
    data = response.json()

    projetos = []
    for projeto in data:
        projetos.append({
            "name": projeto['name'],
            "url": projeto['html_url'],
            "description": projeto['description']
        })

    return projetos

def enviarEmail(nome, remetente, assunto, texto):
    email_from = os.getenv('EMAIL_FROM')    # site
    email_to = os.getenv('EMAIL_TO')        # pessoal
    senha_app = os.getenv('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Reply-To'] = remetente

    msg.set_content(f'''
Nome: {nome}
Email: {remetente}

Mensagem:
{texto}
''')
    
    msg['X-Mailer'] = 'Python SMTP'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_from, senha_app)
            server.send_message(msg)

    except Exception as err:
        print(err)

def responderEmail():
    '''Envia uma resposta para o remetente'''
# Agradeço por entrar em contato, em breve retorno com uma resposta
    pass

def home(request):
    # forma incorreta, com grande volume de pessoas sobrecarregaria a API e o projeto
    # Futuro - Arrumar nova forma de extrair
    projetos = extrairProjetos()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email_remetente = request.POST.get('email')
        assunto = request.POST.get('assunto')
        texto = request.POST.get('texto')

        enviarEmail(nome,email_remetente, assunto, texto)

    return render(request, "portifolio/home.html", {"projetos": projetos})