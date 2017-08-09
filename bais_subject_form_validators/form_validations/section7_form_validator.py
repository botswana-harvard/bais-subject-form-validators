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

        req_fields = ['baby_hiv_test_result',
                      'baby_arv']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='baby_hiv_test',
                field_required=req_field
            )

        return self.cleaned_data
