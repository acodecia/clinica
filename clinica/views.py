# clinica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Paciente, Agendamento, Procedimento
from .forms import PacienteForm, AgendamentoForm, ProcedimentoForm


# View para listar pacientes
class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/paciente_list.html' # Nome do template que vamos criar
    context_object_name = 'pacientes' # Nome da variável no template

# View para adicionar um novo paciente
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html' # Nome do template do formulário
    success_url = reverse_lazy('paciente_list') # Redireciona para a lista de pacientes após salvar

    def form_valid(self, form):
        messages.success(self.request, "✅ Paciente cadastrado com sucesso!")
        response = super().form_valid(form)
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "❌ Erro ao salvar o paciente. Verifique os campos e tente novamente.")
        return super().form_invalid(form)
    
# View para listar agendamentos
class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'clinica/agendamento_list.html'
    context_object_name = 'agendamentos'
    # Podemos adicionar um filtro para ordenar ou exibir apenas agendamentos futuros
    queryset = Agendamento.objects.all().order_by('data_hora')

# View para adicionar um novo agendamento
class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'clinica/agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

    def form_valid(self, form):
        # Primeiro, salva o formulário sem salvar no banco ainda
        agendamento = form.save(commit=False)
        agendamento.save() # Salva o agendamento para ter um ID

        # Agora, processa os procedimentos
        procedimentos = form.cleaned_data['procedimentos']
        valor_total = 0
        for procedimento in procedimentos:
            valor_total += procedimento.preco
        
        agendamento.procedimentos.set(procedimentos) # Adiciona os procedimentos
        agendamento.valor_total = valor_total # Define o valor total
        agendamento.save() # Salva novamente com o valor total

        return super().form_valid(form)

class AgendamentoDetailView(DetailView):
    model = Agendamento
    template_name = 'clinica/agendamento_detail.html'
    context_object_name = 'agendamento'

class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'clinica/agendamento_form.html'
    success_url = reverse_lazy('agendamento_list')

    def form_valid(self, form):
        # Lógica idêntica à de criação
        agendamento = form.save(commit=False)
        
        procedimentos = form.cleaned_data['procedimentos']
        valor_total = 0
        for procedimento in procedimentos:
            valor_total += procedimento.preco
        
        agendamento.valor_total = valor_total
        agendamento.save()
        agendamento.procedimentos.set(procedimentos)

        return super().form_valid(form)

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'clinica/paciente_detail.html'
    context_object_name = 'paciente'

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html' # Reutilizamos o mesmo template!

    def form_valid(self, form):
        messages.success(self.request, "✅ Paciente alterado com sucesso!")
        response = super().form_valid(form)
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "❌ Erro ao salvar o paciente. Verifique os campos e tente novamente.")
        return super().form_invalid(form)

    def get_success_url(self):
        # Após editar com sucesso, redireciona para a página de detalhes do paciente editado
        return reverse_lazy('paciente_detail', kwargs={'pk': self.object.pk})

class ProcedimentoListView(ListView):
    model = Procedimento
    template_name = 'clinica/procedimento_list.html'
    context_object_name = 'procedimentos'

class ProcedimentoCreateView(CreateView):
    model = Procedimento
    form_class = ProcedimentoForm
    template_name = 'clinica/procedimento_form.html'
    success_url = reverse_lazy('procedimento_list')

class ProcedimentoUpdateView(UpdateView):
    model = Procedimento
    form_class = ProcedimentoForm
    template_name = 'clinica/procedimento_form.html'
    success_url = reverse_lazy('procedimento_list')

class ProcedimentoDeleteView(DeleteView):
    model = Procedimento
    template_name = 'clinica/procedimento_confirm_delete.html'
    success_url = reverse_lazy('procedimento_list')

# Você pode adicionar mais views aqui, como detalhes do paciente, editar paciente, etc.

