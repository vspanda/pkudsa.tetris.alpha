import main

t = {}
t['a'] = "AlphaTetris"
t['b'] = "betaTetris"
t['o'] = "omegaTetris"

scores = dict()
for key, val in enumerate(t):
    scores[f"{val}-first"] = 0
    scores[f"{val}-second"] = 0


n = 10
team1 = 'a'
team2 = 'o'

for i in range(n):
    t1 = team1 if i % 2 == 0 else team2
    t2 = team2 if i % 2 == 0 else team1
    x = main.main(t[t1], t[t2])
    if x == 1:
        scores[f"{t1}-first"] += 1
        # scores[f"{teams[t1]}-second"] += 1

    elif x == 2:
        # scores[f"{teams[t2]}-first"] += 1
        scores[f"{t2}-second"] += 1

print(f"SCORES FROM {n} Matches")
print(f"{t[team1]} Going First: {scores[f'{team1}-first']}")
print(f"{t[team1]} Going Second: {scores[f'{team1}-second']}")
print()
print(f"{t[team2]} Going First: {scores[f'{team2}-first']}")
print(f"{t[team2]} Going Second: {scores[f'{team2}-second']}")