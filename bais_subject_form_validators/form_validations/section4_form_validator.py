from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER, NO


class Section4FormValidator(FormValidator):

    def clean(self):
        req_fields = [
            'circumcission_year',
            'circumcission_reason',
            'circumcission_place',
            'circumcised_complications']
        for req_field in req_fields:
            self.required_if(
                YES,
                field='circumcission',
                field_required=req_field,
            )

        self.required_if(
            NO,
            field='circumcission',
            field_required='circumcission_intent',
        )

        self.required_if(
            YES,
            field='circumcission_intent',
            field_required='circumcission_intent_reason',
        )

        self.required_if(
            OTHER,
            field='circumcission_intent',
            field_required='circumcission_intent_reason_other',
        )

        self.required_if(
            NO,
            field='circumcission_intent',
            field_required='circumcission_reject_reason',
        )

        self.required_if(
            OTHER,
            field='circumcission_reject_reason',
            field_required='circumcission_reject_reason_other',
        )

        self.required_if(
            OTHER,
            field='sti_symptoms',
            field_required='sti_symptoms_other',
        )

        return self.cleaned_data
