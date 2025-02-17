"""Determine diplomacy type."""


def get_diplomacy_type(teams, players):
    """Get type of diplomacy."""
    if len(teams) == 2 and len(players) > 2:
        return 'TG'
    elif len(teams) == len(players) and len(players) > 2:
        return 'FFA'
    elif len(players) == 2:
        return '1v1'
    else:
        return 'Other'


def get_diplomacy_data(header, teams):
    """Compute diplomacy."""
    player_num = 0
    computer_num = 0
    for player in header.scenario.game_settings.player_info:
        if player.type == 'human':
            player_num += 1
        elif player.type == 'computer':
            computer_num += 1
    total_num = player_num + computer_num

    diplomacy = {}
    diplomacy['type'] = get_diplomacy_type(teams, header.scenario.game_settings.player_info[1:])
    team_sizes = sorted([len(team) for team in teams])
    diplomacy['team_size'] = 'v'.join([str(size) for size in team_sizes])
    if diplomacy['type'] == 'FFA':
        diplomacy['team_size'] = 'FFA'
    return diplomacy
