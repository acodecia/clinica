# clinica/models.py
from django.db import models
from django.utils import timezone

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail")
    endereco = models.TextField(blank=True, null=True, verbose_name="Endereço")
    data_cadastro = models.DateTimeField(default=timezone.now, verbose_name="Data de Cadastro")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome']

class Procedimento(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do procedimento")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

    class Meta:
        verbose_name = "Procedimento"
        verbose_name_plural = "Procedimentos"
        ordering = ['nome']

class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('agendado', 'Agendado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="agendamentos")
    procedimentos = models.ManyToManyField(Procedimento, related_name="agendamentos")
    data_hora = models.DateTimeField(verbose_name="Data e Hora do Agendamento")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='agendado')
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    procedimento_realizado = models.BooleanField(default=False, verbose_name="Procedimento já foi realizado?")
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor Total", default=0.00)

    def __str__(self):
        procedimentos_str = ", ".join([p.nome for p in self.procedimentos.all()])
        return f"{self.paciente.nome} - {procedimentos_str} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
        

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ['-data_hora']

