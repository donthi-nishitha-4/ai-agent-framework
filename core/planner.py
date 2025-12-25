from typing import List


def create_plan(task_type: str, user_input: str) -> List[str]:
    """
    Create a step-by-step execution plan based on task type.

    Parameters:
        task_type (str): Type of task identified by the task analyzer.
        user_input (str): Original user input.

    Returns:
        List[str]: Ordered list of steps to execute the task.
    """

    if task_type == "planning":
        return [
            "Understand the goal and requirements",
            "Identify relevant topics or actions",
            "Organize steps in a logical sequence",
            "Prepare a structured final response" ]

    elif task_type == "tool":
        return [
            "Identify the appropriate tool",
            "Execute the required operation",
            "Validate the result",
            "Present the output" ]

    else:
        return [
            "Understand the user query",
            "Generate a clear and concise response"]
