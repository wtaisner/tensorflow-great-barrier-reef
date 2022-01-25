# ~~tensorflow~~ torch-great-barrier-reef

#### Kaggle competition:
https://www.kaggle.com/c/tensorflow-great-barrier-reef

#### Requirements:
https://docs.google.com/document/d/1ncurueGQyY-JGWw1YunEkOgoUZtA5ivJUcvZ8HuyDy4/edit

#### Docker documentation: ####
Prerequisites: 

Docker container is used for interference only. It is required to contain a subdirectory with trained models and data to test. In our case, the structure is as follows:

NOTE: for the sake of simplicity, as of now `predictor.py` is hard-coded to preform inference on one test_image and specified model
```
tensorflow-great-barrier-reef
│   README.md
│   .ipynb files    
│   Dockerfile
│
└───inference
│   │   predictor.py
│   │   ...
│   │
│   └───model
│   │   │   model1.pt
│   │   │   model2.pt
│   │   │   ...
│   │
│   └───test_data
│       │   test_image.jpg
│       │   ...
│
└───data
    │   train_images/
    │   ...
```
If it is your first time running docker, start with this command:
`docker build -t NAME .`
where NAME is desired name of the docker container

If you want to start the container, run:

`docker run -it -v PATH:/app/ NAME`

where PATH is full path to directory with `predictor.py`, so in our case it would be:

`docker run -it -v $PWD/inference:/app/ NAME` 

assuming that we run this command in `tensorflow-great-barrier-reef` directory.

`-it` stand for running docker in an interactive mode, while `-v` stands for adding volume with aforementioned `inference` directory. That way, we are able to provide models and images directly to the docker container in order to perform inference.

In order to obtain image with predicted bounding boxes drawn, it is enough to run:

`python3 predictor.py`

as the result, file `result_image.png` is rendered.

