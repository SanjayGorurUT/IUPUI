import pandas as pd
from datetime import datetime

#feature list
#1: admission_type
#2: ethnicity
#3: icuLOS
#4: numICUStays
#5: gender

#possible
#X: drugNameGeneric
#X: age
#X: admissionDiagnosis

print("ADMISSIONS SORTED")
admission_df = pd.read_csv('./sorted/ADM_SORT.csv', usecols = ['SUBJECT_ID', 'ADMITTIME', 'ADMISSION_TYPE', 'ETHNICITY', 'DIAGNOSIS'])
print(admission_df)


#print(admission_df['SUBJECT_ID'][0])


#print("ICU STAYS")
#icu_df = pd.read_csv('ICUSTAYS.csv', usecols = ['SUBJECT_ID', 'ICUSTAY_ID', 'LOS'])
#print(icu_df)

print("PATIENTS SORTED")
patients_df = pd.read_csv('./sorted/PAT_SORT.csv', usecols = ['SUBJECT_ID', 'GENDER', 'DOB'])
print(patients_df)

#with this loop there are more admissions than patients
#if we get a duplicate admission, skip it and keep marker in same spot for patients
curr = 0
y = 0
x = 0

adm_type_list = [];
eth_list = [];
gender_list = [];
fv_matrix = [];
#for x in range(len(patients_df)):
while x < len(patients_df):
    #print("NEW")
    #print("ADMISSION")
    #print(admission_df["SUBJECT_ID"][y])
    #print("PATIENTS")
    #print(patients_df["SUBJECT_ID"][x])

    if curr < admission_df["SUBJECT_ID"][y]:
        #print("ADMISSION")
        #print(admission_df["SUBJECT_ID"][y])
        #print("PATIENTS")
        #print(patients_df["SUBJECT_ID"][x])
       
        curr = int(admission_df["SUBJECT_ID"][y])

        #admit type

        #print("ADMISSION TYPE")
        admit_type = admission_df["ADMISSION_TYPE"][y] 
        if admit_type not in adm_type_list:
            adm_type_list.append(admit_type)
        #print(admit_type)
        #print(adm_type_list.index(admit_type))

        #ethnicity
        #print("ETHNICITY")
        eth = admission_df["ETHNICITY"][y] 
        if eth not in eth_list:
            eth_list.append(eth)
        
        #print(eth)

        #take a look at this 
        #print(eth_list)

        #print(eth_list.index(eth))

        #gender
        gender = patients_df["GENDER"][x]
        if gender not in gender_list:
            gender_list.append(gender)
        #print(gender)

        admittime = admission_df["ADMITTIME"][y]
        dob = patients_df["DOB"][x]

        #strip the hour, minute, second, just worried about the year, month, day
        admittime = admittime.split(" ")[0]
        dob = dob.split(" ")[0]

        #convert to datetime objects
        admittime = datetime.strptime(admittime, "%Y-%m-%d")
        dob = datetime.strptime(dob, "%Y-%m-%d")
        #print(admittime)
        #print(dob)
        
        age = ((admittime - dob).days) / 365
        age = int(round(age, 0))
        #print(age)

        #if age < 0:
            #print(admission_df["SUBJECT_ID"][x])
            #print(patients_df["SUBJECT_ID"][x])
        x = x + 1

        #construct the feature vector element
        element = {
            "id": curr,
            "admit_type": adm_type_list.index(admit_type),
            "ethnicity": eth_list.index(eth),
            "gender": gender_list.index(gender),
            "age": age
        }

        #print(element)
        fv_matrix.append(element)

    y = y + 1

print("FV");
print(fv_matrix)
#print("PRESCRIPTIONS")
#prescriptions_df = pd.read_csv('PRESCRIPTIONS.csv', usecols = ['SUBJECT_ID', 'DRUG_NAME_GENERIC'])
#print(prescriptions_df)


