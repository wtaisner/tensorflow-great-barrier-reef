# ~~tensorflow~~ torch-great-barrier-reef

#### Kaggle competition:
https://www.kaggle.com/c/tensorflow-great-barrier-reef

#### Requirements:
https://docs.google.com/document/d/1ncurueGQyY-JGWw1YunEkOgoUZtA5ivJUcvZ8HuyDy4/edit

####DVC 
should work :) - for detailed explanation and tips see [website](https://dvc.org/doc/start/data-and-model-versioning)
basic operations are:

`dvc pull` to retrieve data (rather irrelevant in our project)

Making changes:
- after making some change to the *data* directory (i.e. adding new model, etc.), it should be added with `dvc add data/PATH`
- usually it also requires `git commit` and `dvc push` to save the changes

I will post further information while versoning I guess