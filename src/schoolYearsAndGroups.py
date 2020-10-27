def csSchoolYearsAndGroups(years, groups):
    # yearList = list(range(1, years + 1, 1))
    # stringList = [str(int) for int in yearList]
    # yearString = ",".join(stringList)

    yr = 1
    alphaNumYr = ""
    while yr <= years:
        group = 0
        letter = 'a'
        while group < groups:
            group += 1
            letter = chr(ord('`') + group)
            alphaNumYr += ('%s%s, ' % (yr, letter))
        yr += 1

        size = len(alphaNumYr)

    return alphaNumYr[:size -2]




print(csSchoolYearsAndGroups(4, 3))
