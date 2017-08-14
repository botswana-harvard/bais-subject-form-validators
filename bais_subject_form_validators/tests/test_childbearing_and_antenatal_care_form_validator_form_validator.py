from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, NO, YES
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import ChildbearingAndAntenatalCareFormValidator


class TestChildbearingAndAntenatalCareFormValidator(TestCase):

    def test_baby_hiv_test_result(self):
        options = {
            'baby_hiv_test': NO,
            'baby_hiv_test_result': 'Positive'}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('baby_hiv_test_result',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_baby_arv(self):
        options = {
            'baby_hiv_test': NO,
            'baby_hiv_test_result': None,
            'baby_arv': 'Yes'}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('baby_arv',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic(self):
        options = {
            'currently_pregnant': YES,
            'ante_natal_clinic': None}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic_none(self):
        options = {
            'currently_pregnant': YES,
            'ante_natal_clinic': YES,
            'ante_natal_clinic_none': None}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_none',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic_none_other1(self):
        options = {
            'ante_natal_clinic_none': OTHER,
            'ante_natal_clinic_none_other': None}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
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
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_none_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_ante_natal_clinic_test(self):
        options = {
            'ante_natal_clinic_test': YES,
            'ante_natal_clinic_test_result': None}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_test_result',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

#
    def test_ante_natal_clinic_partner_test(self):
        options = {
            'ante_natal_clinic_partner_test': YES,
            'ante_natal_clinic_partner_test_result': None}
        form_validator = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('ante_natal_clinic_partner_test_result',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
