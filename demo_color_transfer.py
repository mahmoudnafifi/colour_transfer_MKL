import PIL.Image as Image
import numpy as np
from utils import color_transfer_MKL as ct

main_dir = 'imgs/'
source = main_dir + 'source.jpg'
target = main_dir + 'target.jpg'
out = main_dir + 'output.jpg'

source = Image.open(source)
source = np.array(source)/255
target = Image.open(target)
target = np.array(target)/255

result = ct.color_transfer_MKL(source, target)
img = Image.fromarray(np.uint8(result * 255))
img.save(out)