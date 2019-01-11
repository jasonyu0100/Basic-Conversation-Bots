import re
import random

def on_enter_state(state, data):
    return state_dict.get(state, none_state)(data)

def on_input_state(state, text, data):
    return input_state_dict.get(state, none_input_state)(text, data)

def no_query_on_enter_state(data):
    print(f"I'd like to make a booking at {data['place']} at {data['time']}, with {data['group']}?")

def negative_confirmation_on_enter_state(data):
    print("When are you next available?")

def positive_confirmation_on_enter_state(data):
    print("That's great! We'll see you there!")

def miscellaneous_on_enter_state(data):
    print("We'll contact you later with that information!")

def none_state(data):
    raise Exception("State is not valid")

def no_query_on_input(text, data):
    confirmation_check = re.search('(?P<confirmation>.+) you can make that booking|reservation|time.', text)
    if confirmation_check:
        confirmation = confirmation_check.group('confirmation')
        if confirmation == 'Yes':
            return 'POSITIVE_CONFIRMATION', None
        else:
            return 'NEGATIVE_CONFIRMATION', None
    else:
        return 'MISCELLANEOUS', {'context':text}

def negative_confirmation_on_input(text, data):
    time_check = re.search('We are available at (?P<time>.+)', text)
    if time_check:
        time = time_check.group('confirmation')
        if time:
            return 'END', {'time':time,'confirmation':False}
        else:
            return 'END', {'confirmation':False}
    else:
        return 'END', {'confirmation':False}

def positive_confirmation_on_input(text, data):
    return 'END', {'confirmation':True}

def miscellaneous_on_input(text, data):
    return 'END', {'confirmation':False,'context':data['context']}

def none_input_state(data):
    raise Exception("Input State is not valid")

def on_exit_query():
    print("Thank you for your time.")


state_dict = {
    'NO_QUERY': no_query_on_enter_state,
    'POSITIVE_CONFIRMATION':positive_confirmation_on_enter_state,
    'NEGATIVE_CONFIRMATION':negative_confirmation_on_enter_state,
    'MISCELLANEOUS':miscellaneous_on_enter_state,
}

input_state_dict = {
    'NO_QUERY': no_query_on_input,
    'POSITIVE_CONFIRMATION':positive_confirmation_on_input,
    'NEGATIVE_CONFIRMATION':negative_confirmation_on_input,
    'MISCELLANEOUS':miscellaneous_on_input,
}

tutors = ['a','b','c']

if __name__ == '__main__':
    state = 'NO_QUERY'
    data = {'place':'Mcdonalds','time':'12:45','group':'5 people'}
    while state != 'END':
        on_enter_state(state, data)
        text = input("> ")
        state, data = on_input_state(state, text, data)
    on_exit_query()

