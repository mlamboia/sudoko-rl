from gymnasium.envs.registration import register

register(
    id="sudoko-rl-v0",
    entry_point="envs:MainEnv",
    max_episode_steps=300,
)
