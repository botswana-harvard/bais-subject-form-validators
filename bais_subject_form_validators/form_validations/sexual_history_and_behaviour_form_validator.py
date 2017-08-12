from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES, OTHER, NO, DONT_KNOW

from ..constants import CONCURRENT


class SexualHistoryAndBehaviourFormValidator(FormValidator):

    def clean(self):

        req_fields = [
            'sexual_intercourse_age',
            'sexual_intercouse_consent',
            'sexual_intercourse_influence',
            'sexual_intercouse_protection',
            'sexual_intercouse_protection_reason',
            'sex_recently',
        ]
        for req_field in req_fields:
            self.required_if(
                YES,
                field='sexual_intercouse',
                field_required=req_field,
            )

        self.required_if(
            OTHER,
            field='sexual_intercourse_influence',
            field_required='sexual_intercourse_influence_other',
        )

        self.required_if(
            YES,
            field='sexual_intercouse_protection',
            field_required='sexual_intercouse_protection_use',
        )

        self.not_required_if(
            NO,
            field='sexual_intercouse_protection',
            field_required='sexual_intercouse_protection_use',
        )

        self.not_required_if(
            DONT_KNOW,
            field='sexual_intercouse_protection',
            field_required='sexual_intercouse_protection_use',
        )

        self.required_if(
            OTHER,
            field='sexual_intercouse_protection_use',
            field_required='sexual_intercouse_protection_use_other',
        )

        self.required_if(
            OTHER,
            field='sexual_intercouse_protection_reason',
            field_required='sexual_intercouse_protection_reason_other',
        )

        req_fields_recently = [
            'sex_consentual',
            'sex_with_whom',
        ]
        for rec_field in req_fields_recently:
            self.required_if(
                YES,
                field='sex_recently',
                field_required=rec_field,
            )

        self.required_if(
            OTHER,
            field='sex_with_whom',
            field_required='sex_with_whom_other',
        )

        self.required_if(
            OTHER,
            field='assistance',
            field_required='assistance_other',
        )

        self.not_required_if(
            NO,
            field='physical_sexual_violance_male',
            field_required='physical_sexual_violance_who',
        )

        self.not_required_if(
            NO,
            field='physical_sexual_violance_female',
            field_required='physical_sexual_violance_who',
        )

        self.required_if(
            CONCURRENT,
            field='partners_serial_concurrent',
            field_required='partners_serial_concurrent_explain',
        )

        not_req_fields = [
            'condom_main_reason_partner1',
            'condom_main_reason_partner2',
            'condom_main_reason_partner3',
            'condom_not_used_reason_partner1',
            'condom_not_used_reason_partner2',
            'condom_not_used_reason_partner3',
            'condom_place_partner1',
            'condom_place_partner2',
            'condom_place_partner3',
            'drunk_high_sex_partner1',
            'drunk_high_sex_partner2',
            'drunk_high_sex_partner3',
            'partner_other_partners_partner1',
            'partner_other_partners_partner2',
            'partner_other_partners_partner3',
            'sexual_partner_recent1',
            'sexual_partner_recent2',
            'sexual_partner_recent3',
            'paid_for_sex'
        ]
        for not_req_field in not_req_fields:
            self.not_required_if(
                NO,
                field='sexual_intercouse',
                field_required=not_req_field,
            )

        return self.cleaned_data
