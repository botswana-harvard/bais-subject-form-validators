from django import forms
from django.test import TestCase

from edc_constants.constants import YES, NO, OTHER
from edc_base.modelform_validators import REQUIRED_ERROR, NOT_REQUIRED_ERROR

from ..form_validations import HouseholdMemberFormValidator


class TestHouseholdMemberFormValidator(TestCase):

    def test_member_age(self):
        options = {
            'bedridden_member': NO,
            'member_age': 22}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('member_age',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_received(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': 'Counseling'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_received',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_recieved_from(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': 'Clinic'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_received_from',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
