from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NO

from ..constants import YES_LEFT


class HouseholdQuestionnaireFormValidator(FormValidator):

    def clean(self):

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

        return self.cleaned_data
