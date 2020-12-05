from datetime import date
from django.db import models
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
    crm = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)
    senha = models.CharField(max_length=50)

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
        verbose_name='DAC prévia',
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
        verbose_name='ECO',
    )
    exames_previos_fe = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='FE'
    )
    exames_previos_te = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_TE,
        verbose_name='TE',
    )
    exames_previos_mets = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='METs',
    )
    exames_previos_cat = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_CAT,
        verbose_name='CAT',
    )
    exames_previos_tce = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='TCE',
    )
    exames_previos_cm = MultiSelectField(
        null=True,
        blank=True,
        choices=EXAMES_PREVIOS_CM,
        verbose_name='CM',
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
        if self.tipo_exame == 'Cintilografia Miocárdica':
            exame_adicional = self.cintilografia_adicional

        return exame_adicional

    @property
    def pode_editar(self):
        tempo_cadastro_dias = (date.today() - self.data_cadastro.date()).days
        return tempo_cadastro_dias <= 1
