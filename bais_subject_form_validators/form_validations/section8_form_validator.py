from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER


class Section8FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='tb_sputum_sample_result',
            field_required='tb_sputum_sample_result_other',
        )

        self.required_if(
            OTHER,
            field='tb_sputum_sample_no_result',
            field_required='tb_sputum_sample_no_result_other',
        )

        self.required_if(
            OTHER,
            field='tb_fever_duration',
            field_required='tb_fever_duration_other',
        )

        self.required_if(
            OTHER,
            field='last_cancer_test',
            field_required='last_cancer_test_other',
        )

        return self.cleaned_data
