from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section6FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='aids_hiv_test_reason',
            field_required='aids_hiv_test_reason_other',
        )
