from PIL import Image

def compare():
    i1 = Image.open("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/testcases/images/google1.png")
    i2 = Image.open("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/testcases/images/google1.png")
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)

def histogram_entropy(im):
    """ Calculate the entropy of an images' histogram.
    Used for "smart cropping" in easy-thumbnails;
    see also https://raw.github.com/SmileyChris/easy-thumbnails/master/easy_thumbnails/utils.py
    """
    if not isinstance(im, Image.Image):
        return 0  # Fall back to a constant entropy.

    histogram = im.histogram()
    hist_ceil = float(sum(histogram))
    histonorm = [histocol / hist_ceil for histocol in histogram]
    print(histonorm)
    return histonorm


i1 = Image.open("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/testcases/images/google1.png")
i2 = Image.open("C:/Users/fitim/IdeaProjects/PythonProject/PythonProject/testcases/images/google1.png")
histo1 = histogram_entropy(i1)
histo2 = histogram_entropy(i2)
print(set(histo1) & set(histo2))
print([x for x in histo1 if x in histo2])

histo1.sort()
histo2.sort()
if histo1 == histo2:
    print ("The images are identical")
else :
    print ("The images are not identical")

compare()