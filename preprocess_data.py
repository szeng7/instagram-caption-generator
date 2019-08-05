from keras.preprocessing.image import img_to_array
import argparse as ap
import pickle
import urllib
import cv2
import numpy as np
from tqdm import tqdm

# pylint: disable=no-member

def preprocess_data(data, label_map):
    x = []
    y = []
    for example_index in tqdm(range(len(data))):
        url = data[example_index][0]
        curr_y = data[example_index][1]
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        try:
            image = cv2.resize(image, (64, 64))
            image = img_to_array(image)
            x.append(image)
            y.append(label_map[curr_y])
        except: #toss out images where we can't resize
            pass

    assert len(x) != 0 and len(y) != 0

    return np.asarray(x), np.asarray(y)

def main():
    p = ap.ArgumentParser()

    p.add_argument('--label-map', required=True, \
        help='pickle file of label map')
    p.add_argument('--input-data-pickle', required=True, \
        help='pickle file of data')
    p.add_argument('--output-data-pickle', required=True, \
        help='pickle file to output preprocessed data')
    ARGS = p.parse_args()

    with open(ARGS.label_map, "rb") as f:
        label_map = pickle.load(f)

    with open(ARGS.input_data_pickle, "rb") as f:
        data = pickle.load(f)

    x_data, y_data = preprocess_data(data, label_map)

    with open(ARGS.output_data_pickle, "wb") as f:
        pickle.dump((x_data, y_data), f)

if __name__ == "__main__":
    main()