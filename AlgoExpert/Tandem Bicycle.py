def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalSpeed = 0
    if fastest == True:
    #find the fastest speed
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse = True)  
        for speed in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[speed],blueShirtSpeeds[speed])
        return totalSpeed
    else:
    #find the slowest 
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort() 
        for speed in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[speed],blueShirtSpeeds[speed])
        return totalSpeed