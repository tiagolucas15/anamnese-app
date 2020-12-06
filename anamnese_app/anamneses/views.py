from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .serializers import *
from .decorators import *


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        form = LoginForm()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')

            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('inicio')
            else:
                messages.info(request, 'CRM ou Senha incorreto')

        context = {
            'form': form,
        }

        return render(request, 'anamneses/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@usuario_admin
def cadastrarMedico(request):
    form = CriarUsuarioForm()

    if request.method == 'POST':
        crm = request.POST.get('username')
        nome = request.POST.get('nome')

        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Medico.objects.create(
                user=user,
                crm=crm,
                nome=nome,
            )
            messages.success(
                request, f'Médico(a) {nome} cadastrado com sucesso!')
            return redirect('inicio')

    context = {'form': form}
    return render(request, 'anamneses/medico_form.html', context)


def home(request):
    if request.method == 'GET':
        search_value = request.GET.get('search-bar', None)

        if not search_value:
            return render(request, 'anamneses/home.html')

        paciente = Paciente.objects.filter(cns=search_value).first()

        if paciente:
            return redirect('paciente', search_value)
        else:
            messages.info(request, 'Não há pacientes com esse CNS cadastrado.')
            return redirect('cadastrar_paciente', search_value)


def paciente(request, cns):
    paciente = Paciente.objects.get(cns=cns)
    anamneses = paciente.anamnese_set.all().order_by('-data_cadastro')
    anamnese_atual = anamneses.first()
    context = {
        'anamnese_atual': anamnese_atual,
        'anamneses': anamneses[1:],
        'paciente': paciente,
    }

    return render(request, 'anamneses/paciente_file.html', context)


def cadastrarPaciente(request, cns=None):
    form = PacienteForm(initial={'cns': cns})

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            paciente_nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'Paciente {paciente_nome} foi cadastrado com sucesso!')
            return redirect('paciente', cns=paciente.cns)

    context = {
        'form': form,
        'title': 'Cadastrar Paciente',
    }

    return render(request, 'anamneses/paciente_form.html', context)


@login_required(login_url='login')
def editarPaciente(request, cns):
    paciente = Paciente.objects.get(cns=cns)
    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save()
            paciente_nome = form.cleaned_data.get('nome')
            messages.success(
                request, f'O paciente {paciente_nome} foi editado com sucesso!')
            return redirect('paciente', cns=paciente.cns)

    context = {
        'form': form,
        'title': 'Editar Paciente',
    }

    return render(request, 'anamneses/paciente_form.html', context)


@login_required(login_url='login')
def cadastrarAnamnese(request, cns):
    AnamneseFormSet = inlineformset_factory(
        Paciente,
        Anamnese,
        exclude=('paciente',),
        extra=1,
    )
    paciente = Paciente.objects.get(cns=cns)

    formset = AnamneseFormSet(
        queryset=Anamnese.objects.none(),
        instance=paciente,
    )

    if request.method == 'POST':
        formset = AnamneseFormSet(request.POST, instance=paciente)
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                f'Anamnese cadastrada para o paciente {paciente.nome} com sucesso!'
            )
            return redirect('paciente', cns=cns)

    context = {
        'formset': formset,
        'title': 'Cadastrar Anamnese',
        'paciente': paciente,
    }

    return render(request, 'anamneses/anamnese_form.html', context)


@login_required(login_url='login')
def editarAnamnese(request, cns, pk):
    AnamneseFormSet = inlineformset_factory(
        Paciente,
        Anamnese,
        exclude=('paciente',),
        extra=0,
    )
    paciente = Paciente.objects.get(cns=cns)
    anamnese_queryset = Anamnese.objects.filter(pk=pk)
    anamnese_instance = anamnese_queryset.get()

    formset = AnamneseFormSet(
        queryset=anamnese_queryset,
        instance=paciente
    )
    if request.method == 'POST':
        formset = AnamneseFormSet(request.POST, instance=paciente)
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                f'Anamnese editada para o paciente {paciente.nome} com sucesso!'
            )
            return redirect('paciente', cns=cns)

    checked_motivo_exame = anamnese_instance.motivo_exame
    checked_hda = anamnese_instance.hda
    checked_hpp_risco = anamnese_instance.hpp_risco
    checked_hpp_dac = anamnese_instance.hpp_dac
    checked_hpp_comorbidades = anamnese_instance.hpp_comorbidades
    checked_exames_previos_eco = anamnese_instance.exames_previos_eco
    checked_exames_previos_te = anamnese_instance.exames_previos_te
    checked_exames_previos_cat = anamnese_instance.exames_previos_cat
    checked_exames_previos_cm = anamnese_instance.exames_previos_cm
    checked_exames_previos_fe = anamnese_instance.exames_previos_fe
    checked_exames_previos_mets = anamnese_instance.exames_previos_mets
    checked_exames_previos_tce = anamnese_instance.exames_previos_tce
    checked_medicamentos = anamnese_instance.medicamentos

    context = {
        'formset': formset,
        'title': 'Editar Anamnese',
        'paciente': paciente,
        'checked_motivo_exame': checked_motivo_exame,
        'checked_hda': checked_hda,
        'checked_hpp_risco': checked_hpp_risco,
        'checked_hpp_dac': checked_hpp_dac,
        'checked_hpp_comorbidades': checked_hpp_comorbidades,
        'checked_exames_previos_eco': checked_exames_previos_eco,
        'checked_exames_previos_te': checked_exames_previos_te,
        'checked_exames_previos_cat': checked_exames_previos_cat,
        'checked_exames_previos_cm': checked_exames_previos_cm,
        'checked_exames_previos_fe': checked_exames_previos_fe,
        'checked_exames_previos_tce': checked_exames_previos_tce,
        'checked_medicamentos': checked_medicamentos,
    }

    return render(request, 'anamneses/anamnese_form.html', context)


@usuario_admin
def uploadFicha(request):
    if request.method == 'POST':
        form = UploadFichaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ficha salva!')
            return redirect('inicio')

    else:
        form = UploadFichaForm()
        context = {
            'form': form,
        }
    return render(request, 'anamneses/upload_ficha.html', context)
