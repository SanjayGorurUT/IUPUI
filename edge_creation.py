import pandas as pd
import math

#print("ADMISSIONS")
#admission_df = pd.read_csv('ADMISSIONS.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'ADMISSION_TYPE', 'ETHNICITY', 'DIAGNOSIS'])
#print(admission_df)

print("DIAGNOSES")
#diagnoses_df = pd.read_csv('DIAGNOSES_ICD.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'SEQ_NUM', 'ICD9_CODE'])
diagnoses_df = pd.read_csv('DIAGNOSES_ICD.csv', usecols = ['SUBJECT_ID', 'SEQ_NUM', 'ICD9_CODE'])
print(diagnoses_df)
print(diagnoses_df["SUBJECT_ID"][0])

print("IDS")
ids_df = pd.read_csv('id.csv')
print(ids_df)

print("TEST")
print(ids_df["id"][0])

#reconstruct id_list
id_list = []

for x in range(len(ids_df)):
    id_list.append(ids_df["id"][x])

print(id_list)

print("OVER")

id_set = set();

pat_array = []

for x in range(0, 651047 + 1):
#for x in range(0, 1000):

    #is it a subject id we are interested in?
    if diagnoses_df["SUBJECT_ID"][x] not in id_list:
        print("NOT IN")
        print(diagnoses_df["SUBJECT_ID"][x])
        continue
    #have we seen this before?
    if diagnoses_df["SUBJECT_ID"][x] not in id_set:
        id_set.add(diagnoses_df["SUBJECT_ID"][x])
        code = diagnoses_df["ICD9_CODE"][x]

        if "V" not in str(code) and "E" not in str(code):

            #check to see if it's nan or not (sometimes patients get no diagnosis in diagnoses.csv?)
            if math.isnan(float(code)) is True:
                continue

            diag = {
                "id": diagnoses_df["SUBJECT_ID"][x],
                "diagnosis_code": int(code)
            }
            pat_array.append(diag)

#print(pat_array)

#sort by subject id, ascending
pat_array = sorted(pat_array, key = lambda i: i['id'])
#print(pat_array)
#print(len(pat_array))

for x in range(len(pat_array)):
    print(pat_array[x]["id"])

dimensions = len(pat_array) #create the sparse matrix

similarity_matrix = [[0 for a in range(dimensions)] for b in range(dimensions)]

print(pat_array[0]["diagnosis_code"])

for x in range(dimensions):
    for y in range(x + 1, dimensions):
        if x == y: 
            continue
        #if diagnoses_df["ICD9_CODE"][x] == diagnoses_df["ICD9_CODE"][y]:
        if pat_array[x]["diagnosis_code"] % 1000 == pat_array[y]["diagnosis_code"] % 1000:
            print(x)
            print(y)
            similarity_matrix[x][y] = 1
        else:
            similarity_matrix[x][y] = 0

for x in range(len(similarity_matrix[0])):
    print(similarity_matrix[x])

#construct edge csv file
threshold = 0.5

edge_dict = []
for x in range(dimensions):
    for y in range(x + 1, dimensions):
        if x == y:
            continue
        if similarity_matrix[x][y] > threshold:
            entry = {
                "id1": x,
                "id2": y
            }
            edge_dict.append(entry)

df = pd.DataFrame(edge_dict)
df.to_csv('edges.csv', index = False)
#print(similarity_matrix)

#print("ICU STAYS")
#icu_df = pd.read_csv('ICUSTAYS.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'ICUSTAY_ID', 'LOS'])
#print(icu_df)

#print("PATIENTS")
#patients_df = pd.read_csv('PATIENTS.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'GENDER', 'DOB'])
#print(patients_df)

#print("PRESCRIPTIONS")
#prescriptions_df = pd.read_csv('PRESCRIPTIONS.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'DRUG_NAME_GENERIC'])
#print(prescriptions_df)
