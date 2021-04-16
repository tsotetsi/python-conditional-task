# JHB Metro Police Demerit System Program.
driver_speed = float(input("What was your average speed on the road in km/h?: "))
road_speed = float(input("What was the allowed road speed?: "))

points = (driver_speed - road_speed)/5

if driver_speed <= 60:
    print("OK")
elif driver_speed > road_speed:
    print("Points: " +str(points))

    if points > 12:
        print("Time to go to jail")
