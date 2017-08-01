from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER
from edc_base.modelform_validators import REQUIRED_ERROR, NOT_REQUIRED_ERROR

from ..form_validations import Section1FormValidator


class TestAdverseEventFormValidator(TestCase):

    def testrespondent_employment_other1(self):
        options = {
            'respondent_employment': OTHER,
            'respondent_employment_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_employment_other', form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_respondent_employment_other2(self):
        options = {
            'respondent_employment': 'Value',
            'respondent_employment_other': 'something'}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_employment_other', form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
