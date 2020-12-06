from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('paciente/<str:cns>/', views.paciente, name='paciente'),
    path('cadastrar_paciente/', views.cadastrarPaciente,
         name='cadastrar_paciente'),
    path('cadastrar_paciente/<cns>', views.cadastrarPaciente,
         name='cadastrar_paciente'),
    path('editar_paciente/<str:cns>', views.editarPaciente,
         name='editar_paciente'),
    path('paciente/<str:cns>/cadastrar_anamneses/', views.cadastrarAnamnese,
         name='cadastrar_anamnese'),
    path('paciente/<str:cns>/editar_anamneses/<str:pk>', views.editarAnamnese,
         name='editar_anamnese'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('cadastrar_medico/', views.cadastrarMedico, name='cadastrar_medico'),
    path('upload_ficha/', views.uploadFicha, name='upload_ficha'),
]
