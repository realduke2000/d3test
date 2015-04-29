#!/usr/bin/python

import Image
import ImageDraw
import ImageColor
import sys
import os

MAX_HITS = 10.0
COLOR_RANGE = 16
UNIT = MAX_HITS / COLOR_RANGE

FILE_PATH = "heatmap.png"
IMAGE_WIDTH = 2048
IMAGE_HEIGHT = 1024
POINTS_PATH = "points.txt"

def readPoints(file):
    points=dict()
    f = open(file)
    try:
        for line in f:
            x = line.split(' ')[0].strip()
            y = line.split(' ')[1].strip()
            p = (int(x),int(y))
            hit = points.get(p)
            if hit is None:
                hit = 0
            else:
                hit += 1
            points[p] = hit
        return points
    finally:
        f.close()

def get_color(hits):
    col = "#FFECEC"

    if hits >= 0 and hits <= UNIT * 1:
        col = "#ffd2d2"
    elif hits > UNIT * 1 and hits <= UNIT * 2:
        col = "#FFB5B5"
    elif hits > UNIT * 2 and hits <= UNIT * 3:
        col = "#FF9797"
    elif hits > UNIT * 3 and hits <= UNIT * 4:
        col = "#FF7575"
    elif hits > UNIT * 4 and hits <= UNIT * 5:
        col = "#FF5151"
    elif hits > UNIT * 5 and hits <= UNIT * 6:
        col = "#FF2D2D"
    elif hits > UNIT * 6 and hits <= UNIT * 7:
        col = "#FF0000"
    elif hits > UNIT * 7 and hits <= UNIT * 8:
        col = "#EA0000"
    elif hits > UNIT * 8 and hits <= UNIT * 9:
        col = "#CE0000"
    elif hits > UNIT * 9 and hits <= UNIT * 10:
        col = "#AE0000"
    elif hits > UNIT * 10 and hits <= UNIT * 11:
        col = "#930000"
    elif hits > UNIT * 11 and hits <= UNIT * 12:
        col = "#750000"
    elif hits > UNIT * 12 and hits <= UNIT * 13:
        col = "#600000"
    elif hits > UNIT * 13 and hits <= UNIT * 14:
        col = "#4D0000"
    elif hits > UNIT * 14 and hits <= UNIT * 15:
        col = "#2F0000"
    return col

def aggregatePointsColor(points):
    for p in points:
        points[p] = ImageColor.getrgb(get_color(points[p]))
    return points

def writeImage(points):
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

    im = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(im)

    for p in points:
        draw.point(p, fill=points[p])
    del draw
    im.save(FILE_PATH)

def main(args):
    points = readPoints(POINTS_PATH)
    points = aggregatePointsColor(points)
    writeImage(points)

if __name__=="__main__":
    main(sys.argv[1:])
