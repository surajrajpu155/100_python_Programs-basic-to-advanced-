# 10. Write a program to read seconds and convert them into hours, minutes and seconds.

total_seconds = int(input("Enter seconds value you want to convert into hours, minutes and the seconds: "))

hours = total_seconds / 3600
minutes = total_seconds / 60
second = total_seconds

print(f"{total_seconds} second in hour is {hours}")
print(f"{total_seconds} second in minutes is {minutes}")
print(f"{total_seconds} second in second is {second}")


# ------------------------------------------------------------------


total_seconds = int(input("Enter seconds value you want to convert: "))

# Calculate hours, minutes, and remaining seconds
hours = total_seconds // 3600 

remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Display the converted time duration
print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
