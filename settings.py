import os
import glob

# SCREEN
WIDTH = 640
HEIGHT = 480

#DATA
P_W = 80 # WIDTH
P_H = 85 # HEIGHT
POOL_XYS = (
                  ((2*P_W, 1*P_H),(3*P_W, 1*P_H),(4*P_W, 1*P_H)),
    ((1*P_W, 2*P_H),(2*P_W, 2*P_H),(3*P_W, 2*P_H),(4*P_W, 2*P_H),(5*P_W, 2*P_H)),
    ((1*P_W, 3*P_H),(2*P_W, 3*P_H),(3*P_W, 3*P_H),(4*P_W, 3*P_H),(5*P_W, 3*P_H)),
                  ((2*P_W, 4*P_H),(3*P_W, 4*P_H),(4*P_W, 4*P_H)),
    )

DATA_DIR = ''

DATA_IMAGE = 'images'

IMAGE_FORMAT = 'png'

COLORS = [c.split("_")[1].split(".")[0] for c in glob.glob("%s/pez_*.%s" % (DATA_IMAGE, IMAGE_FORMAT))]

IMAGES = {
    'pool_background': os.path.join(DATA_IMAGE, 'pool_background%sx%s.%s' % (WIDTH, HEIGHT, IMAGE_FORMAT)),
    'cagna': os.path.join(DATA_IMAGE, 'cagna.%s' % (IMAGE_FORMAT)),
    'anzuelo': os.path.join(DATA_IMAGE, 'anzuelo.%s' % (IMAGE_FORMAT)),
    }

for c in COLORS:
    IMAGES['pez_%s' % c] = os.path.join(DATA_IMAGE, 'pez_%s.%s' % (c, IMAGE_FORMAT))

CAGNA = (
    {'name': 'Humano',
     'x':400,
     'y': 300,
     }
    )

P_T_H_SEP = 60
P_T_V_SEP = 50
P_T_WL = 500
P_T_WR = P_T_WL + P_T_H_SEP 
P_T_HB = 50

PS = (
    (P_T_WR, P_T_HB * 9),
    (P_T_WL, P_T_HB * 9),
    (P_T_WR, P_T_HB * 8),
    (P_T_WL, P_T_HB * 8),
    (P_T_WR, P_T_HB * 7),
    (P_T_WL, P_T_HB * 7),
    (P_T_WR, P_T_HB * 6),
    (P_T_WL, P_T_HB * 6),
    (P_T_WR, P_T_HB * 5),
    (P_T_WL, P_T_HB * 5),
    (P_T_WR, P_T_HB * 4),
    (P_T_WL, P_T_HB * 4),
    (P_T_WR, P_T_HB * 3),
    (P_T_WL, P_T_HB * 3),
    (P_T_WR, P_T_HB * 2),
    (P_T_WL, P_T_HB * 2),
    (P_T_WR, P_T_HB * 1),
    (P_T_WL, P_T_HB * 1),
    )
