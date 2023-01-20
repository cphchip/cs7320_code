'''
VacWorld.py
'''
Name = 'Christopher Henderson'
ID = '48996654'


def getAction(state):
    '''state: current state
       return  the action based on state
    '''
    if state[1][1] == 0 and 'R' in state:
        return 'MOVELEFT'

    if state[1][0] == 1 and 'L' in state:
        return 'SUCK'

    if state[1][1] == 1 and 'R' in state:
        return 'SUCK'

    if state[1][0] == 0 and 'L' in state:
        return 'MOVERIGHT'


def updateState(state, action):
    ''' state : current state
        action : current action
        return : next state
    '''
    if action == 'SUCK' and 'R' in state:
        return ['R',[state[1][0],0]]
    
    if action == 'SUCK' and 'L' in state:
        return ['L',[0,state[1][1]]]

    if action == 'MOVERIGHT':
        return ['R',state[1]]

    if action == 'MOVELEFT':
        return ['L',state[1]]


def bool_all_rooms_clean(state):
    '''returns True or False if all room are clean or not'''
    if 1 in state[1]:
        return False
    else:
        return True 


def run_vacuum(start_state):
    state = start_state
    loop_count = 0  # counter to stop program when it goes wrong

    # run the simulation until all rooms clean
    while not bool_all_rooms_clean(state):
        action = getAction(state)
        state = updateState(state, action)
        # show state and stop if too many loops
        print(f"cycle:{loop_count}\taction={action}\t\tstate={state}")
        loop_count += 1

        if loop_count > 20:
            print(
                "Uh oh ! Code stuck in a state ... program terminated")
            return

    print("All rooms clean!")
    return


def main():
    # when you run this code without implementing above functions
    # the program will stop after 20 cycles
    # Part 1: Start in room R
    start_state = ['R', [1, 1]]
    print(f"\nPart1. Start in room R\nStart State: {start_state}")
    run_vacuum(start_state)

    # Part 2: Start in room L
    start_state = ['L', [1, 1]]
    print(f"\nPart2. Start in room L\nStart State: {start_state}")
    run_vacuum(start_state)

if __name__ == '__main__':
    main()
