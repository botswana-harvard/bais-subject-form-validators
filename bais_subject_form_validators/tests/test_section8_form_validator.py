from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section8FormValidator


class TestSection8FormValidator(TestCase):

    def test_tb_sputum_sample_result_other1(self):
        options = {
            'tb_sputum_sample_result': OTHER,
            'tb_sputum_sample_result_other': None}
        form_validator = Section8FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_sputum_sample_result_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_sputum_sample_result_other2(self):
        options = {
            'tb_sputum_sample_no_result': 'Value',
            'tb_sputum_sample_no_result_other': 'word of mouth'}
        form_validator = Section8FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_sputum_sample_no_result_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

#
    def test_tb_sputum_sample_no_result_other1(self):
        options = {
            'tb_sputum_sample_no_result': OTHER,
            'tb_sputum_sample_no_result_other': None}
        form_validator = Section8FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_sputum_sample_no_result_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_sputum_sample_no_result_other2(self):
        options = {
            'tb_sputum_sample_no_result': 'Value',
            'tb_sputum_sample_no_result_other': 'word of mouth'}
        form_validator = Section8FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_sputum_sample_no_result_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
