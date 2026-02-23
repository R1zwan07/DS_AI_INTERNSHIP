# Temperature Analysis 

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

print("First reading (index 0):", temperatures[0])
print("Last reading (index -1):", temperatures[-1])

afternoon_peak = temperatures[3:6]
print("Afternoon Peak (indices 3:6):", afternoon_peak)

last_three_hours = temperatures[-3:]
print("Last 3 Hours (indices -3:):", last_three_hours)