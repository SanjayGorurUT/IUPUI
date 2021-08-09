import numpy as np
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

#fv_matrix[patient num][feature index]
fv_matrix = [[0 for x in range(4)] for y in range(len(patients_df))]
#print(fv_matrix[4][3])

#id_list (holds all patient ids that are valid)
id_list = [];

cat1 = 0;
cat2 = 0;
cat3 = 0;
cat4 = 0;
cat5 = 0;
cat6 = 0;

index = 0
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
        admit_type = admission_df["ADMISSION_TYPE"][y].lower()

        if "newborn" in admit_type:
            admit_type = 0
        elif "emergency" in admit_type:
            admit_type = 1
        elif "elective" in admit_type:
            admit_type = 2
        elif "urgent" in admit_type:
            admit_type = 3
        else:
            admit_type = 4
        
        #print(adm_type_list.index(admit_type))
        

        #ethnicity
        #print("ETHNICITY")
        eth = admission_df["ETHNICITY"][y].lower()
        #print(eth)

        if "white" in eth or "portuguese" in eth:
            eth = 1
            cat1 = cat1 + 1
        elif "black" in eth:
            eth = 2
            cat2 = cat2 + 1
        elif "asian" in eth or "native hawaiian" in eth or "middle" in eth:
            eth = 3
            cat3 = cat3 + 1
        elif "hispanic" in eth or "south american" in eth or "caribbean" in eth:
            eth = 4
            cat4 = cat4 + 1
        elif "american indian" in eth:
            eth = 5
            cat5 = cat5 + 1
        else:
            eth = 6
            cat6 = cat6 + 1
        
        #print(eth)

        #take a look at this 


        #print(eth_list.index(eth))

        #gender
        gender = patients_df["GENDER"][x].lower()
        #print(gender)
        if "f" in gender:
            gender = 0
        elif "m" in gender:           
            gender = 1
        else: 
            gender = 2
        #if gender not in gender_list:
        #    gender_list.append(gender)
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

        #print(admission_df["SUBJECT_ID"][y])
        #print(patients_df["SUBJECT_ID"][x])
        #print(age)


        
        x = x + 1

        #skip patient if older than 120 years of age
        if age > 120: 
            print("Too old")
            print(admission_df["SUBJECT_ID"][y])
            continue


        #construct the feature vector element
        #element = {
        #    "id": curr,
        #    "admit_type": adm_type_list.index(admit_type),
        #    "ethnicity": eth,
        #    "gender": gender_list.index(gender),
        #    "age": age
        #}

        fv_matrix[index][0] = admit_type
        fv_matrix[index][1] = eth 
        fv_matrix[index][2] = gender
        fv_matrix[index][3] = age 
        
        index = index + 1

        #print(element)
        #fv_matrix.append(element)

        id_list.append(admission_df["SUBJECT_ID"][y])

    y = y + 1

#print(cat1)
#print(cat2)
#print(cat3)
#print(cat4)
#print(cat5)
#print(cat6)

#fv_matrix cutting off the 0 entries
short_fv_matrix = [[0 for x in range(4)] for y in range(len(id_list))]

for x in range(0, len(id_list)):
    short_fv_matrix[x] = fv_matrix[x]

print(index)
print(len(id_list))
print("FV");

print(short_fv_matrix[44528])
print(fv_matrix[44528])
print(fv_matrix[44529])

fv_matrix = short_fv_matrix

#convert into np array
fv_matrix = np.array(fv_matrix)

#normalize it
fv_matrix_norm_col = np.linalg.norm(fv_matrix, axis=0)
fv_matrix_norm = fv_matrix/fv_matrix_norm_col

#create the format for features.csv
fv_dict = []
for x in range(len(fv_matrix)):
    for y in range(len(fv_matrix[0])):
        element = {
            "node_id": id_list[x],
            "feature_id": y,
            "value": fv_matrix_norm[x][y]
        }
        fv_dict.append(element)

#print(fv_dict[4])
#print(fv_dict[5])
#print(fv_dict[6])
#print(fv_dict[7])

id_dict = []
for x in range(len(id_list)):
    element = {
        "id": id_list[x]
    }
    id_dict.append(element)

#convert to csv files
df = pd.DataFrame(fv_dict)
df.to_csv('features.csv', index = False)

df = pd.DataFrame(id_dict)
df.to_csv('id.csv', index = False)
#print(fv_matrix[1])
#print(fv_matrix_norm_col)
#print(fv_matrix_norm[1])

#x = np.linalg.norm(fv_matrix_norm)
#print(x)


#TEST

#a = np.array([5, 2, 0, 1, 9])

#data = np.array([[150, 60, 23, 5000],
#                [165, 65, 29, 2300],
#                [155, 85, 35, 7500],
#                [135, 72, 54, 1800],
#                [170, 91, 24, 1500]])

#print(fv_matrix)

#print(short_fv_matrix)
#print("PRESCRIPTIONS")
#prescriptions_df = pd.read_csv('PRESCRIPTIONS.csv', usecols = ['SUBJECT_ID', 'DRUG_NAME_GENERIC'])
#print(prescriptions_df)


