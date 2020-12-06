def min_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the minimum value over all legal successors
   
    # HINT: Assume that the utility is ALWAYS calculated for
            player 1, NOT for the "active" player
    """
    utility = gameState.utility(0)
    if utility == 0:
        available_actions = gameState.actions()
        min_move = float("inf")
        for action in available_actions:
            min_move = min(min_move, max_value(gameState.result(action)))
        return min_move
    return utility


def max_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the maximum value over all legal successors
   
    # HINT: Assume that the utility is ALWAYS calculated for
            player 1, NOT for the "active" player
    """
    utility = gameState.utility(0)
    if utility == 0:
        available_actions = gameState.actions()
        max_move = float("-inf")
        for action in available_actions:
            max_move = max(max_move, min_value(gameState.result(action)))
        return max_move
    return utility