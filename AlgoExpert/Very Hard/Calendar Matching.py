'''
Take in two calendars of meetings, find free time inbetween to schedule a meeting together

https://www.algoexpert.io/questions/calendar-matching

⚫ Very Hard Difficulty
'''

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    unavailability1 = unavailability(calendar1, dailyBounds1)
    unavailability2 = unavailability(calendar2, dailyBounds2)
    mergedCal = mergeCals(unavailability1, unavailability2)
    flattenedCal = flattenCal(mergedCal)
    # print(flattenedCal)
    return getMatchingAvailabilities(flattenedCal, meetingDuration)


def unavailability(calendar, bounds):
    unavailabilityCal = calendar
    unavailabilityCal.insert(0, ["0:00",bounds[0]])
    unavailabilityCal.append([bounds[1], "23:59"])
    #investigate lambda functions
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], unavailabilityCal))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def mergeCals(cal1, cal2):
    merged = []
    i, j = 0, 0
    while i < len(cal1) and j < len(cal2):
        meeting1, meeting2 = cal1[i], cal2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    while i < len(cal1):
        merged.append(cal1[i])
        i += 1
    while j < len(cal2):
        merged.append(cal2[j])
        j += 1
    return merged

def flattenCal(cal):
    flattened = [cal[0][:]]
    for i in range(1, len(cal)):
        currentMeeting = cal[i]
        previousMeeting = flattened[-1]
        currentStart, currentEnd = currentMeeting
        # print(previousMeeting)
        previousStart, previousEnd = previousMeeting
        if previousEnd >= currentStart:
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            flattened[-1] = newPreviousMeeting 
        else:
            flattened.append(currentMeeting)
    return flattened

def getMatchingAvailabilities(cal, duration):
    matched = []
    for i in range(1, len(cal)):
        start = cal[i - 1][1]
        end = cal[i][0]
        availableDuration = end - start
        if availableDuration >= duration:
            matched.append([start,end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matched))

def minutesToTime(total):
    hours = total // 60
    minutes = total % 60
    hoursString = str(hours)
    if minutes < 10:
        minutesString = "0" + str(minutes)
    else:
        minutesString = str(minutes)
    return hoursString + ":" + minutesString


#sample input
cal1 = [
  ["9:00", "10:30"],
  ["12:00", "13:00"],
  ["16:00", "18:00"]
]
daily1 = ["9:00", "20:00"]
cal2 = [
  ["10:00", "11:30"],
  ["12:30", "14:30"],
  ["14:30", "15:00"],
  ["16:00", "17:00"]
]
daily2 = ["10:00", "18:30"]
duration = 30

calendarMatching(cal1,daily1,cal2,daily2,duration)