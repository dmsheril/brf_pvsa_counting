# from skimage import data
# from skimage.viewer import ImageViewer
#
# image = data.coins()
# viewer = ImageViewer(image)
# viewer.show()

import os
from skimage import io
from skimage.viewer import ImageViewer
import numpy as np
import shutil
import sys

path = "C:\\Users\\Delsey Sherrill\\Desktop\\BRF\\4_Strong_Positives"
fname = "2020-06-15-15-57-28_scan_Plate_TM_p00_0_B05f00d0_29.2M.TIF"
file = os.path.join(path, fname)
image = io.imread(file)
# viewer = ImageViewer(image)
# viewer.show()

# chipX = 100
# chipY = 100
chipX = 5000
chipY = 6000

chipRegionSize = 1000
chip1k = image[chipY:(chipY + chipRegionSize), chipX:(chipX + chipRegionSize), :]
# viewer2 = ImageViewer(chip1k)
# viewer2.show()

# # note: have to close first viewer before the 2nd one will open
# chipSize = 2000
# chip2k = image[chipX:chipX+chipSize, chipY:chipY+chipSize, :]
# viewer3 = ImageViewer(chip2k)
# viewer3.show()

# conclusion: I like 1k x 1k chips best for labeling

# chip out the middle portion, that is what I will pull chips from
midR = np.shape(image)[0] // 2 # integer will result from this division!
midC = np.shape(image)[1] // 2
# midR = 7370
# midC = 7963
chipRegionSize = 10000
r1 = midR - chipRegionSize // 2
r2 = midR + chipRegionSize // 2
c1 = midC - chipRegionSize // 2
c2 = midC + chipRegionSize // 2
chipRegion = image[r1:r2, c1:c2, :]
# viewer = ImageViewer(chipRegion)
# viewer.show()

# make the chips
fprefix, ext = os.path.splitext(fname)
chipDir = os.path.join(path, fprefix + "_chips")
if os.path.isdir(chipDir):
    answer = input("Directory {:s} exists; delete and regenerate chips? y/[n]  ".format(fprefix))
    if answer == "y":
        shutil.rmtree(chipDir)
    else:
        print("Ok, exiting...")
        sys.exit(0)

os.makedirs(chipDir)
chipC = midC - chipRegionSize // 2
chipR = midR - chipRegionSize // 2
chipSize = 1000
nChipsPerSide = 10
chipNum = 1
for i in range(0, nChipsPerSide):
    print("Saving chips for row {:d}".format(i+1))
    for j in range(0, nChipsPerSide):
        chip = image[chipR:chipR+chipSize, chipC:chipC+chipSize, :]
        chipFile = os.path.join(chipDir, "{:s}_CH{:03d}.png".format(fprefix, chipNum))
        io.imsave(chipFile, chip)
        chipC += chipSize
        chipNum += 1
    chipR += chipSize
    chipC = midC - chipRegionSize // 2







