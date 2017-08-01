from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NEVER, NO
from edc_base.modelform_validators import (REQUIRED_ERROR,
                                           NOT_REQUIRED_ERROR)

from ..form_validations import Section1FormValidator


class TestSection1FormValidator(TestCase):

    def test_respondent_employment_other1(self):
        options = {
            'respondent_employment': OTHER,
            'respondent_employment_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_employment_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_respondent_employment_other2(self):
        options = {
            'respondent_employment': 'Value',
            'respondent_employment_other': 'something'}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_employment_other',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_mine_period(self):
        options = {
            'mine': YES,
            'mine_period': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('mine_period',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_commodity(self):
        options = {
            'mine': YES,
            'mine_period': 1,
            'commodity': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('commodity',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_mine_occupation_other(self):
        options = {
            'mine_occupation': OTHER,
            'mine_occupation_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('mine_occupation_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_commodity_other(self):
        options = {
            'commodity': OTHER,
            'commodity_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('commodity_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_religion_other(self):
        options = {
            'religion': OTHER,
            'religion_other': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('religion_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_respondent_marriage_age(self):
        options = {
            'marital_status': NEVER,
            'respondent_marriage_age': 20}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_marriage_age',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_respondent_married_years(self):
        options = {
            'marital_status': NEVER,
            'respondent_marriage_age': None,
            'respondent_married_years': 1}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('respondent_married_years',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_spouse_visit(self):
        options = {
            'living_with_spouse': NO,
            'spouse_visit': None}
        form_validator = Section1FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('spouse_visit',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
