from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section5FormValidator


class TestSection5FormValidator(TestCase):

    def test_tb_information_source_other1(self):
        options = {
            'tb_information_source': OTHER,
            'tb_information_source_other': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_information_source_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_information_source_other2(self):
        options = {
            'tb_information_source': 'Value',
            'tb_information_source_other': 'word of mouth'}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_information_source_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_prevention_other1(self):
        options = {
            'tb_prevention': OTHER,
            'tb_prevention_other': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_prevention_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_prevention_other2(self):
        options = {
            'tb_prevention': 'Value',
            'tb_prevention_other': 'word of mouth'}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_prevention_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_hiv_and_aids_unborn_baby_transmission_other1(self):
        options = {
            'hiv_and_aids_unborn_baby_transmission': OTHER,
            'hiv_and_aids_unborn_baby_transmission_other': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('hiv_and_aids_unborn_baby_transmission_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_hiv_and_aids_unborn_baby_transmission_other2(self):
        options = {
            'hiv_and_aids_unborn_baby_transmission': 'Value',
            'hiv_and_aids_unborn_baby_transmission_other': 'word of mouth'}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('hiv_and_aids_unborn_baby_transmission_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
