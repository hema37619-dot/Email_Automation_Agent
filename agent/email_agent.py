from agent.planner import create_plan
from agent.executor import (
    execute_plan
)
class EmailAgent:
    def run(
        self,
        receiver,
        goal
    ):

        print("\nAgent Started")

        plan = create_plan(goal)

        for step in plan:

            print(
                f"✓ {step}"
            )

        result = execute_plan(
            receiver,
            goal
        )

        return result