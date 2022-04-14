def calculateangle(hour, minute):
    m_2 = minute // 5

    g = ((12 - hour) * 5) + minute
    l = [g, minute]
    m1 = max(l)
    angle = m1 * 6
    if angle > 180:
        angle = 360 - angle

    if (6 < hour) and (m_2 < 6):
        return str(angle) + "°"
    elif (6 > hour) and (m_2 < 6):
        if angle < 0:
            angle = -1 * angle
        return str(angle) + "°"
    elif (6 < hour) and (m_2 > 6):
        if angle < 0:
            angle = -1 * angle
        return str(angle) + "°"
    elif (hour <= 6) and (m_2 >= 6):
        m0 = 60 - minute
        m1 = hour * 5
        m2 = m1 + m0
        angle = m2 * 6
        if angle > 180:
            angle = 360 - angle
        if angle < 0:
            angle = -1 * angle
        return str(angle) + "°"


print(calculateangle(11, 55))