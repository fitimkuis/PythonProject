import webcolors

class Colour(object):

    def __init__(self):
        self.__my_list = []

    def closest_colour(self,requested_colour):
        min_colours = {}
        for key, name in webcolors.css3_hex_to_names.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = name
        return min_colours[min(min_colours.keys())]

    def get_colour_name(self,requested_colour):
        try:
            closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
        except ValueError:
            closest_name = self.closest_colour(requested_colour)
            actual_name = None
        return actual_name, closest_name


    def fetch_colour_name(self,rgb):
        if 'rgba' in rgb:
            rgb = rgb.replace('rgba','')
            tup = eval(rgb)
            self.__my_list = list(tup)
            self.__my_list.pop(3)
        else:
            rgb = rgb.replace('rgb','')
            tup = eval(rgb)
            self.__my_list = list(tup)

        requested_colour = (self.__my_list[0], self.__my_list[1], self.__my_list[2])
        actual_name, closest_name = self.get_colour_name(requested_colour)
        print ("Actual colour name:", actual_name, ", closest colour name:", closest_name)
        #convert_to_hex(requested_colour)
        return closest_name

    def convert_to_hex(self):
        hex = '#{:02x}{:02x}{:02x}'.format(self.__my_list[0], self.__my_list[1], self.__my_list[2])
        return hex

#col = Colour()
#print(col.fetch_colour_name("rgb(255, 255, 255)"))
#print(col.convert_to_hex())





