#sort the csv files by subject_id (defining feature of patient)

import pandas as pd

adm = pd.read_csv("ADMISSIONS.csv")
adm.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
adm.to_csv('./sorted/ADM_SORT.csv', index=False)

diag = pd.read_csv("DIAGNOSES_ICD.csv")
diag.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
diag.to_csv('./sorted/DIAG_SORT.csv', index=False)

icu = pd.read_csv("ICUSTAYS.csv")
icu.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
icu.to_csv('./sorted/ICU_SORT.csv', index=False)

pat = pd.read_csv("PATIENTS.csv")
pat.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
pat.to_csv('./sorted/PAT_SORT.csv', index=False)

pat = pd.read_csv('./sorted/PAT_SORT.csv')
#Divide the set into training 75% and testing 25%
pat_train = []
pat_test = []
count = 0
for x in range(len(pat)):
    element = {
        "ROW_ID": pat["ROW_ID"][x],
        "SUBJECT_ID": pat["SUBJECT_ID"][x],
        "GENDER": pat["GENDER"][x],
        "DOB": pat["DOB"][x],
        "DOD": pat["DOD"][x]
    }


    if count % 4 == 0:
        pat_test.append(element)
    else:
        pat_train.append(element)
    #pat_train.append(element)

    count = count + 1

df = pd.DataFrame(pat_train)
#df.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
df.to_csv('./sorted/PAT_TRAIN_SORT.csv', index=False)

df = pd.DataFrame(pat_test)
#df.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
df.to_csv('./sorted/PAT_TEST_SORT.csv', index=False)


#pres = pd.read_csv("PRESCRIPTIONS.csv")
#print(pres)
#pres.sort_values(["SUBJECT_ID"], axis=0, ascending=[True], inplace=True)
#print(pres)
#pres.to_csv('./sorted/PRES_SORT.csv', index=False)

