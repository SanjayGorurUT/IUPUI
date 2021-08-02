Some patient graph analysis that's being done last minute like all expertly-crafted things

Prediction task: 30 day patient mortality in the ICU

Identify patient traits/demographics to help with this prediction

Proposed CSV files:
admissions.csv
patients.csv
icustays.csv

To Consider:
labevents.csv (d_labitems.csv)
chartevents.csv (most charted data goes here, just a lot)
d_items.csv defines itemid in chartevents.csv 
diagnoses_icd.csv (diagnoses for patients, with codes)
d_icd_diagnoses (table for identifying these diagnoses)
microbiologyevents.csv 
datetimeevents.csv (all recorded observatoins, might be too much)
inputevents_cv, inputevents_mv (one or the other, both have similar info on things like intubation/IVs)
prescriptions.csv (not sure if there's a medication that can signify end of life/critical condition)

Don't really need:
drgcodes.csv (diagnosis codes for billing purposes)
outputevents.csv (things that are excreted by patient)
transfers.csv (any patient bed movement within hospital)

Don't need/not relevant:
callout.csv (time difference between discharge and acknowledgment)
caregivers.csv (who is assigned to what patient)
cptevents.csv (billing purpose regarding procedural terminology)
d_cpt (dict for cptevents)
services.csv (clinical service that patient registered with)
