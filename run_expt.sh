#! /usr/bin/env bash

echo "Downloading requirements"
pip install -r requirements.txt

DATA_DIR=data/preprocessed

if [ -f "${DATA_DIR}/preprocessed_traina_64x64.pickle" ] && \
[ -f "${DATA_DIR}/preprocessed_trainb_64x64.pickle" ] && \
[ -f "${DATA_DIR}/preprocessed_dev_64x64.pickle" ] && \
[ -f "${DATA_DIR}/preprocessed_test_64x64.pickle" ]; then

    echo "Using existing preprocessed files"

else

    echo "Preprocessing data using raw pickle files..."

    echo "Train A"
    python preprocess_data.py --label-map ${DATA_DIR}/label_map.pickle --input-data-pickle ${DATA_DIR}/traina.pickle \
    --output-data-pickle ${DATA_DIR}/preprocessed_traina_64x64.pickle

    echo "Train B"
    python preprocess_data.py --label-map ${DATA_DIR}/label_map.pickle --input-data-pickle ${DATA_DIR}/trainb.pickle \
    --output-data-pickle ${DATA_DIR}/preprocessed_trainb_64x64.pickle

    echo "Dev"
    python preprocess_data.py --label-map ${DATA_DIR}/label_map.pickle --input-data-pickle ${DATA_DIR}/dev.pickle \
    --output-data-pickle ${DATA_DIR}/preprocessed_dev_64x64.pickle

    echo "Test"
    python preprocess_data.py --label-map ${DATA_DIR}/label_map.pickle --input-data-pickle ${DATA_DIR}/test.pickle \
    --output-data-pickle ${DATA_DIR}/preprocessed_test_64x64.pickle
fi

echo "Training..."
python feature_trainer.py --train-pickle ${DATA_DIR}/preprocessed_traina_64x64.pickle --dev-pickle ${DATA_DIR}/preprocessed_dev_64x64.pickle --test-pickle ${DATA_DIR}/preprocessed_test_64x64.pickle


