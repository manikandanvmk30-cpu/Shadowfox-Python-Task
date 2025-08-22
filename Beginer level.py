import random


pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))



P = 1000
R = 5
T = 3
simple_interest = (P * R * T) / 100
print("Simple Interest:", simple_interest)


print("Formatted (Octal):", format(145, 'o'))

radius = 84
area = 3.14 * radius ** 2
print("Pond Area:", int(area))
print("Water Volume (liters):", int(area * 1.4))

distance = 490
time_seconds = 7 * 60
print("Speed (m/s):", int(distance / time_seconds))


justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After Recruitment:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman Leads:", justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Aquaman") + 1, "Superman")
print("Resolved Conflict:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Team:", justice_league)

justice_league.sort()
print("Sorted Team:", justice_league)
print("New Leader:", justice_league[0])


height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

def find_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    return None

c1 = find_country(city1)
c2 = find_country(city2)

if c1 and c2 and c1 == c2:
    print(f"Both cities are in {c1}")
else:
    print("They don't belong to the same country")

rolls = [random.randint(1, 6) for _ in range(20)]
count_6 = rolls.count(6)
count_1 = rolls.count(1)
count_2_sixes = sum(1 for i in range(len(rolls)-1) if rolls[i] == 6 and rolls[i+1] == 6)

print("6s Rolled:", count_6)
print("1s Rolled:", count_1)
print("Consecutive 6s:", count_2_sixes)

total_jacks = 0
for _ in range(10):
    total_jacks += 10
    print(f"Completed: {total_jacks}")
    tired = input("Are you tired? (yes/no): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            break

if total_jacks < 100:
    print(f"You completed a total of {total_jacks} jumping jacks.")
else:
    print("Congratulations! You completed the workout.")
