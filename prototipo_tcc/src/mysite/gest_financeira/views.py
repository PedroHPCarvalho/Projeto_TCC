import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
from .models import Registros
from .gpt_api import go_ia

# Create your views here.


@login_required(login_url='login')  # redireciona para a rota 'login' se não estiver autenticado
def home(request):
    registros = Registros.objects.filter(id_user=request.user)
    gastos_totais = Registros.objects.filter(id_user=request.user, type_register__iexact='saída').aggregate(total=Sum('amount'))['total'] or 0
    entradas_totais = Registros.objects.filter(id_user=request.user, type_register__iexact='entrada').aggregate(total=Sum('amount'))['total'] or 0
    orcamento_livre = entradas_totais - gastos_totais
    contexto_pag = {
        'registros': registros,
        'gastos_totais': gastos_totais,
        'entradas_totais': entradas_totais,
        'orcamento_livre': orcamento_livre
    }
    return render(request, "gest_financeira/home.html", contexto_pag)


@login_required(login_url='login')  # redireciona para a rota 'login' se não estiver autenticado
def process_chat(request):
    if request.method == "POST":
        mensagem = request.POST.get("mensagem", "")
        response_ia = go_ia(mensagem)
        response_ia_json = response_ia.choices[0].message.content
        if response_ia_json:
            try:
                dados = json.loads(response_ia_json)
            except json.JSONDecodeError:
                dados = {"error": "Resposta da IA não é um JSON válido."}
        else:
            dados = {"error": "Resposta vazia da IA."}

        campos_obrigatorios = ['date', 'amount', 'description', 'category', 'type_register']
        if all(campo in dados and dados[campo] for campo in campos_obrigatorios):
            Registros.objects.create(
                id_user=request.user,
                description=dados['description'],
                category=dados['category'],
                type_register=dados['type_register'],
                amount=dados['amount'],
                date=dados['date']
            )
            return JsonResponse({"mensagem": "Registro inserido com sucesso!", "status": "ok"})
        else:
            return JsonResponse({"mensagem": "Erro: JSON incompleto ou inválido.", "status": "erro"})
        
