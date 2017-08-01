from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class Section1FormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='respondent_employment',
            field_required='respondent_employment_other',
        )

        self.required_if(
            YES,
            field='mine',
            field_required='mine_period'
        )

        self.required_if(
            OTHER,
            field='mine_occupation',
            field_required='mine_occupation_other',
        )

        self.required_if(
            YES,
            field='mine',
            field_required='commodity'
        )

        self.required_if(
            OTHER,
            field='commodity',
            field_required='commodity_other',
        )

        self.required_if(
            OTHER,
            field='religion',
            field_required='religion_other',
        )

        self.not_required_if(
            NEVER,
            field='marital_status',
            field_required='respondent_marriage_age',
        )

        self.required_if(
            NO,
            field='living_with_spouse',
            field_required='spouse_visit',
        )

        self.not_required_if(
            NEVER,
            field='marital_status',
            field_required='respondent_married_years',
        )

        return self.cleaned_data
