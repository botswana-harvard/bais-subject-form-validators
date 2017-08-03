from django import forms
from django.test import TestCase, tag

from edc_constants.constants import YES, OTHER, NO, DONT_KNOW
from edc_base.modelform_validators import (
    REQUIRED_ERROR,
    NOT_REQUIRED_ERROR)

from ..form_validations import Section3FormValidator
from ..constants import CONCURRENT


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

    def test_sexual_intercourse_influence_other(self):
        options = {
            'sexual_intercourse_influence': OTHER,
            'sexual_intercourse_influence_other': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercourse_influence_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_use(self):
        options = {
            'sexual_intercouse_protection': YES,
            'sexual_intercouse_protection_use': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_use',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_use_no(self):
        options = {
            'sexual_intercouse_protection': NO,
            'sexual_intercouse_protection_use': 'Condom'}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_use',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_use_dont_know(self):
        options = {
            'sexual_intercouse_protection': DONT_KNOW,
            'sexual_intercouse_protection_use': 'Condom'}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_use',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_use_other(self):
        options = {
            'sexual_intercouse_protection_use': OTHER,
            'sexual_intercouse_protection_use_other': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_use_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sexual_intercouse_protection_reason_other(self):
        options = {
            'sexual_intercouse_protection_reason': OTHER,
            'sexual_intercouse_protection_reason_other': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sexual_intercouse_protection_reason_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sex_consentual(self):
        options = {
            'sex_recently': YES,
            'sex_consentual': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sex_consentual',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sex_with_whom(self):
        options = {
            'sex_recently': YES,
            'sex_consentual': YES,
            'sex_with_whom': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sex_with_whom',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_sex_with_whom_other(self):
        options = {
            'sex_with_whom': OTHER,
            'sex_with_whom_other': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('sex_with_whom_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_assistance_other(self):
        options = {
            'assistance': OTHER,
            'assistance_other': None}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('assistance_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_physical_sexual_violance_who_male(self):
        options = {
            'physical_sexual_violance_male': NO,
            'physical_sexual_violance_who': 'Aobakwe'}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('physical_sexual_violance_who',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_physical_sexual_violance_who_female(self):
        options = {
            'physical_sexual_violance_female': NO,
            'physical_sexual_violance_who': 'Aobakwe'}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('physical_sexual_violance_who',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_partners_serial_concurrent_explain(self):
        options = {
            'partners_serial_concurrent': CONCURRENT,
            'physical_sexual_violance_who': 'Aobakwe'}
        form_validator = Section3FormValidator(cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('partners_serial_concurrent_explain',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
