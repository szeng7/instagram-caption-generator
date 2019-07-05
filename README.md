# Instagram Caption Generator

This is a project to try and create a Instagram caption generator by training a neural network to associate phrases/captions with certain objects within the image provided. See Project Board for initial brainstorming, but the general workflow is as shown below:

Web Scraping: Using public APIs to scrap Instagram for training data. This will include the image (?), the number of followers of the user, the number of likes the image got, the caption and the number of comments

Conversion: Getting some sort of CNN-model to convert images to captions/descriptions in order to get words of what the image contains (image classification in a sense?)

Training: Training the main model on what a good caption would be based on the heuristic of percentage of likes and comments to followers (higher is better).
