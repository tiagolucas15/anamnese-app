# Generated by Django 3.0.8 on 2020-11-02 23:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('anamneses', '0004_auto_20201102_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='motivo_exame',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('dor_toráxica', 'Dor toráxica'), ('pos_sca', 'pós-SCA'), ('alteracao_exame', 'Alteração exame'), ('equiv_anginoso', 'Equiv. anginoso'), ('pos_crvm', 'pós-CRVM'), ('lesao_coronaria', 'Lesão coronária'), ('arritmia', 'Arritmia'), ('pos_ptca', 'pós-PTCA'), ('icc', 'ICC'), ('sincope', 'Síncope'), ('risco_cirurgico', 'Risco cirúrgico')], max_length=122, null=True),
        ),
    ]
