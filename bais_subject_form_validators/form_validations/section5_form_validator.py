from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section5FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='tb_information_source',
            field_required='tb_information_source_other',
        )

        self.required_if(
            OTHER,
            field='tb_prevention',
            field_required='tb_prevention_other',
        )

        self.required_if(
            OTHER,
            field='hiv_and_aids_unborn_baby_transmission',
            field_required='hiv_and_aids_unborn_baby_transmission_other',
        )

        self.required_if(
            OTHER,
            field='hiv_and_aids_newborn_baby_transmission',
            field_required='hiv_and_aids_newborn_baby_transmission_other',
        )

        return self.cleaned_data
