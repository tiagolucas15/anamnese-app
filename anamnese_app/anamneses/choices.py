TIPO_EXAME = (
    ('Cintilografia Miocárdica', 'Cintilografia Miocárdica'),
    ('Pesquisa de Viabilidade', 'Pesquisa de Viabilidade'),
)

CINTILOGRAFIA_ADICIONAL = (
    ('Protocolo de 1 dia', 'Protocolo de 1 dia'),
    ('Protocolo de 2 dias', 'Protocolo de 2 dias'),
)

VIABILIDADE_ADICIONAL = (
    ('Rep/Redist T', ' Repouso/Redistribuição tardia'),
    ('Est/Redist/Redist T', 'Estresse/Redistribuição/Redistribuição tardia'),
)

MOTIVO_EXAME = (
    ('dor_toracica', 'Dor torácica'),
    ('pos_sca', 'pós Síndrome Coronariana Aguda'),
    ('alteracao_exame', 'Alteração exame'),
    ('equiv_anginoso', 'Equivalente Anginoso'),
    ('pos_crvm', 'pós cirurgia de revascularização do miocárdio'),
    ('lesao_coronaria', 'Lesão coronária'),
    ('arritmia', 'Arritmia'),
    ('pos_ptca', 'pós Angioplastia Coronária Transluminal Percutânea'),
    ('icc', 'Insuficiência Cardíaca Congestiva'),
    ('sincope', 'Síncope'),
    ('risco_cirurgico', 'Risco cirúrgico'),
)

HDA = (
    ('assintomatico', 'Assintomático'),
    ('cansaco', 'Cansaço'),
    ('sincope', 'Síncope'),
    ('dor_toracica_tipica', 'Dor torácica típica'),
    ('dor torarica_atipica', 'Dor torácica atípica'),
    ('dispneia_esforcos', 'Dispnéia aos esforços'),
    ('dispneia_repouso', 'Dispnéia de repouso'),
    ('palpitacoes', 'Palpitações'),
)

HPP_RISCO = (
    ('has', 'Hipertensão Arterial Sistêmica'),
    ('obesidade', 'Obesidade'),
    ('dm', 'Diabetes Mellitus'),
    ('dislipidemia', 'Dislipidemia'),
    ('tabagismo', 'Tabagismo'),
    ('hf', 'Histórico Familiar'),
    ('ex_tabagismo', 'Ex-tabagismo'),
    ('menopausa', 'Menopausa'),
)

HPP_DAC = (
    ('iam', 'Infarto Agudo do Miocárdio'),
    ('crvm', 'Cirurgia de Revascularização do Miocárdio'),
    ('ptca', 'Angioplastia Coronária Transluminal Percutânea'),
    ('cat_alterado', 'Cateterismo Cardíaco alterado'),
)

HPP_COMORBIDADES = (
    ('avc', 'Acidente Vascular Cerebral'),
    ('irc', 'Insuficiência Renal Crônica'),
    ('aao', 'Aneurisma de Aorta'),
    ('doenca_vascular', 'Doença vascular'),
)

EXAMES_PREVIOS_ECO = (
    ('normal', 'Normal'),
    ('alt_segmentar', 'Alteração Segmentar'),
    ('disf_sistolica', 'Disfunção Sistólica'),
    ('disf_diastolica', 'Disfunção diastólicaa'),
)

EXAMES_PREVIOS_TE = (
    ('normal', 'Normal'),
    ('ecg', 'Elétrocardiograma'),
    ('dor', 'Dor'),
    ('arritmia', 'Arritmia'),
    ('baixo_pa', '&#8595 Pressão arterial'),
)

EXAMES_PREVIOS_CAT = (
    ('normal', 'Normal'),    
    ('da', 'Artéria Descendente Anterior'),
    ('cx', 'Artéria Circunflexa'),
    ('cd', 'Coronária Direita'),
    ('saf', 'Safena'),
    ('mam', 'Artéria Mamária'),
)

EXAMES_PREVIOS_CM = (
    ('normal', 'Normal'),
    ('isquemia', 'Isquemia'),
    ('fibrose', 'Fibrose'),
    ('isq_fib', 'Isquemia / Fibrose'),
    ('gated_alt', 'Gated alterado'),
)

MEDICAMENTOS = (
    ('bloq_calcio', 'Bloq. Cálcio'),
    ('aas', 'AAS'),
    ('nitrato', 'Nitrato'),
    ('beta_bloqueador', '&#946-bloqueador'),
    ('estatina', 'Estatina'),
    ('diuretico', 'Diurético'),
    ('bra', 'BRA'),
    ('ieca', 'IECA'),
    ('clopido_rel', 'Clopido.rel'),
)

FICHAS = {
    ('estresse', 'Ficha de Estresse'),
    ('repouso', 'Ficha de Repouso'),
}
