
import mysql.connector

# Establish the connection
cnx = mysql.connector.connect(user='root', password='0612sebaynuria', host='localhost', database='home_league')
cursor = cnx.cursor()

# List of matches for matchday 1
matches = [
    ("Ibu 600", "M&M"),
    ("Rivera", "The rits"),
    ("Red Boys", "Caudillos"),
    ("Lil king arthur", "Chichones")
]

# Function to handle the matchday
def handle_matchday(matches):
    print("\nMatchday 1:\n")

    # Simulate matches and input scores
    for match in matches:
        home_team, away_team = match

        # Input scores in the format "5-3"
        score_input = input(f"Enter the score for {home_team} vs {away_team} (for example, 5-3): ")
        home_score, away_score = map(int, score_input.split('-'))

        # Update LeagueTable based on the match result
        update_query = (
            "UPDATE LeagueTable "
            "SET PJ = PJ + 1, "
            "    G = G + %s, "
            "    E = E + %s, "
            "    P = P + %s, "
            "    GF = GF + %s, "
            "    GE = GE + %s, "
            "    GT = GT + %s, "
            "    Pts = Pts + %s "
            "WHERE Club = %s"
        )
        cursor.execute(update_query, (1 if home_score > away_score else 0, 1 if home_score == away_score else 0, 1 if home_score < away_score else 0, home_score, away_score, home_score - away_score, 3 if home_score > away_score else 1 if home_score == away_score else 0, home_team))
        cursor.execute(update_query, (1 if away_score > home_score else 0, 1 if away_score == home_score else 0, 1 if away_score < home_score else 0, away_score, home_score, away_score - home_score, 3 if away_score > home_score else 1 if away_score == home_score else 0, away_team))

    # Confirm the changes for the matchday
    cnx.commit()

# Handle the matchday
handle_matchday(matches)

# Close the connection
cursor.close()
cnx.close()
