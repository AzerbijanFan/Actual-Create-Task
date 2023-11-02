import random


teams = []

for i in range(2):
    team_name = input(f"Enter the name of Team {i + 1}: ")
    teams.append(team_name)

coin_toss_result = random.choice(["Heads", "Tails"])
print(f"Coin toss result: {coin_toss_result}")

if coin_toss_result == "Heads":
    first_possession_team = teams[0]
else:
    first_possession_team = teams[1]

print(f"{first_possession_team} will have the first possession.")
