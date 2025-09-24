# clinica/urls.py
from django.urls import path
from .views import PacienteListView, PacienteCreateView, AgendamentoListView, AgendamentoCreateView, AgendamentoDetailView, AgendamentoUpdateView, PacienteDetailView, PacienteUpdateView, ProcedimentoListView, ProcedimentoCreateView, ProcedimentoUpdateView, ProcedimentoDeleteView

urlpatterns = [
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/novo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('agendamentos/', AgendamentoListView.as_view(), name='agendamento_list'),
    path('agendamentos/novo/', AgendamentoCreateView.as_view(), name='agendamento_create'),
    path('agendamentos/<int:pk>/', AgendamentoDetailView.as_view(), name='agendamento_detail'),
    path('agendamentos/<int:pk>/editar/', AgendamentoUpdateView.as_view(), name='agendamento_update'),
    path('procedimentos/', ProcedimentoListView.as_view(), name='procedimento_list'),
    path('procedimentos/novo/', ProcedimentoCreateView.as_view(), name='procedimento_create'),
    path('procedimentos/<int:pk>/editar/', ProcedimentoUpdateView.as_view(), name='procedimento_update'),
    path('procedimentos/<int:pk>/excluir/', ProcedimentoDeleteView.as_view(), name='procedimento_delete'),
]
  
    # Adicione mais URLs conforme for criando mais views
