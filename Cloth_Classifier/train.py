from fastai import *
from fastai.vision import *
path = Path("/home/biswajit/Desktop/Fine-Grained-Clothing-Classification/data/cloth_categories")
data = ImageDataBunch.from_csv(path, csv_labels="train_labels.csv", ds_tfms=get_transforms(), size=224)
data.normalize(imagenet_stats)
data.show_batch(rows=8, figsize=(14,12))
print(data.classes)
print (len(data.classes),data.c)
learn = create_cnn(data, models.resnet34, metrics=accuracy)
learn.fit_one_cycle(1)
learn.save('stage-1_arch-34_sz-150')
