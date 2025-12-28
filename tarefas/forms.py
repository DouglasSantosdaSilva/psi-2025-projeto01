from django import forms
from .models import Jogador
class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'idade', 'posicao', 'nascimento', 'cidade', 'foto']
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control'}),
            'idade': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'posicao': forms.TextInput(attrs={'placeholder': 'Ex: Atacante', 'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade natal', 'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }