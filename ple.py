import argparse

import numpy as np
import cv2

def ple():
    pleser = argparse.ArgumentParser()
    pleser.add_argument('--num', '-n', type=int, default='0',
                        help='The number of your VerySimpleAnimals Colletion')
    pleser.add_argument('--victim', '-v', type=int, default='0',
                        help='The number of the VerySimpleAnimals Colletion to be fused')
    pleargs = pleser.parse_args()
    path = './ple'
    # Read the image
    ple1 = cv2.imread(path + '/' + 'VSA_' + str(pleargs.num) + '.jpg')
    if ple1 is None:
        print('Error: Cannot read the image ple')
        return
    ple2 = cv2.imread(path + '/' + 'VSA_' + str(pleargs.victim) + '.jpg')
    if ple2 is None:
        print('Error: Cannot read the image ple')
        return
    # Match the size of the two images
    ple1 = cv2.resize(ple1, (ple2.shape[1], ple2.shape[0]))
    # Attach each half of the two images so that ple1 is on the left and ple2 is on the right.
    ple = np.concatenate((ple1[:, :ple1.shape[1] // 2], ple2[:, ple2.shape[1] // 2:]), axis=1)
    # Save the image
    cv2.imwrite('chimera_' + str(pleargs.num) + '_' + str(pleargs.victim) + '.jpg', ple)

if __name__ == "__main__":
    ple()