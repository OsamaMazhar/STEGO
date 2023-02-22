import os
from pycocotools.coco import COCO
from tqdm import tqdm

data_dir = './dataset'
cat_names = ['elephant', 'giraffe']
for data_type in ['train2017', 'val2017']:
    for idx, cat_name in enumerate(cat_names):
        img_count = 0
        annFile = '{}/cocostuff/annotations_json/instances_{}.json'.format(data_dir, data_type)
        coco = COCO(annFile)
        save_path = os.path.join(data_dir, 'cocostuff', 'curated', data_type, f'COCO_{cat_name}_{data_type}.txt')
        f = open(save_path, 'w')
        cat_ids = coco.getCatIds(catNms=[cat_name])
        print(f'category id for {cat_name} is: {cat_ids}')
        image_ids = coco.getImgIds(catIds=cat_ids)
        for img_id in tqdm(image_ids[:]):
            f.write(os.path.splitext(coco.imgs[img_id]['file_name'])[0] + "\n")
            img_count += 1
        print(f'Number of images for {cat_name} class: {img_count}')
