
import random
from env import EmailEnv, Action

env = EmailEnv()
obs = env.reset()

total_reward = 0

while True:
    if len(obs.inbox) == 0:
        break

    action = Action(
        action_type=random.choice(["read","delete","reply"]),
        email_id=0
    )

    obs, reward, done, _ = env.step(action)
    total_reward += reward.value

    if done:
        break

print("Baseline Reward:", total_reward)
