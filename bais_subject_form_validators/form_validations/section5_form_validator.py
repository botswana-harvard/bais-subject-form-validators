from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section5FormValidator(FormValidator):

    def clean(self):

        req_fields = ['tb_recent_information',
                      'tb_information_source']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='tb_awareness',
                field_required=req_field
            )

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
            YES,
            field='tb_curable',
            field_required='tb_cure',
        )

        self.required_if(
            OTHER,
            field='hiv_and_aids_newborn_baby_transmission',
            field_required='hiv_and_aids_newborn_baby_transmission_other',
        )

        req_fields = ['smc_programme_awareness',
                      'smc_programme_source']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='smc_programme',
                field_required=req_field
            )

        self.required_if(
            OTHER,
            field='smc_programme_source',
            field_required='smc_programme_source_other'
        )

        return self.cleaned_data
