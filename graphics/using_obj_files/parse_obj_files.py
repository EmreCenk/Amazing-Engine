import os
from graphics.shapes_2d import triangle

possible_extensions = {".obj", ".txt"}

def parse_triangle_list(path, color = (255,255,255)):

    root, extension = os.path.splitext(path)

    if extension not in possible_extensions:
        raise Exception("File must be an obj file") #There might be a better error. At the moment, the name of the
        # Exception does not really matter

    try:
        file = open(path, "r") #opening the path

    except FileNotFoundError:
        raise FileNotFoundError(".obj file path is not valid")

    text_to_parse = file.read()
    file.close()
    text_to_parse = text_to_parse.split("\n")[:-1] #We remove the last entry since the last entry is an empty string
    all_triangles = []
    for entry in text_to_parse:
        if entry[0] != "f": # We only parse faces
            continue

        vertices = entry.split(" ")
        print(int(vertices[1]),
        int(vertices[2]),
        int(vertices[3]))
        all_triangles.append(

            triangle(
                v1 = int(vertices[1]),
                v2 = int(vertices[2]),
                v3 = int(vertices[3]),
                color = color
            )

        )

    return all_triangles




if __name__ == '__main__':
    parse_triangle_list("object_sample_files/sphere_example.obj")