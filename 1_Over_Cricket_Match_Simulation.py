import random

def toss(user_choice):
    outcomes = ["Heads", "Tails"]
    toss_result = random.choice(outcomes)
    return toss_result == user_choice, toss_result

def decide_play(team_won_toss):
    decision = input(f"{team_won_toss} won the toss! What do you want to do? Bat or Bowl? ").strip().capitalize()
    return decision

def play_ball():
    # Add no-ball and wide options
    outcome = random.choices(
        ['0', '1', '2', '3', '4', '6', 'W', 'NB', 'WD'],
        weights=[20, 30, 10, 5, 30, 20, 5, 5, 5],
        k=1
    )[0]

    if outcome == 'W':
        print("Wicket! A player is out.")
        return 0, False  # No runs scored on a wicket, player out
    elif outcome == 'NB':
        print("No Ball! Awarded 1 extra run.")
        return 1, True  # Award 1 extra run for no ball, continue the over
    elif outcome == 'WD':
        print("Wide Ball! Awarded 1 extra run.")
        return 1, True  # Award 1 extra run for wide, continue the over
    else:
        runs = int(outcome)
        print(f"Runs scored: {runs}")
        return runs, False  # Normal run

def play_over(team_name, opponent_runs=None):
    balls = 0
    total_runs = 0
    wickets = 0

    while balls < 6:
        runs, extra_ball = play_ball()
        total_runs += runs

        # Increment wickets only if a wicket occurs
        if runs == 0 and extra_ball is False:  # Count as a dot ball
            print("Dot ball, no runs scored.")
        elif runs == 0 and extra_ball:  # If it's a no-ball or wide, don't count it as a dot
            print("Extra delivery (No ball or Wide), no wicket counted.")
        elif runs == 0 and extra_ball is False:
            wickets += 1  # Increment wickets only if it's a legitimate dot ball

        # Count only legal deliveries
        if not extra_ball:
            balls += 1

        print(f"Total runs for {team_name}: {total_runs} after {balls} balls\n")

        # Check for 2 wickets
        if wickets >= 2:
            print(f"{team_name} lost 2 wickets. Innings ended.")
            break

        # Check if Team 2 has surpassed Team 1's score
        if opponent_runs is not None and total_runs > opponent_runs:
            print(f"{team_name} has scored more than {team1}. Innings ended.")
            break

    return total_runs, wickets

def play_match(team1, team2):
    print(f"\n{team1} is batting:")
    team1_runs, team1_wickets = play_over(team1)
    print(f"End of innings for {1}. Total runs: {team1_runs}\n")

    print(f"{team2} is batting:")
    team2_runs, team2_wickets = play_over(team2, team1_runs)
    print(f"End of innings for {team2}. Total runs: {team2_runs}\n")

    # Show final scores
    print("Final Scores:")
    print(f"{team1}: {team1_runs} runs")
    print(f"{team2}: {team2_runs} runs")

    if team2_runs > team1_runs:
        winner = f"{team2} wins!"
    elif team1_runs > team2_runs:
        winner = f"{team1} wins!"
    else:
        winner = "It's a tie!"

    print(winner)

# Input for the two teams
team1 = input("Enter the name of Team 1: ")
team2 = input("Enter the name of Team 2: ")

# User inputs their choice for the toss
user_choice = input(f"{team1}, choose Heads or Tails for the toss: ").strip().capitalize()

# Simulate the toss
user_won_toss, toss_result = toss(user_choice)
print(f"Toss Result: {toss_result}")

if user_won_toss:
    decision = decide_play(team1)
    print(f"{team1} won the toss and decided to {decision} first.")
else:
    decision = decide_play(team2)
    print(f"{team2} won the toss and decided to {decision} first.")

# Input playing XI for both teams
print("Now I would like to call the captain of the team to tell the playing XI:")
print("Firstly", team1)

team1_11 = list(map(str, input(f"Playing 11 for {team1}: ").split(" ")))
team2_11 = list(map(str, input(f"Playing 11 for {team2}: ").split(" ")))

print(f"Playing 11 for {team1}:")
for player in team1_11:
    print(player)

print(f"\nPlaying 11 for {team2}:")
for player in team2_11:
    print(player)

# Start the match
play_match(team1,team2)