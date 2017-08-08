from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section8FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='ante_natal_clinic_none',
            field_required='ante_natal_clinic_none_other',
        )

        self.required_if(
            OTHER,
            field='ante_natal_clinic_test',
            field_required='ante_natal_clinic_test_other',
        )