from core.task_analyzer import analyze_task
from core.planner import create_plan


class Agent:
    """
    Central controller of the AI Agent Framework.
    """

    def run(self, user_input: str) -> str:
        # Step 1: Analyze the task
        analysis = analyze_task(user_input)

        # Step 2: Create a plan based on task type
        plan = create_plan(analysis["task_type"], user_input)

        # Step 3: Build structured response
        response = (
            "AI Agent Execution\n"
            "------------------\n"
            f"Task Type : {analysis['task_type']}\n\n"
            "Execution Plan:\n"
        )

        for index, step in enumerate(plan, start=1):
            response += f"{index}. {step}\n"

        return response
