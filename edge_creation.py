#run this script once, concurrent runs will destory the target csv files (id.csv, features.csv)

import pandas as pd
import math

#print("ADMISSIONS")
#admission_df = pd.read_csv('ADMISSIONS.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'ADMISSION_TYPE', 'ETHNICITY', 'DIAGNOSIS'])
#print(admission_df)

#print("DIAGNOSES")
#diagnoses_df = pd.read_csv('DIAGNOSES_ICD.csv', index_col='SUBJECT_ID', usecols = ['SUBJECT_ID', 'SEQ_NUM', 'ICD9_CODE'])
diagnoses_df = pd.read_csv('DIAGNOSES_ICD.csv', usecols = ['SUBJECT_ID', 'SEQ_NUM', 'ICD9_CODE'])
#print(diagnoses_df)
#print(diagnoses_df["SUBJECT_ID"][0])

#print("IDS")
ids_df = pd.read_csv('./csv/id.csv')
#print(ids_df)

feature_df = pd.read_csv('./csv/features.csv')

#print("TEST")
#print(ids_df["id"][0])

#reconstruct id_list
id_list = []

for x in range(len(ids_df)):
    id_list.append(ids_df["id"][x])

#print(id_list)

#print("OVER")

id_set = set();

node_id = 0
pat_array = []
#this is roughly 400k
#for x in range(len(diagnoses_df)):
#100k works
for x in range(0, 250000):
    if x % 10000 == 0:
        print(x)

    #is it a subject id we are interested in?
    if diagnoses_df["SUBJECT_ID"][x] not in id_list:
        #print("NOT IN")
        #print(diagnoses_df["SUBJECT_ID"][x])
        continue
    #have we seen this before?
    if diagnoses_df["SUBJECT_ID"][x] not in id_set:
        id_set.add(diagnoses_df["SUBJECT_ID"][x])
        code = diagnoses_df["ICD9_CODE"][x]

        if "V" not in str(code) and "E" not in str(code):

            #check to see if it's nan or not (sometimes patients get no diagnosis in diagnoses.csv?)
            if math.isnan(float(code)) is True:
                continue

            #print(diagnoses_df["SUBJECT_ID"][x])
            element = {
                "id": diagnoses_df["SUBJECT_ID"][x],
                #"id": node_id,
                "diagnosis_code": int(code)
            }
            pat_array.append(element)

            node_id = node_id + 1

#print(pat_array)

#sort by subject id, ascending
pat_array = sorted(pat_array, key = lambda i: i['id'])
#print("PAT ARRAY")
#print(pat_array)
#print(len(pat_array))

#for x in range(len(pat_array)):
#    print(pat_array[x]["id"])

dimensions = len(pat_array) #create the sparse matrix

similarity_matrix = [[0 for a in range(dimensions)] for b in range(dimensions)]

#print(pat_array[0]["diagnosis_code"])

#get ids of all elements in pat_array, these are the new id_list
temp_list = []

for x in range(dimensions):
    for y in range(x + 1, dimensions):
        if x == y: 
            continue
        #if diagnoses_df["ICD9_CODE"][x] == diagnoses_df["ICD9_CODE"][y]:
        if pat_array[x]["diagnosis_code"] % 1000 == pat_array[y]["diagnosis_code"] % 1000:
            #print("MATCH")
            #print(x)
            #print(y)
            similarity_matrix[x][y] = 1

            if pat_array[x]["id"] not in temp_list:
                temp_list.append(pat_array[x]["id"])

            if pat_array[y]["id"] not in temp_list:
                temp_list.append(pat_array[y]["id"])
        else:
            similarity_matrix[x][y] = 0

#for x in range(len(similarity_matrix[0])):
#    print(similarity_matrix[x])


temp_list.sort()
#print("sorted")
#print(temp_list)

#construct edge csv file
threshold = 0.5

edge_dict = []
for x in range(dimensions):
    for y in range(x + 1, dimensions):
        if x == y:
            continue
        if similarity_matrix[x][y] > threshold:

            entry = {
                "id1": temp_list.index(pat_array[x]["id"]),
                "id2": temp_list.index(pat_array[y]["id"])
            }
            edge_dict.append(entry)

            #add the reverse pair
            entry2 = {
                "id1": temp_list.index(pat_array[y]["id"]),
                "id2": temp_list.index(pat_array[x]["id"])
            }
            edge_dict.append(entry2)

#sort the edge_dict by id1 elements
edge_dict = sorted(edge_dict, key = lambda i: i["id1"])

df = pd.DataFrame(edge_dict)
df.to_csv('./csv/edges.csv', index = False)

#reconstruct id.csv
id_list = temp_list

id_dict = []
for x in range(len(id_list)):
    element = {
        "id": id_list[x]
    }
    id_dict.append(element)

df = pd.DataFrame(id_dict)
df.to_csv('./csv/id.csv', index = False)

#reconstruct feature vector matrix
fv_dict = []
index = -1
curr = 0
for x in range(len(feature_df)):
    if feature_df["node_id"][x] not in id_list:
        continue
    
    if curr != feature_df["node_id"][x]:
        curr = feature_df["node_id"][x]
        index = index + 1
        #print("CURR")
        #print(curr)
    if feature_df["value"][x] == 0:
        continue

    element = {
        "node_id": index,
        "feature_id": feature_df["feature_id"][x],
        "value": feature_df["value"][x]
    }

    fv_dict.append(element)
df = pd.DataFrame(fv_dict)
df.to_csv('./csv/features.csv', index = False)

#print(len(fv_dict))
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
