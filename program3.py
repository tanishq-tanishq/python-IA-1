#	A traffic system records the average speed of vehicles every hour for 12 hours.Write a program that: Reads 12 speed values (floats). Calculates the average speed. Displays whether traffic flow was “Slow” (avg < 40), “Normal” (40–80), or “Fast” (avg > 80).


speeds = []  


print("Enter speed values for 12 hours:")
for i in range(12):
    speed = float(input(f"Enter The Speed: "))
    speeds.append(speed)


average_speed = sum(speeds) / 12

print("\nAverage Speed:", round(average_speed, 2), "km/h")

#
if average_speed < 40:
    print("Slow")
elif 40 <= average_speed <= 80:
    print("Normal")
else:
    print("Fast")
