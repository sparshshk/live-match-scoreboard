import requests
import time

API_KEY = "YOUR_API_KEY"
URL = "https://api.cricapi.com/v1/currentMatches"

def get_live_scores():
    params = {
        "apikey": API_KEY,
        "offset": 0
    }
    response = requests.get(URL, params=params)
    data = response.json()

    if "data" not in data:
        print("No live matches right now")
        return

    for match in data["data"]:
        print("-" * 40)
        print("Match:", match.get("name"))
        print("Status:", match.get("status"))

        if "score" in match and match["score"]:
            for team in match["score"]:
                print(
                    f"{team['inning']}: "
                    f"{team['r']}/{team['w']} "
                    f"in {team['o']} overs"
                )

while True:
    print("\nLIVE MATCH SCORES\n")
    get_live_scores()
    time.sleep(30)
