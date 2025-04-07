# Q-learning

This project demonstrates the implementation of Q-learning, a reinforcement learning algorithm, in a custom game environment. The project includes various modules for game logic, graphics, Q-learning
the game involves a 5x5 matrix with a predefined position for the checkpoint and the player is randomly placed in the matrix. 

We use the following algorithm to effectively build the corresponding Q-table which will contain state,action information to then later allow the player to locate the checkpoint efficiently.
```Qtable[state][action] = Qtable[state][action] + learning_rate * (reward + gamma * np.argmax(Qtable[new_state] - Qtable[state]))```
