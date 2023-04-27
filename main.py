from views.principal_menu import main
import curses


def app():
    main()


if __name__ == "__main__":
    app()

# with open("./models/players.json", "r") as f:
#     players = json.load(f)
#     temp = []
#     for player in players:
#         old_id = player["id"]
#         new_id = old_id[:2].upper() + old_id[2:]
#         player["id"] = new_id
#         temp.append(player)
#     with open("./models/players.json", "w") as f:
#         json.dump(temp, f, indent=4)
