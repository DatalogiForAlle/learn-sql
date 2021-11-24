# Create your tests here.
from django.test import TestCase
from ..forms import SqlForm
from django.core.exceptions import ValidationError


class SqlFormtests(TestCase):

    def test_insert_forbidden_upper_case(self):
        """ INSERT statements are invalid """
        sql = "blah blah INSERT blah blah"
        form = SqlForm(data={'sql': sql})

        is_valid = form.is_valid()

        self.assertFalse(is_valid)
        assert 'Du har ikke tilladelse til at udføre INSERT-operationer' in str(
            form.errors)

    def test_insert_forbidden_lower_case(self):
        """ INSERT statements are invalid - also in uppercase """
        sql = "blah blah insert blah blah"
        form = SqlForm(data={'sql': sql})

        is_valid = form.is_valid()

        self.assertFalse(is_valid)
        assert 'Du har ikke tilladelse til at udføre INSERT-operationer' in str(
            form.errors)

    def test_create_forbidden(self):
        """ CREATE statements are invalid """
        sql = "blah blah cReate blah blah"
        form = SqlForm(data={'sql': sql})

        is_valid = form.is_valid()

        self.assertFalse(is_valid)
        assert 'Du har ikke tilladelse til at udføre CREATE-operationer' in str(
            form.errors)

    def test_must_start_with_select(self):
        """ Sql statements must start with 'SELECT' """
        sql = "blah blah blah"
        form = SqlForm(data={'sql': sql})

        is_valid = form.is_valid()

        self.assertFalse(is_valid)
        assert 'Kun SELECT-operationer er tilladte' in str(
            form.errors)
