from gym.envs.registration import register

register(
    id='name-v0',
    entry_point='gym_name.envs:NameEnv',
)
register(
    id='name-extrahard-v0',
    entry_point='gym_foo.envs:NameExtraHardEnv',
)