from fastai import *
from fastai.vision import *
path = Path("/home/biswajit/Desktop/Fine-Grained-Clothing-Classification/data/cloth_categories")
data = ImageDataBunch.from_csv(path, csv_labels="test_labels.csv", ds_tfms=get_transforms(), size=224)
data.normalize(imagenet_stats)
# data.show_batch(rows=8, figsize=(14,12))
# print(data.classes)
# print (len(data.classes),data.c)
learn = create_cnn(data, models.resnet34, metrics=accuracy)
learn.load('stage-1_arch-34_sz-150')
output, target = learn.get_preds()
interp = ClassificationInterpretation.from_learner(learn)
interp.plot_top_losses(9, figsize=(15,11))
print(interp.most_confused(min_val=0))
