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

    def test_household_help_received_from(self):
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

    def test_household_illness(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_illness_support(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness_support',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_illness_help(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': 'Money'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness_help',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_provider(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': None,
            'household_help_provider': 'Relatives'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_provider',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_review(self):
        options = {
            'bedridden_member': NO,
            'member_age': None,
            'household_help': None,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': None,
            'household_help_provider': None,
            'household_help_review': 'No'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_review',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_received2(self):
        options = {
            'household_help': NO,
            'household_help_received': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_received',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_received_from2(self):
        options = {
            'household_help': NO,
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

    def test_household_illness2(self):
        options = {
            'household_help': NO,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_illness_support2(self):
        options = {
            'household_help': NO,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness_support',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_illness_help2(self):
        options = {
            'household_help': NO,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': 'Yes'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_illness_help',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_provider2(self):
        options = {
            'household_help': NO,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': None,
            'household_help_provider': 'Relatives'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_provider',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)

    def test_household_help_review2(self):
        options = {
            'household_help': NO,
            'household_help_received': None,
            'household_help_received_from': None,
            'household_illness': None,
            'household_illness_support': None,
            'household_illness_help': None,
            'household_help_provider': None,
            'household_help_review': 'No'}
        form_validator = HouseholdMemberFormValidator(
            cleaned_data=options)
        try:
            form_validator.validate()
        except forms.ValidationError:
            pass
        self.assertIn('household_help_review',
                      form_validator._errors)
        self.assertIn(NOT_REQUIRED_ERROR, form_validator._error_codes)
