from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER


class AttitudesTowardsPeopleFormValidator(FormValidator):

    def clean(self):

        req_fields = ['aids_hiv_times_tested',
                      'aids_hiv_test_partner',
                      'aids_hiv_test_reason',
                      'aids_hiv_not_tested']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='aids_hiv_testing',
                field_required=req_field
            )

        self.required_if(
            OTHER,
            field='aids_hiv_test_reason',
            field_required='aids_hiv_test_reason_other',
        )

        self.required_if(
            OTHER,
            field='aids_hiv_not_tested',
            field_required='aids_hiv_not_tested_other',
        )

        self.required_if(
            OTHER,
            field='current_arv_supplier',
            field_required='current_arv_supplier_other',
        )

        req_fields = ['aids_hiv_times_tested',
                      'aids_hiv_test_partner',
                      'aids_hiv_test_reason',
                      'aids_hiv_not_tested']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='aids_hiv_testing',
                field_required=req_field
            )

        self.required_if(
            OTHER,
            field='not_on_arv_therapy',
            field_required='not_on_arv_therapy_other',
        )

        self.required_if(
            OTHER,
            field='tb_reaction',
            field_required='tb_reaction_other',
        )

        return self.cleaned_data
