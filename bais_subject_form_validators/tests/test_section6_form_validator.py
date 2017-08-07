from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section6FormValidator


class TestSection6FormValidator(TestCase):

    def test_aids_hiv_test_reason_other1(self):
        options = {
            'aids_hiv_test_reason': OTHER,
            'aids_hiv_test_reason_other': None}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('aids_hiv_test_reason_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_aids_hiv_test_reason_other2(self):
        options = {
            'aids_hiv_test_reason': 'Value',
            'aids_hiv_test_reason_other': 'Chronic Sickness'}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('aids_hiv_test_reason_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

#
    def test_aids_hiv_not_tested_other1(self):
        options = {
            'aids_hiv_not_tested': OTHER,
            'aids_hiv_not_tested_other': None}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('aids_hiv_not_tested_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_aids_hiv_not_tested_other2(self):
        options = {
            'aids_hiv_not_tested': 'Value',
            'aids_hiv_not_tested_other': 'No Access'}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('aids_hiv_not_tested_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_current_arv_supplier_other1(self):
        options = {
            'current_arv_supplier': OTHER,
            'current_arv_supplier_other': None}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('current_arv_supplier_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_current_arv_supplier_other2(self):
        options = {
            'current_arv_supplier': 'Value',
            'current_arv_supplier_other': 'Clinic'}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('current_arv_supplier_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_not_on_arv_therapy_other1(self):
        options = {
            'not_on_arv_therapy': OTHER,
            'not_on_arv_therapy_other': None}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('not_on_arv_therapy_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_not_on_arv_therapy_other2(self):
        options = {
            'not_on_arv_therapy': 'Value',
            'not_on_arv_therapy_other': 'allergies'}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('not_on_arv_therapy_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_reaction_other1(self):
        options = {
            'tb_reaction': OTHER,
            'tb_reaction_other': None}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_reaction_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_reaction_other2(self):
        options = {
            'tb_reaction': 'Value',
            'tb_reaction_other': 'Scared'}
        form_validator = Section6FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_reaction_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
