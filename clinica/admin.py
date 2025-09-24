# clinica/admin.py
from django.contrib import admin
from .models import Paciente, Procedimento, Agendamento

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'data_cadastro')
    search_fields = ('nome', 'email', 'telefone')
    list_filter = ('data_cadastro',)

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    # 1. 'procedimento' foi removido da lista de exibição.
    #    Adicionamos 'valor_total' que é mais útil aqui.
    list_display = ('paciente', 'data_hora', 'status', 'valor_total')
    
    # 2. A busca agora usa o nome plural 'procedimentos'.
    search_fields = ('paciente__nome', 'procedimentos__nome')
    
    # 3. O filtro também usa o nome plural 'procedimentos'.
    list_filter = ('status', 'data_hora', 'procedimentos')
    
    # 4. 'procedimento' foi REMOVIDO daqui.
    #    autocomplete_fields não é compatível com o campo ManyToMany.
    autocomplete_fields = ['paciente']
    
    # 5. Esta é a FORMA CORRETA de exibir o campo ManyToMany 'procedimentos'.
    filter_horizontal = ('procedimentos',)