conversion = {"x":0,
              "y":1,
              "z":2,
              "X":0,
              "Y":1,
              "Z":2,
              }

excluded = {
    "x":[1, 2],
    "y":[0, 2],
    "z":[0, 1],
    "X":[1, 2],
    "Y":[0, 2],
    "Z":[0, 1],
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
}

ang_conversion = {"x":3,
              "y":4,
              "z":5,
              "X":3,
              "Y":4,
              "Z":5,
              }

TOP = {(1,0,1,0),
       (1,0,0,0),
       (1,0,0,1)}

BOTTOM = {(0,1,1,0),
          (0,1,0,0),
          (0,1,0,1)}

#Shape tags:
OBJ = 0
SPHERE = 1
CUBE = 2
PYRAMID = 3

#Drawing styles:
WIREFRAME = 1
SOLID = 2
