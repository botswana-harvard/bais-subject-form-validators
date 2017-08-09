from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section5FormValidator


class TestSection5FormValidator(TestCase):

    def test_tb_recent_information(self):
        options = {
            'tb_awareness': YES,
            'tb_recent_information': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_recent_information',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_information_source(self):
        options = {
            'tb_awareness': YES,
            'tb_recent_information': YES,
            'tb_information_source': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_information_source',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_tb_information_source_other(self):
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

    def test_tb_prevention_other(self):
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

    def test_sexual_intercourse_age(self):
        options = {
            'tb_curable': YES,
            'tb_cure': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('tb_cure',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_hiv_and_aids_unborn_baby_transmission_other(self):
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

    def test_hiv_and_aids_newborn_baby_transmission_other(self):
        options = {
            'hiv_and_aids_newborn_baby_transmission': OTHER,
            'hiv_and_aids_newborn_baby_transmission_other': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('hiv_and_aids_newborn_baby_transmission_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_programme_awareness(self):
        options = {
            'smc_programme': YES,
            'smc_programme_awareness': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('smc_programme_awareness',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_smc_programme_source(self):
        options = {
            'smc_programme': YES,
            'smc_programme_awareness': YES,
            'smc_programme_source': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('smc_programme_source',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_smc_programme_source_other(self):
        options = {
            'smc_programme_source': OTHER,
            'smc_programme_source_other': None}
        form_validator = Section5FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('smc_programme_source_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
