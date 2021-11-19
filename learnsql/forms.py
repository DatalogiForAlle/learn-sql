from django import forms


class SqlForm(forms.Form):
    sql = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': '5', 'cols': '200'},
        ),
        required=True,
        label="Indtast en SQL-forespørgsel i boksen og tryk på 'send'",
        help_text="")
