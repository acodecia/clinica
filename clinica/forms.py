# clinica/forms.py
from django import forms
from .models import Paciente, Agendamento, Procedimento

class PacienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Formato de SAÍDA: Diz ao Django para renderizar a data como AAAA-MM-DD
            attrs={
                'type': 'date', 
                'class': 'form-control'
            }
        ),
        input_formats=['%Y-%m-%d'] # Formato de ENTRADA: Diz ao Django para ACEITAR este formato ao receber os dados
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'nome': 'Nome Completo',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'endereco': 'Endereço',
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'procedimentos', 'data_hora', 'observacoes', 'status', 'valor_total']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'procedimentos': forms.CheckboxSelectMultiple,
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'valor_total': forms.HiddenInput(),
        }
        labels = {
            'paciente': 'Paciente',
            'procedimentos': 'Selecione os Procedimentos',
            'data_hora': 'Data e Hora',
            'observacoes': 'Observações',
            'status': 'Status do Agendamento',
        }

class ProcedimentoForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['nome', 'descricao', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'nome': 'Nome do Procedimento',
            'descricao': 'Descrição (Opcional)',
            'preco': 'Preço (R$)',
        }

