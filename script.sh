#!/bin/bash

mkdir csv
mkdir sorted

echo "Starting sorting.py..."
python sorting.py

echo "Starting feature_creation.py..."
python feature_creation.py

echo "Making copies of feature and id csvs..."
cp ./csv/features.csv ./csv/features.csv.bkp
cp ./csv/id.csv ./csv/id.csv.bkp

echo "Starting edge_creation.py..."
python edge_creation.py

echo "Starting label_creation.py..."
python label_creation.py

echo "Build successful! CSV files located in ./csv"
