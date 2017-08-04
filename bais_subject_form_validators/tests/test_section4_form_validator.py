from django import forms
from django.test import TestCase

from edc_constants.constants import YES, NO, OTHER
from edc_base.modelform_validators import (
    REQUIRED_ERROR,
    NOT_REQUIRED_ERROR)

from ..form_validations import Section4FormValidator


class TestSection4FormValidator(TestCase):

    def test_circumcission_year(self):
        options = {
            'circumcission': YES,
            'circumcission_year': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_year',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_reason(self):
        options = {
            'circumcission': YES,
            'circumcission_year': 2017,
            'circumcission_reason': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_place(self):
        options = {
            'circumcission': YES,
            'circumcission_year': 2017,
            'circumcission_reason': 'Medical reasons',
            'circumcission_place': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_place',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcised_complications(self):
        options = {
            'circumcission': YES,
            'circumcission_year': 2017,
            'circumcission_reason': 'Medical reasons',
            'circumcission_place': 'Clinic',
            'circumcised_complications': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcised_complications',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_intent(self):
        options = {
            'circumcission': NO,
            'circumcission_intent': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_intent',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_intent_reason(self):
        options = {
            'circumcission_intent': YES,
            'circumcission_intent_reason': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_intent_reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_intent_reason_other(self):
        options = {
            'circumcission_intent': OTHER,
            'circumcission_intent_reason_other': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_intent_reason_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_reject_reason(self):
        options = {
            'circumcission_intent': NO,
            'circumcission_reject_reason': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_reject_reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_circumcission_reject_reason_other(self):
        options = {
            'circumcission_reject_reason': OTHER,
            'circumcission_reject_reason_other': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('circumcission_reject_reason_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sti_symptoms_other(self):
        options = {
            'sti_symptoms': OTHER,
            'sti_symptoms_other': None}
        form_validator = Section4FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sti_symptoms_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
