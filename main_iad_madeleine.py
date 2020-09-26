import aux_functions as af
import numpy as np

# MAIN

# environnement parameters
R = [0, 0, 1, 10]
x = 0.25
y = 0.25

T = np.zeros((4, 3, 4))
T[0][0] = [0, 0, 0, 0]
T[0][1] = [0, 1, 0, 0]
T[0][2] = [0, 0, 1, 0]

T[1][0] = [0, 1-x, 0, x]
T[1][1] = [0, 0, 0, 0]
T[1][2] = [0, 0, 0, 0]

T[2][0] = [1-y, 0, 0, y]
T[2][1] = [0, 0, 0, 0]
T[2][2] = [0, 0, 0, 0]

T[3][0] = [1, 0, 0, 0]
T[3][1] = [0, 0, 0, 0]
T[3][2] = [0, 0, 0, 0]

# iteration value algorithm parameters
gamma = 0.9
eps = 0.00001


# compute the possible action for each state
possible_Pi = af.find_possible_Pi(T)

# iteration value algorithm to find the optimal policy
# init
n_state = len(T)
curr_V = [0]*n_state
next_V = [0]*n_state
i = 0
diff = eps + 1
# compute V*
while diff >= eps:
    next_V = af.update_V(curr_V, gamma, T, R, possible_Pi)
    diff = af.RMS_error(curr_V, next_V)
    curr_V = next_V.copy()
    i = i+1
# find the optimal policy
optimal_Pi = af.optimal_policy(curr_V, T, possible_Pi)
