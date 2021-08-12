**Prediction task**: Patient Mortality

**Details below in constructing and testing the graph**

Contact Jonathan Wu at jswu72@gatech.edu for any questions about errors in regards to the script.

**To-Do**
- [X] Identify patient traits/demographics to help with this prediction. Subject_id is effectively patient id
- [ ] Pull information out of csv files
   - [X] Read up on extracting information per row header
   - [X] Extract per subject_id, construct into vector
   - [ ] Read Rocheteau et al, 2021 for how they calculated a similarity score for difficult things like diagnosis similarity
   - [X] Normalize vector (Rocheteau et al, 2021 went -1 and 1 for 5th and 95th percentile. Extremes -4, 4)
- [ ] Construct graph
   - [ ] Cosine similarity on all pairs of vectors (currently on a diagnosis check)
   - [X] Build an edge (x,y) for similarity scores over threshold 
- [X] Setup labels for dataset (mortality, 0/1)
   - [X] Keep a portion hidden for testing purposes
- [X] Run through a graph neural network (cluster-GCN)
   - [X] Predict on patient mortality (0/1, no/yes)

**Directions to construct and test the graph, using the script**

1) Get access to the MIMIC-III repository, found here: https://physionet.org/content/mimiciii/1.4/.
2) Extract ADMISSIONS.csv, DIAGNOSES_ICD.csv, PATIENTS.csv and place them in the home directory of this repository.
3) Run the bash script script.sh to construct the graph.
4) Take the csv files placed in ./csv and move them to the input directory of Rozemberczki's implementation of Cluster-GCN: https://github.com/benedekrozemberczki/ClusterGCN

**Directions to construct and test the graph, without the script**

1) Follow steps 1 and 2 above in the previous section
2) Create the csv and sorted directories in the home repository
3) Run the sorting.py script
4) Run the feature_creation.py script
5) Run the edge_creation.py script
6) Run the label_creation.py script
7) Export the csv files similar to in step 4 of the previous section
