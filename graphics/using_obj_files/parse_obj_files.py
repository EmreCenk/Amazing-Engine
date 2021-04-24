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
    text_to_parse = text_to_parse.split("\n")
    if text_to_parse[-1]=="":
        text_to_parse.pop(-1)

    print(text_to_parse[0][0],"r")
    while text_to_parse[0][0] in [ "#", "o"]:
        text_to_parse.pop(0)


    all_triangles = []
    all_vertices = []

    for entry in text_to_parse:
        points = entry.split(" ")
        if "s o" in entry or entry == "":
            continue

        if entry[0] == "v":
            current_entries = [float(points[1]), float(points[2]), float(points[3])]

            all_vertices.append(current_entries)
            continue


        current_entries = [int(points[1])-1, int(points[2])-1, int(points[3])-1] #these need to be integers since they are
        # indexes
        print(len(all_vertices),current_entries)

        all_triangles.append(

            triangle(
                v1 = all_vertices[current_entries[0]],
                v2 = all_vertices[current_entries[1]],
                v3 = all_vertices[current_entries[2]],
                color = color
            )

        )

    return all_triangles,all_vertices




if __name__ == '__main__':
    parse_triangle_list("sample_object_files/sphere_example.obj")