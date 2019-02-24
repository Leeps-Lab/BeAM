from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from otree_redwood.models import DecisionGroup
from otree_redwood.utils import DiscreteEventEmitter


import csv

author = 'Your name here'

doc = """
Your app description
"""

def parse_config(config):
    # parsingmethod for the config files
    with open( 'beam/configs/' +  config) as config_file:
        data = list(csv.DictReader(config_file))


    configs = {
        'A_indices': float(data[0]['period_length']),
        'B_indices': float(data[0]['tick_length']),
        'A_types': float(data[0]['game_constant']),
        'B_types': float(data[0]['a_sto']),
        'surplus_values': float(data[0]['b_sto']),
        'time_limit': float(data[0]['s_sto']),
        'num_rounds': float(data[0]['x_0']),
    }
    return configs

class Constants(BaseConstants):
    name_in_url = 'beam'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    side = models.StringField()
    player_id = models.IntegerField()
    player_type = models.IntegerField()
    demands = models.IntegerField()
    
    
    # boolean list will ned o deal with it 
    can_select = models.IntegerField()
    
    # Commited can be abstracted down to be the index of the commit,
    # not the full list where only one index has a value
    commited = models.IntegerField()
