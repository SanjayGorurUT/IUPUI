**Prediction task**: 30 day patient mortality in the ICU

Identify patient traits/demographics to help with this prediction. Subject_id is effectively patient id

**Proposed CSV files**:
* admissions.csv
  * subject_id
  * admission_type
  * ethnicity
  * diagnosis (on admission, could change)
* patients.csv
  * subject_id
  * gender
  * dob (age)
* icustays.csv
  * subject_id
  * icustay_id (maybe get a count? or see if it's multiple icu visits in same hospital stay (hadm_id))
  * length of stay

**To Consider**:
* labevents.csv (d_labitems.csv)
* chartevents.csv (most charted data goes here, just a lot)
* d_items.csv defines itemid in chartevents.csv 
* diagnoses_icd.csv (diagnoses for patients, with codes)
* d_icd_diagnoses (table for identifying these diagnoses)
* microbiologyevents.csv 
* datetimeevents.csv (all recorded observatoins, might be too much)
* inputevents_cv, inputevents_mv (one or the other, both have similar info on things like intubation/IVs)
* prescriptions.csv (not sure if there's a medication that can signify end of life/critical condition)

**Don't really need**:
* drgcodes.csv (diagnosis codes for billing purposes)
* outputevents.csv (things that are excreted by patient)
* transfers.csv (any patient bed movement within hospital)

**Don't need/not relevant**:
* callout.csv (time difference between discharge and acknowledgment)
* caregivers.csv (who is assigned to what patient)
* cptevents.csv (billing purpose regarding procedural terminology)
* d_cpt (dict for cptevents)
* services.csv (clinical service that patient registered with)
