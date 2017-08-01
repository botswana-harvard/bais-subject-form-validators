from django import forms
from django.test import TestCase

from edc_constants.constants import YES
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validations import Section2FormValidator


class TestSection2FormValidator(TestCase):

    def test_substance_method_alcohol(self):
        options = {
            'taken_alcohol': YES,
            'substance_method_alcohol': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_alcohol',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_alcohol(self):
        options = {
            'taken_alcohol': YES,
            'substance_method_alcohol': 'Drinking',
            'substance_age_alcohol': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_alcohol',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_alcohol(self):
        options = {
            'taken_alcohol': YES,
            'substance_method_alcohol': 'Drinking',
            'substance_age_alcohol': 12,
            'substance_frequency_alcohol': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_alcohol',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_tobacco(self):
        options = {
            'taken_tobacco': YES,
            'substance_method_tobacco': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_tobacco',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_tobacco(self):
        options = {
            'taken_tobacco': YES,
            'substance_method_tobacco': 'Smoking',
            'substance_age_tobacco': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_tobacco',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_tobacco(self):
        options = {
            'taken_tobacco': YES,
            'substance_method_tobacco': 'Smoking',
            'substance_age_tobacco': 13,
            'substance_frequency_tobacco': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_tobacco',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_marijuana(self):
        options = {
            'taken_marijuana': YES,
            'substance_method_marijuana': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_marijuana',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_marijuana(self):
        options = {
            'taken_marijuana': YES,
            'substance_method_marijuana': 'Smoking',
            'substance_age_marijuana': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_marijuana',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_marijuanaa(self):
        options = {
            'taken_marijuana': YES,
            'substance_method_marijuana': 'Smoking',
            'substance_age_marijuana': 18,
            'substance_frequency_marijuana': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_marijuana',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
