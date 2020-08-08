# FlipkartGrid (Team Ignitors - Fashion Intelligence)
This repo focusses on classifying clothes into different categories. A simple Code, which predicts the categories of clothes like shirt/dress/skirt etc.

**Running the Model & Training with dataset:-**
* Download the [Dataset](https://drive.google.com/drive/folders/0B7EVK8r0v71pekpRNUlMS3Z5cUk) and place it inside [This folder](https://github.com/Debanitrkl/FlipkartGrid/tree/master/Cloth_Classifier/data/cloth_categories)
* Run `python train.py`, after training a resnet-34 model will be saved in a model folder. 
* Evaluate with `python test.py`, The accuracy is more than 90%.

**Requirements:-**
* fastai
* Pytorch with cuda10.0 + 
