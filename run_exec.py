
a = ""

while 1:
    a = input("Pick a number from 1 to 6 (inclusive):")
    try:
        a = int(a)
        if a<=6 and 1<=a:
            break

    except:pass

if a == 1:
    from tests_and_examples import rotating_cube

elif a == 2:
    from tests_and_examples import shape_demonstration

elif a == 3:
    from tests_and_examples import creating_text

elif a == 4:
    from tests_and_examples import teapot

elif a == 5:
    from tests_and_examples import dna

elif a == 6:

    from tests_and_examples import cube_of_cubes
