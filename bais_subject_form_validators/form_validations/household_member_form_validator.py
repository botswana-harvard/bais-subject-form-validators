from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NO

from ..constants import YES_LEFT


class HouseholdQuestionnaireFormValidator(FormValidator):

    def clean(self):

        req_fields = [
            'household_help_received',
            'household_help_received_from',
            'household_illness',
            'household_illness_support',
            'household_illness_help',
            'household_help_provider',
            'household_help_review', ]
        for req_field in req_fields:
            self.not_required_if(
                NO,
                field='household_help',
                field_required=req_field,
            )

        self.required_if(
            OTHER,
            field='household_help_received',
            field_required='household_help_received_other',
        )

        self.required_if(
            OTHER,
            field='household_help_received_from',
            field_required='household_help_received_from_other',
        )

        self.required_if(
            OTHER,
            field='household_illness_help',
            field_required='household_illness_help_other',
        )

        self.not_required_if(
            NO,
            field='household_deaths',
            field_required='household_deaths_review',
        )

        return self.cleaned_data
