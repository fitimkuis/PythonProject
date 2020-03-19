import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def fetch_colour_name(rgb):
    print(rgb)
    if 'rgba' in rgb:
        rgb = rgb.replace('rgba','')
        tup = eval(rgb)
        my_list = list(tup)
        my_list.pop(3)
    else:
        rgb = rgb.replace('rgb','')
        tup = eval(rgb)
        my_list = list(tup)

    requested_colour = (my_list[0], my_list[1], my_list[2])
    actual_name, closest_name = get_colour_name(requested_colour)
    print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
    return closest_name







