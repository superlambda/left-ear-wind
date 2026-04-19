from random import random

def move_cars(car_positions):
    return [x + 1 if random() > 0.3 else x for x in car_positions]

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {
        'time': state['time'] - 1,
        'car_positions': move_cars(state['car_positions'])
    }

def draw(state):
    print()
    print('\n'.join(output_car(x) for x in state['car_positions']))

def race(state):
    draw(state)
    if state['time'] > 0:
        race(run_step_of_race(state))

race({
    'time': 5,
    'car_positions': [1, 1, 1]
})