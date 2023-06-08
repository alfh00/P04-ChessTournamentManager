import json
import jsonpickle


path = "./db/tournaments.json"

def load_data():
    with open(path, "r") as f:
        data = json.load(f)["tournaments"]
        # print(data)

    tournaments = [jsonpickle.decode(tournament) for tournament in data]
    # jsonpickle.decode(data["tournaments"])
    print()
    t = list(filter(lambda x: x.name =="tour1", tournaments))

load_data()