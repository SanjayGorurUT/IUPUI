#sort the csv files by subject_id (defining feature of patient)

import pandas as pd

adm = pd.read_csv("ADMISSIONS.csv")

print(adm)

adm.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)

print(adm)

adm.to_csv('./sorted/ADM_SORT.csv', index=False)

diag = pd.read_csv("DIAGNOSES_ICD.csv")
print(diag)
diag.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
print(diag)
diag.to_csv('./sorted/DIAG_SORT.csv', index=False)

icu = pd.read_csv("ICUSTAYS.csv")
print(icu)
icu.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
print(icu)
icu.to_csv('./sorted/ICU_SORT.csv', index=False)

pat = pd.read_csv("PATIENTS.csv")
print(pat)
pat.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
print(pat)
pat.to_csv('./sorted/PAT_SORT.csv', index=False)

pres = pd.read_csv("PRESCRIPTIONS.csv")
print(pres)
pres.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
print(pres)
pres.to_csv('./sorted/PRES_SORT.csv', index=False)

