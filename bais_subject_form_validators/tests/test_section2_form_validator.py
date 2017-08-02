from django import forms
from django.test import TestCase, tag

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

    def test_substance_method_cocaine(self):
        options = {
            'taken_cocaine': YES,
            'substance_method_cocaine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_cocaine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_cocaine(self):
        options = {
            'taken_cocaine': YES,
            'substance_method_cocaine': 'Snort',
            'substance_age_cocaine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_cocaine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_cocaine(self):
        options = {
            'taken_cocaine': YES,
            'substance_method_cocaine': 'Snort',
            'substance_age_cocaine': 21,
            'substance_frequency_cocaine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_cocaine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_crack(self):
        options = {
            'taken_crack': YES,
            'substance_method_crack': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_crack',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_crack(self):
        options = {
            'taken_crack': YES,
            'substance_method_crack': 'Injection',
            'substance_age_crack': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_crack',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_crack(self):
        options = {
            'taken_crack': YES,
            'substance_method_crack': 'Injection',
            'substance_age_crack': 30,
            'substance_frequency_crack': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_crack',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_meth(self):
        options = {
            'taken_meth': YES,
            'substance_method_meth': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_meth',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_meth(self):
        options = {
            'taken_meth': YES,
            'substance_method_meth': 'Injection',
            'substance_age_meth': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_meth',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_meth(self):
        options = {
            'taken_meth': YES,
            'substance_method_meth': 'Injection',
            'substance_age_meth': 10,
            'substance_frequency_meth': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_meth',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_nyaope(self):
        options = {
            'taken_nyaope': YES,
            'substance_method_nyaope': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_nyaope',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_nyaope(self):
        options = {
            'taken_nyaope': YES,
            'substance_method_nyaope': 'Smoking',
            'substance_age_nyaope': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_nyaope',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_nyaope(self):
        options = {
            'taken_nyaope': YES,
            'substance_method_nyaope': 'Smoking',
            'substance_age_nyaope': 18,
            'substance_frequency_nyaope': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_nyaope',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_heroine(self):
        options = {
            'taken_heroine': YES,
            'substance_method_heroine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_heroine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_heroine(self):
        options = {
            'taken_heroine': YES,
            'substance_method_heroine': 'Injection',
            'substance_age_heroine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_heroine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_heroine(self):
        options = {
            'taken_heroine': YES,
            'substance_method_heroine': 'Injection',
            'substance_age_heroine': 12,
            'substance_frequency_heroine': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_heroine',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_method_ecstasy(self):
        options = {
            'taken_ecstasy': YES,
            'substance_method_ecstasy': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_method_ecstasy',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_age_ecstasy(self):
        options = {
            'taken_ecstasy': YES,
            'substance_method_ecstasy': 'Swallow',
            'substance_age_ecstasy': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_age_ecstasy',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_substance_frequency_ecstasy(self):
        options = {
            'taken_ecstasy': YES,
            'substance_method_ecstasy': 'Swallow',
            'substance_age_ecstasy': 16,
            'substance_frequency_ecstasy': None}
        form_validator = Section2FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('substance_frequency_ecstasy',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
