from django import forms

from .models import RegistroCheckIn


class RegistroCheckInForm(forms.ModelForm):
    percepcao = forms.ChoiceField(
        choices=RegistroCheckIn.Percepcao.choices,
        widget=forms.RadioSelect,
        label='Como você está se sentindo hoje?',
    )

    class Meta:
        model = RegistroCheckIn
        fields = ('percepcao', 'observacao')
        labels = {
            'observacao': 'Quer registrar alguma observação?',
        }
        widgets = {
            'observacao': forms.Textarea(attrs={
                'rows': 4,
                'maxlength': 500,
                'placeholder': 'Escreva uma observação, se desejar.',
                'aria-describedby': 'observacao-ajuda',
            }),
        }
