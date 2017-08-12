from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES
from edc_base.modelform_validators import REQUIRED_ERROR

from ..form_validations import KnowledgeAboutHivAndAidsAndTbFormValidator


class TestKnowledgeAboutHivAndAidsAndTbFormValidator(TestCase):

    def test_tb_recent_information(self):
        options = {
            'tb_awareness': YES,
            'tb_recent_information': None}
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
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
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('smc_programme_source_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_arv_sexual_behaviour_yes(self):
        options = {
            'arv_sexual_behaviour': YES,
            'arv_sexual_behaviour_yes': None}
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('arv_sexual_behaviour_yes',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_arv_sexual_behaviour_yes_other(self):
        options = {
            'arv_sexual_behaviour_yes': OTHER,
            'arv_sexual_behaviour_yes_other': None}
        form_validator = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('arv_sexual_behaviour_yes_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
