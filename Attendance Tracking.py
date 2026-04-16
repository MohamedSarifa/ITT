day1 = {101, 102, 103, 105}
day2 = {102, 104, 105, 106}

print("Present both days:", day1 & day2)
print("Present either day:", day1 | day2)
print("Absent on second day (but present on first):", day1 - day2)
