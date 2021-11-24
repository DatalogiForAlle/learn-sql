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

        if "create" in sql.lower():
            raise forms.ValidationError(
                'Du har ikke tilladelse til at udføre CREATE-operationer')

        if "drop" in sql.lower():
            raise forms.ValidationError(
                'Du har ikke tilladelse til at udføre DROP-operationer')

        if "insert" in sql.lower():
            raise forms.ValidationError(
                'Du har ikke tilladelse til at udføre INSERT-operationer')

        if sql.lower()[:6].lower() != 'select':
            raise forms.ValidationError(
                'Kun SELECT-operationer er tilladte')

        return sql
