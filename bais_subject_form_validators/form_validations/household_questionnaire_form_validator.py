from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES


class HouseholdQuestionnaireFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='person_citizenship',
            field_required='person_citizenship_other',
        )

        self.required_if(
            YES,
            field='person_citizenship',
            field_required='person_citizenship_other',
        )

        return self.cleaned_data
