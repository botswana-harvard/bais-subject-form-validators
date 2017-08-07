from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NO

from ..constants import YES_LEFT


class HouseholdQuestionnaireFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='person_citizenship',
            field_required='person_citizenship_other',
        )

        self.required_if(
            YES,
            field='person_biological_mother_alive',
            field_required='person_biological_mother_household',
        )

        self.required_if(
            YES,
            field='person_biological_father_alive',
            field_required='person_biological_father_household',
        )

        self.not_required_if(
            NO,
            field='person_attended_school',
            field_required='person_currently_studying',
        )

        self.not_required_if(
            YES_LEFT,
            field='person_attended_school',
            field_required='person_currently_studying',
        )

        self.required_if(
            YES,
            field='person_work_unpaid',
            field_required='person_work_unpaid_reason',
        )

        self.required_if(
            OTHER,
            field='person_work_unpaid_reason',
            field_required='person_work_unpaid_reason_other',
        )

        return self.cleaned_data
