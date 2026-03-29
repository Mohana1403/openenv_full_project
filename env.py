
from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    inbox: List[str]
    processed: List[str]

class Action(BaseModel):
    action_type: str
    email_id: int

class Reward(BaseModel):
    value: float

class EmailEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.inbox = ["urgent: server down", "spam offer", "meeting at 5"]
        self.processed = []
        self.done = False
        return self.state()

    def state(self):
        return Observation(inbox=self.inbox, processed=self.processed)

    def step(self, action: Action):
        reward = 0.0

        if action.email_id >= len(self.inbox):
            return self.state(), Reward(value=-1.0), self.done, {}

        email = self.inbox[action.email_id]

        if action.action_type == "delete":
            reward += 1.0 if "spam" in email else -0.5
        elif action.action_type == "reply":
            reward += 1.0 if "urgent" in email else -0.2
        elif action.action_type == "read":
            reward += 0.1

        self.processed.append(email)
        self.inbox.pop(action.email_id)

        if len(self.inbox) == 0:
            self.done = True

        return self.state(), Reward(value=reward), self.done, {}
