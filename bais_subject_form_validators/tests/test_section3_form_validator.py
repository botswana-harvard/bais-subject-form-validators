from django import forms
from django.test import TestCase, tag

from edc_constants.constants import YES
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validations import Section3FormValidator


class TestSection3FormValidator(TestCase):

    def test_sexual_intercourse_age(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercourse_age',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_consent(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': 12,
            'sexual_intercouse_consent': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_consent',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercourse_influence(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': 18,
            'sexual_intercouse_consent': YES,
            'sexual_intercourse_influence': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercourse_influence',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': 18,
            'sexual_intercouse_consent': YES,
            'sexual_intercourse_influence': 'Old enough',
            'sexual_intercouse_protection': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_reason(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': 18,
            'sexual_intercouse_consent': YES,
            'sexual_intercourse_influence': 'Old enough',
            'sexual_intercouse_protection': YES,
            'sexual_intercouse_protection_reason': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sex_recently(self):
        options = {
            'sexual_intercouse': YES,
            'sexual_intercourse_age': 18,
            'sexual_intercouse_consent': YES,
            'sexual_intercourse_influence': 'Old enough',
            'sexual_intercouse_protection': YES,
            'sexual_intercouse_protection_reason': 'Family planning',
            'sex_recently': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sex_recently',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
