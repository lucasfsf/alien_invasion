import json

high_score_file = 'high_score.json'

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state. 
        self.game_active = False

        # High score should never be reset.
        self.high_score = self._get_stored_high_score()
    

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def _get_stored_high_score(self):
        """Checks if a high score file exists and tries to retrieve 
        value from this file"""
        try:
            with open(high_score_file) as f:
                # Gets stored high score and stores it in a json file
                high_score = json.load(f)
        except FileNotFoundError:
            # Returns 0 as the default hs when starting the game
            return 0
        else:    
            return high_score


