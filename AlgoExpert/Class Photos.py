'''
.sort() two arrays, compare the heights, if 
one row is taller than every mathcing pair then 
true if not false.

https://www.algoexpert.io/questions/class-photos

'''


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for idx, redshirt in enumerate(redShirtHeights):
        if max(redShirtHeights) > max(blueShirtHeights):
            if redshirt <= blueShirtHeights[idx]:
                print("False")
                return False
        else:
            if redshirt >= blueShirtHeights[idx]:
                print("False")
                return False
    print("True")
    return True

