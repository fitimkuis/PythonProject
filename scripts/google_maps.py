# import gmplot package
import gmplot

latitude_list = [ 60.924434, 60.920038, 60.920810 ]
longitude_list = [ 24.644376, 24.639001, 24.651361 ]

gmap5 = gmplot.GoogleMapPlotter(60.922744, 24.647273, 14)

gmap5.scatter(latitude_list, longitude_list, '# FF0000', size = 40, marker = False)


#gmap5.apikey = "AIzaSyAEjjaGDHdkDsPxoSKjjtvskIBC3EhsHlk"

# polygon method Draw a polygon with
# the help of coordinates
gmap5.polygon(latitude_list, longitude_list, color = 'cornflowerblue')

gmap5.draw("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/scripts/map15.html")