from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER


class Section1FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='respondent_employment',
            field_required='respondent_employment_other',
        )

        return self.cleaned_data
