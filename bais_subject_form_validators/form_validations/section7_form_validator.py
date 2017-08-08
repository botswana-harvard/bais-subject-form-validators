from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section7FormValidator(FormValidator):

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

#         self.required_if(
#             OTHER,
#             field='hiv_and_aids_unborn_baby_transmission',
#             field_required='hiv_and_aids_unborn_baby_transmission_other',
#         )

        return self.cleaned_data
