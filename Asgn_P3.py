# You need to install gymnasium and pygame
# https://github.com/Farama-Foundation/Gymnasium
import gymnasium as gym
import numpy as np

class state():
    def __init__(self, pos, state_type):
        self.pos = pos
        self.state_type = state_type
        self.actions = [0, 0, 0, 0]
        self.value = 0
        self.reward = 0

def value_iteration(states, e, gamma, noise, world_type):
    iterations = 0
    while True:
        change = 0
        for x in range(len(states)):
            for y in range(len(states[0])):
                z = states[x][y]
                if z.state_type == 'G':
                    pass
                else:
                    temp = z.value
                    z.value = z.actions[get_val(states, z, gamma, noise, world_type)]
                    #print(f'{temp}, {z.value}')
                    change = max(change, abs(temp - z.value))
                iterations += 1
        if change < e:
            break
    # for x in range(len(states)):
    #     for y in range(len(states[0])):
    #         print(f'{states[x][y].value:.2f}', end=', ')
    #     print()
    return iterations

                        
def get_val(states, current_state, gamma, noise, world_type):
    x, y = current_state.pos
    if world_type:
        #left
        current_state.actions[0] = noise * (gamma * check_state(states, (x, y), 0)) + noise * (gamma * check_state(states, (x, y), 3)) + noise * (gamma * check_state(states, (x, y), 1))
        #down
        current_state.actions[1] = noise * (gamma * check_state(states, (x, y), 1)) + noise * (gamma * check_state(states, (x, y), 2)) + noise * (gamma * check_state(states, (x, y), 0))
        #right
        current_state.actions[2] = noise * (gamma * check_state(states, (x, y), 2)) + noise * (gamma * check_state(states, (x, y), 1)) + noise * (gamma * check_state(states, (x, y), 3))
        #up
        current_state.actions[3] = noise * (gamma * check_state(states, (x, y), 3)) + noise * (gamma * check_state(states, (x, y), 0)) + noise * (gamma * check_state(states, (x, y), 2))
    else:
        #left
        current_state.actions[0] = 1 * (gamma * check_state(states, (x, y), 0))
        #down
        current_state.actions[1] = 1 * (gamma * check_state(states, (x, y), 1))
        #right
        current_state.actions[2] = 1 * (gamma * check_state(states, (x, y), 2))
        #up
        current_state.actions[3] = 1 * (gamma * check_state(states, (x, y), 3))
    return np.argmax(current_state.actions)

def check_state(states, pos, action):
    x, y = pos
    if action == 0:
        if y == 0:
            return states[x][y].value
        else:
            return states[x][y-1].value
    elif action == 1:
        if x == len(states)-1:
            return states[x][y].value
        else:
            return states[x+1][y].value
    elif action == 2:
        if y == len(states)-1:
            return states[x][y].value
        else:
            return states[x][y+1].value
    elif action == 3:
        if x == 0:
            return states[x][y].value
        else:
            return states[x-1][y].value

# values to change for testing, change world type determines is_slippery
world_type = False
ncols = 4
nrows = 4
e = 0.001
noise = 1.0/3.0
# change this for different decay rate
gamma = 0.8

# You need this part
# S:Start, F:Frozen, H:Hole, G:Goal
map = ["SFFF", "FHFH", "FFFF", "HFFG"]
# is_slippery=True means stochastic and is_slippery=False means deterministic
env = gym.make('FrozenLake-v1', render_mode="human", desc=map, map_name="4x4", is_slippery=world_type)
env.reset()
env.render()

# make the policy
policy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
states = [[state for i in range(nrows)] for j in range(ncols)]

for i in range(nrows):
    for j in range(ncols):
        states[i][j] = state((i, j), map[i][j])
        if states[i][j].state_type == 'G':
            states[i][j].reward = 1
            states[i][j].value = 1
        else:
            states[i][j].reward = 0
            
for x in range(len(states)):
    for y in range(len(states[0])):
        print(states[x][y].value)
    print()
    
iterations = 0
iterations = value_iteration(states, e, gamma, noise, world_type)
for x in range(len(states)):
    for y in range(len(states[0])):
        policy[x*ncols+y] = np.argmax(states[x][y].actions)
        
print(policy)
print(f'Iterations: {iterations}')
for x in range(len(states)):
    for y in range(len(states[0])):
        print(f'{states[x][y].value:.5f}', end=', ')
    print()
    
# This part uses the found policy to interact with the environment.
# You don't need to change anything here.
s = 0
goal = ncols * nrows - 1
while s != goal:
    a = policy[s]
    s, r, t, f, p = env.step(a)
    if t == True and s != goal:
        env.reset()
        s = 0

print("end")

