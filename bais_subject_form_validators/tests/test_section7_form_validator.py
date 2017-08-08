from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section7FormValidator


class TestSection7FormValidator(TestCase):

    def test_ante_natal_clinic_none_other1(self):
        options = {
            'ante_natal_clinic_none': OTHER,
            'ante_natal_clinic_none_other': None}
        form_validator = Section7FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_none_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic_none_other2(self):
        options = {
            'ante_natal_clinic_none': 'Value',
            'ante_natal_clinic_none_other': 'cant afford'}
        form_validator = Section7FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_none_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

#
    def test_ante_natal_clinic_test_other1(self):
        options = {
            'ante_natal_clinic_test': OTHER,
            'ante_natal_clinic_test_other': None}
        form_validator = Section7FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_test_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic_test_other2(self):
        options = {
            'ante_natal_clinic_none': 'Value',
            'ante_natal_clinic_none_other': 'confidential'}
        form_validator = Section7FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_test_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
