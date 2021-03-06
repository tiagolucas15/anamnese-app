from datetime import date
from django.db import models
from django.contrib.auth.models import User

from .choices import *

from multiselectfield import MultiSelectField


class Paciente(models.Model):
    cns = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def pode_criar_anamnese(self):
        anamnese = self.anamnese_set.last()
        if anamnese:
            return not anamnese.pode_editar
        return True


class Medico(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    crm = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome


class Anamnese(models.Model):
    paciente = models.ForeignKey(
        Paciente,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    medico_assistente = models.ForeignKey(
        Medico,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='medico_assistente',
    )
    medico = models.ForeignKey(
        Medico,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    dum = models.DateField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.IntegerField(null=True, blank=True)
    alergia = models.TextField(
        null=True,
        blank=True,
        verbose_name='Alergias',
    )
    cafeina = models.BooleanField(null=True, blank=True)
    asma = models.BooleanField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    tipo_exame = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=TIPO_EXAME,
        verbose_name='Tipo de exame',
    )
    cintilografia_adicional = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=CINTILOGRAFIA_ADICIONAL,
    )
    viabilidade_adicional = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=VIABILIDADE_ADICIONAL,
    )
    motivo_exame = MultiSelectField(
        null=True,
        blank=True,
        choices=MOTIVO_EXAME,
        verbose_name='Motivo de exame',
    )
    motivo_exame_outros = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Outros'
    )
    hda = MultiSelectField(
        null=True,
        blank=True,
        choices=HDA,
        verbose_name='Hist??ria da Doen??a Atual'
    )
    hda_outros = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Outros'
    )
    hpp_risco = MultiSelectField(
        null=True,
        blank=True,
        choices=HPP_RISCO,
        verbose_name='Fatores de risco',
    )
    hpp_dac = MultiSelectField(
        null=True,
        blank=True,
        choices=HPP_DAC,
        verbose_name='DAC pr??via',
    )
    hpp_comorbidades = MultiSelectField(
        null=True,
        blank=True,
        choices=HPP_COMORBIDADES,
        verbose_name='Comorbidades',
    )
    hpp_outros = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Outros'
    )
    exames_previos_eco = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_ECO,
        verbose_name='Ecografia',
    )
    exames_previos_fe = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Fra????o de Eje????o (%)'
    )
    exames_previos_te = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_TE,
        verbose_name='Teste Ergom??trico',
    )
    exames_previos_mets = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='MET',
    )
    exames_previos_cat = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_CAT,
        verbose_name='Cateterismo Card??aco',
    )
    exames_previos_tce = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Tronco de Coro??ria Esquerda',
    )
    exames_previos_cm = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_CM,
        verbose_name='Cintilografia Mioc??rdica',
    )
    exames_previos_outros = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Outros'
    )
    medicamentos = MultiSelectField(
        null=True,
        blank=True,
        choices=MEDICAMENTOS,
    )
    medicamentos_outros = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Outros'
    )
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def exame_info_adicional(self):
        exame_adicional = self.viabilidade_adicional
        if self.tipo_exame == 'Cintilografia Mioc??rdica':
            exame_adicional = self.cintilografia_adicional

        return exame_adicional

    @property
    def pode_editar(self):
        tempo_cadastro_dias = (date.today() - self.data_cadastro.date()).days
        return tempo_cadastro_dias <= 1


class FichaAnamnse(models.Model):

    tipo = models.CharField(
        max_length=10,
        choices=FICHAS,
    )
    ficha = models.FileField(upload_to="static/pdfs/")

    def __str__(self):
        return tipo
