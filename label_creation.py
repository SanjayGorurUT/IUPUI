import pandas as pd
import math

ids_df = pd.read_csv('./csv/id.csv')

#reconstruct ids list
id_list = []
for x in range(len(ids_df)):
    id_list.append(ids_df["id"][x])

#print(id_list)

pat_df = pd.read_csv('./sorted/PAT_TRAIN_SORT.csv')

node_id = 0 #ClusterGCN implementation starts from 0, index accordingly (no longer patient IDs)
target_list = []
for x in range(len(pat_df)):
    if pat_df["SUBJECT_ID"][x] not in id_list:
        continue
    
    dod_exists = 0;
    if "-" in str(pat_df["DOD"][x]):
        dod_exists = 1; 
    element = {
        #"node_id": pat_df["SUBJECT_ID"][x],
        "node_id": node_id,
        "target": dod_exists
    }
    target_list.append(element)
    
    node_id = node_id + 1

df = pd.DataFrame(target_list)
df.to_csv("./csv/target.csv", index=False)
        
