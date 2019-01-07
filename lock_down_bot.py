import re
import random

def on_enter_state(state, data):
    return state_dict.get(state, none_state)(data)

def on_input_state(state, text, data):
    return input_state_dict.get(state, none_input_state)(text, data)

def no_query_on_enter_state(data):
    print("How can I help?")

def location_on_enter_state(data):
    print("Where are you?")

def tutor_on_enter_state(data):
    print("Would you like a specific tutor?")

def rescue_on_enter_state(data):
    print(f"{data['tutor']} is on the way")

def get_tutor_on_enter_state(data):
    print('What tutor would you like?')

def none_state(data):
    raise Exception("State is not valid")

def no_query_on_input(text, data):
    match = re.search('(I am|I\'m) locked out( (in|at) (?P<location>.*))?', text)
    if match:
        location = match.group('location')
        if location:
            return 'TUTOR', location
        else:
            return 'LOCKED OUT', None
    else:
        return 'END', None

def location_on_input(text, data):
    location = data
    return 'TUTOR', location

def tutor_on_input(text, data):
    if text.lower() == 'yes':
        return 'GET_TUTOR', None
    else:
        return 'RESCUE', {'tutor':random.choice(tutors)}

def rescue_on_input(text, data):
    return 'END', None

def get_tutor_on_input(text, data):
    tutor = text
    return 'RESCUE', {'tutor':tutor}

def none_input_state(data):
    raise Exception("Input State is not valid")

def on_exit_query():
    print("Thank you for your time.")


state_dict = {
    'NO QUERY': no_query_on_enter_state,
    'LOCKED OUT': location_on_enter_state,
    'TUTOR': tutor_on_enter_state,
    'RESCUE': rescue_on_enter_state,
    'GET_TUTOR': get_tutor_on_enter_state
}

input_state_dict = {
    'NO QUERY': no_query_on_input,
    'LOCKED OUT': location_on_input,
    'TUTOR': tutor_on_input,
    'RESCUE': rescue_on_input,
    'GET_TUTOR': get_tutor_on_input
}

tutors = ['a','b','c']

if __name__ == '__main__':
    state = 'NO QUERY'
    data = None
    while state != 'END':
        on_enter_state(state, data)
        text = input("> ")
        state, data = on_input_state(state, text, data)
    on_exit_query()

