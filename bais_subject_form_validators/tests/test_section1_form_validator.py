from django.core.exceptions import ValidationError
from django.test import TestCase

from edc_constants.constants import OTHER

from ..form_validations import Section1FormValidator


class TestAdverseEventFormValidator(TestCase):

    def testrespondent_employment_other1(self):
        options = {
            'respondent_employment': OTHER,
            'respondent_employment_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)

    def test_respondent_employment_other2(self):
        options = {
            'respondent_employment': 'Value',
            'respondent_employment_other': 'something'}
        form_validator = Section1FormValidator(cleaned_data=options)
        self.assertRaises(ValidationError, form_validator.clean)
