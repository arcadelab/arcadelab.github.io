import glob
import re
import numpy as np
from PIL import Image

pattern = r'(?P<name>[a-zA-z]+)_art_small\.png'
for fname in glob.glob('*.png'):
    if (m := re.match(pattern, fname)) is not None:
        img = np.array(Image.open(fname))
        indices = np.logical_and(np.all(img[:,:,0:1] == img, 2), np.all(img > 160, 2))
        indices = np.logical_or(indices, img.mean(2) > 210)
        #img = np.concatenate([img, 255 * np.ones((img.shape[0], img.shape[1], 1), dtype=img.dtype)], axis=2)
        img[indices, :] = 234
        Image.fromarray(img).save('{}_art_modify.png'.format(m.group('name')))
