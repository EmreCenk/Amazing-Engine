import os
from models.shapes_2d import triangle

possible_extensions = {".obj", ".txt"}


def parse_triangle_list(path, color = (255,255,255)):

    root, extension = os.path.splitext(path)

    if extension not in possible_extensions:
        raise Exception("Invalid path. File must be an obj file")

    try:
        file = open(path, "r") #opening the path

    except FileNotFoundError:

        raise FileNotFoundError(".obj file path is not valid. given path:",path)

    text_to_parse = file.read()
    file.close()
    text_to_parse = text_to_parse.split("\n")
    if text_to_parse[-1]=="":
        text_to_parse.pop(-1)



    all_triangles = []
    all_vertices = []

    for entry in text_to_parse:
        if len(entry) == 0 or entry[0] not in ["v", "f"]:
            continue

        entry = entry.replace("  ", " ")

        points = entry.split(" ")

        if entry[0:2] == "v ":
            current_entries = [float(points[1]), float(points[2]), float(points[3])]

            all_vertices.append(current_entries)


        elif entry[0:2] == "f ":
            if len(points)>4: #3 vertex numbers plus the 'f' at the beginning
                raise ValueError("This Engine does not support obj files with non-triangulated faces")

            for i in range(len(points)):
                points[i] = points[i].split("/")[0]

            current_entries = [int(points[1])-1, int(points[2])-1, int(points[3])-1] #these need to be integers since they are
            # indexes

            all_triangles.append(

                triangle(
                    v1 = all_vertices[current_entries[0]],
                    v2 = all_vertices[current_entries[1]],
                    v3 = all_vertices[current_entries[2]],
                    color = color
                )

            )

    return all_triangles,all_vertices


