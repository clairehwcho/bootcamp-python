# 1. Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    # NINJA BONUS: Add an @class method that, given a list of dictionaries, populates and returns a new list of Player objects.
    @classmethod
    def get_team(cls, player_dict):
        player_objects = []
        for player in player_dict:
            player_objects.append(cls(player))
        return player_objects

    # When you type print(), it will check __repr__(self) method first to see if there is any default way of representing the object.
    # It tells python how to handle representing that class
    def __repr__(self):
        display = f"Player: {self.name}, {self.age} years old, position: {self.position}, team: {self.team}"
        return display



# 2. Given these variables, create Player instances for each of the following dictionaries.
# Be sure to instantiate these outside the class definition, in the outer scope.
kevin = {
        "name": "Kevin Durant",
        "age":34,
        "position": "small forward",
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum",
        "age":24,
        "position": "small forward",
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving",
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(player_kevin)
print(player_jason)
print(player_kyrie)

# 3. Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players)
# write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32,
        "position": "Point Guard",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard",
    	"age":33,
        "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32,
        "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# pseudo-coding
    # for loop over the list of dictionaries
    # each time use that dictionary info
    # to create a new player instance

new_team = []

for player_dict in players: # for val in list:
    player = Player(player_dict)
    new_team.append(player)
print(new_team)


