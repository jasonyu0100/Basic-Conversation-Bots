import re
import random

def on_enter_state(state, data):
    return state_dict.get(state, none_state)(data)

def on_input_state(state, text, data):
    return input_state_dict.get(state, none_input_state)(text, data)

def no_query_on_enter_state(data):
    print("What would you like to do?")

def outside_on_enter_state(data):
    print("Would you like to play outside?")

def none_state(data):
    raise Exception("State is not valid")

def no_query_on_input(text, data):
    match = re.search('I want to (?P<verb>do|play|watch) (?P<activity>.*)', text)
    if match:
        activity = match.group('activity')
        verb = match.group('verb')
        if activity in activities:
            return 'END', {'activity':activity, 'verb':verb}
        else:
            print('That activity is not available.')
            return 'END', None
    else:
        return 'END', None

def outside_on_input(text, data):
    check = text.lower()
    if check == "yes":
        return 'END', None
    else:
        return 'END', None


def none_input_state(data):
    raise Exception("Input State is not valid")

def on_exit_query(data):
    activity = data['activity']
    verb = data.get('verb','do')
    print(f"Have fun {verb}ing {activity}")


state_dict = {
    'NO QUERY': no_query_on_enter_state,
    'OUTSIDE': outside_on_enter_state,
}

input_state_dict = {
    'NO QUERY': no_query_on_input,
    'OUTSIDE': outside_on_input,
}

activities = {
    'soccer': {
        'group': True,
        'outside': True,
        'time': 60 #Minutes
    },
    'ping pong': {
        'group': False,
        'outside': True,
        'time': 10 #Minutes
    },
    'big two': {
        'group': True,
        'outside': False,
        'time': 10 #Minutes
    },
    'movie': {
        'group': False,
        'outside': False,
        'time': 120 #Minutes
    }
}

if __name__ == '__main__':
    state = 'NO QUERY'
    data = None
    while state != 'END':
        on_enter_state(state, data)
        text = input("> ")
        state, data = on_input_state(state, text, data)
    on_exit_query(data)

