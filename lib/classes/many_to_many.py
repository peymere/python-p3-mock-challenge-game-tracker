class Game:
    def __init__(self, title):
        self.title = title

    def results(self):
        return [results for results in Result.all if results.game == self]

    def players(self):
        return list({result.player for result in self.results() if isinstance(result.player, Player)})

    def average_score(self, player):
        if len(self.results()) == 0:
            return 0
        player_scores = [result.score for result in self.results() if result.player == player]
        return sum(player_scores) / len(player_scores)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 1:
            raise ValueError("Title must be 1 or more characters")
        if hasattr(self, "_title"):
            raise AttributeError("Title can not be changed")
        self._title = title

class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    def results(self):
        return [results for results in Result.all if results.player == self]

    def games_played(self):
        return list({result.game for result in self.results() if isinstance(result.game, Game)})

    def played_game(self, game):
        if game in self.games_played():
            return True
        return False

    def num_times_played(self, game):
        play_count = 0
        for result in self.results():
            if isinstance(result.game, Game) and result.game == game:
                play_count += 1
        return play_count

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        if len(username) < 2 or len(username) > 16:
            raise ValueError("username must be between 2 to 16 characters")
        self._username = username

    @classmethod
    def highest_scored(cls, game):
        players = game.players()
        if not players:
            return None
        best_player = max(players, key=lambda player: game.average_score(player))
        return best_player

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        self._game = game

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError("score must be an integer")
        if score < 1 or score > 5000:
            raise ValueError("score must be between 2 to 16 characters")
        if hasattr(self, "_score"):
            raise AttributeError("Score can not be changed")
        self._score = score