from edc_base.modelform_validators import FormValidator
from edc_constants.constants import OTHER, YES, NEVER, NO


class BackgroundCharacteristicsFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            OTHER,
            field='respondent_employment',
            field_required='respondent_employment_other',
        )

        req_fields = ['mine_period',
                      'commodity']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='mine',
                field_required=req_field
            )

        self.required_if(
            OTHER,
            field='mine_occupation',
            field_required='mine_occupation_other',
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

        model_fields = ['respondent_marriage_age',
                        'respondent_married_years']
        for fields in model_fields:
            self.not_required_if(
                NEVER,
                field='marital_status',
                field_required=fields,
            )

        self.required_if(
            NO,
            field='living_with_spouse',
            field_required='spouse_visit',
        )

        return self.cleaned_data
