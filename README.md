# Instagram Caption Generator

## Overview

This is a project to try and create a Instagram caption generator by training a neural network to associate phrases/captions with certain objects within the image provided. The general workflow is as shown below and is more indepth in the jupyter notebooks in the data_exploration folder.

Web Scraping: Using public APIs to scrap Instagram for training data. This will include the image, the number of followers of the user, the number of likes the image got, the caption and the number of comments

Image-Feature Conversion: Getting some sort of CNN to obtain features from an image in order to get roughly what the image contains (image classification)

Feature-Caption Conversion: Getting some sort of seq2seq model that will be able to convert features into a caption (will use BERT with captions).

## How To

To run the entire pipeline (preprocess and train) with the preprocessed data in ```data/preprocessed```:

```./run_expt.sh```

Note that you might have to do ```chmod +x ./run_expt.sh``` first.

The conversion from the raw data I have in this repo to the preprocessed data I use is in the jupyter notebooks in data_exploration and takes a lengthy amount of time. I highly recommend just emailing me for the preprocessed data.

## File Directory

data - A folder where all data lies (preprocessed and raw). Inside raw, you'll find my web scraped data. If you follow the preprocessing I do, you'll be able to obtain the other files. If you don't want to do this, feel free to email me at simonzeng9@gmail.com to obtain a copy of the dataset to be used directly for training!

data_exploration - A folder where I do initial data analysis for brainstorming regarding how to approach this problem (ie. looking at emojis, hashtags, etc). data_analysis.ipynb is where I do the analysis and cnn_dataset.ipynb is where I start to convert the data into a format where I can train a CNN.

precomputed_embedding_models - A folder where I keep the [word2vec model](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) that Google trained on about 100 million words from a Google News dataset

[This](https://github.com/szeng7/instagram_webscraping) is a repo of files that I'm using to scrape instagram for training data.

If you'd like a pickle file of the dataset I scraped and used, feel free to shoot me an email at simonzeng9@gmail.com!
