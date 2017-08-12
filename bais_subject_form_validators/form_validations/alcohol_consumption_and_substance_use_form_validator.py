from edc_base.modelform_validators import FormValidator
from edc_constants.constants import YES


class AlcoholConsumptionAndSubstanceUseFormValidator(FormValidator):

    def clean(self):
        alc_fields = ['substance_method_alcohol',
                      'substance_age_alcohol',
                      'substance_frequency_alcohol']
        for alc_field in alc_fields:
            self.required_if(
                YES,
                field='taken_alcohol',
                field_required=alc_field,
            )

        tob_fields = ['substance_method_tobacco',
                      'substance_age_tobacco',
                      'substance_frequency_tobacco']
        for tob_field in tob_fields:
            self.required_if(
                YES,
                field='taken_tobacco',
                field_required=tob_field,
            )

        maj_fields = ['substance_method_marijuana',
                      'substance_age_marijuana',
                      'substance_frequency_marijuana']
        for maj_field in maj_fields:
            self.required_if(
                YES,
                field='taken_marijuana',
                field_required=maj_field,
            )

        coc_fields = ['substance_method_cocaine',
                      'substance_age_cocaine',
                      'substance_frequency_cocaine']
        for coc_field in coc_fields:
            self.required_if(
                YES,
                field='taken_cocaine',
                field_required=coc_field,
            )

        cra_fields = ['substance_method_crack',
                      'substance_age_crack',
                      'substance_frequency_crack']
        for cra_field in cra_fields:
            self.required_if(
                YES,
                field='taken_crack',
                field_required=cra_field,
            )

        met_fields = ['substance_method_meth',
                      'substance_age_meth',
                      'substance_frequency_meth']
        for met_field in met_fields:
            self.required_if(
                YES,
                field='taken_meth',
                field_required=met_field,
            )

        nya_fields = ['substance_method_nyaope',
                      'substance_age_nyaope',
                      'substance_frequency_nyaope']
        for nya_field in nya_fields:
            self.required_if(
                YES,
                field='taken_nyaope',
                field_required=nya_field,
            )

        her_fields = ['substance_method_heroine',
                      'substance_age_heroine',
                      'substance_frequency_heroine']
        for her_field in her_fields:
            self.required_if(
                YES,
                field='taken_heroine',
                field_required=her_field,
            )

        ecs_fields = ['substance_method_ecstasy',
                      'substance_age_ecstasy',
                      'substance_frequency_ecstasy']
        for ecs_field in ecs_fields:
            self.required_if(
                YES,
                field='taken_ecstasy',
                field_required=ecs_field,
            )

        cod_fields = ['substance_method_codeine',
                      'substance_age_codeine',
                      'substance_frequency_codeine']
        for cod_field in cod_fields:
            self.required_if(
                YES,
                field='taken_codeine',
                field_required=cod_field,
            )

        return self.cleaned_data
