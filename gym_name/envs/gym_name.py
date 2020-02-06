import gym
from gym import error, spaces, utils
from gym.utils import seeding

class NameEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
        # initialize envirnoment
        pass
    def step(self, action):
        # dynamical step in time returns reward and observation
        pass
    def reset(self):
        # resets state space
        pass
    def render(self, mode='human'):
        # display some usefulll info
        pass
    def close(self):
        # close simulation
        pass