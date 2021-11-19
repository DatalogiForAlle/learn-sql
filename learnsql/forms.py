from django import forms
from django.core.exceptions import ValidationError


class SqlForm(forms.Form):
    sql = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': '5', 'cols': '200'},
        ),
        required=True,
        label="Indtast en SQL-forespørgsel i boksen og tryk på 'send'",
        help_text="")

    def clean_sql(self):
        sql = self.cleaned_data['sql']

        if "delete" in sql.lower():
            raise forms.ValidationError(
                'Du har ikke tilladelse til at udføre DELETE-operationer')

        if "update" in sql.lower():
            raise forms.ValidationError(
                'Du har ikke tilladelse til at udføre UPDATE-operationer')
        return sql
