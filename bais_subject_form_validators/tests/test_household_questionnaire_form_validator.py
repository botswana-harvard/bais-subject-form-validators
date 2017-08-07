from django import forms
from django.test import TestCase

from edc_constants.constants import OTHER, YES, NO
from edc_base.modelform_validators import (
    REQUIRED_ERROR,
    NOT_REQUIRED_ERROR)

from ..constants import YES_LEFT

from ..form_validations import HouseholdQuestionnaireFormValidator


class TestHouseholdQuestionnaireFormValidator(TestCase):

    def test_person_citizenship_other(self):
        options = {
            'person_citizenship': OTHER,
            'person_citizenship_other': None}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_citizenship_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_person_biological_mother_household(self):
        options = {
            'person_biological_mother_alive': YES,
            'person_biological_mother_household': None}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_biological_mother_household',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_person_biological_father_household(self):
        options = {
            'person_biological_father_alive': YES,
            'person_biological_father_household': None}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_biological_father_household',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_person_currently_studying_no(self):
        options = {
            'person_attended_school': NO,
            'person_currently_studying': 'Tertiary'}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_currently_studying',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_person_currently_studying_yes_left(self):
        options = {
            'person_attended_school': YES_LEFT,
            'person_currently_studying': 'Tertiary'}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_currently_studying',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_person_work_unpaid_reason(self):
        options = {
            'person_work_unpaid': YES,
            'person_work_unpaid_reason': None}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_work_unpaid_reason',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)

    def test_person_work_unpaid_reason_other(self):
        options = {
            'person_work_unpaid_reason': OTHER,
            'person_work_unpaid_reason_other': None}
        form_validator = HouseholdQuestionnaireFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('person_work_unpaid_reason_other',
                      form_validator._errors)
        self.assertIn(REQUIRED_ERROR, form_validator._error_codes)
