# Instagram Caption Generator

This is a project to try and create a Instagram caption generator by training a neural network to associate phrases/captions with certain objects within the image provided. Below is initial brainstorming:


- [ ] Need instagram/image based dataset.
    - [ ] https://github.com/gvsi/instagram-like-predictor
    - [ ] https://towardsdatascience.com/predict-the-number-of-likes-on-instagram-a7ec5c020203
    - [ ] https://github.com/cesc-park/attend2u
    - [ ] Consider webscrapping?
        - [ ] https://github.com/h4t0n/instagram-scraper
- [ ] Need input features
    - [ ] way of converting image into a caption/description
    - [ ] hashtags
- [ ] Need way of judging output features
    - [ ] Number of likes
    - [ ] Number of followers
    - [ ] Percentage of likes to followers?
- [ ] Model architecture
    - [ ] CNN to decode an image into a description