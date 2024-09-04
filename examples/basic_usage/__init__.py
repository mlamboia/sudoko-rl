import gymnasium as gym
from gymnasium.envs.registration import register

register(
    id="sudoko-rl-v0",
    entry_point="envs:MainEnv",
    max_episode_steps=300,
)

def main():
    env = gym.make('sudoko-rl-v0')

    observation, info = env.reset()

    for _ in range(1000):
        print(env.render())
        action = env.action_space.sample()
        observation, reward, done, truncated, info = env.step(action)

        if done or truncated:
            observation, info = env.reset()

    env.close()

if __name__ == "__main__":
    main()
