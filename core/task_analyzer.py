from typing import Dict


def analyze_task(user_input: str) -> Dict[str, str]:
    """
    Analyze the user input and classify the task.

    Parameters:
        user_input (str): Input provided by the user.

    Returns:
        dict: A dictionary containing task type and original query.
    """

    text = user_input.lower().strip()

    # Identify task type
    if any(keyword in text for keyword in ["plan", "schedule", "roadmap"]):
        task_type = "planning"

    elif any(keyword in text for keyword in ["calculate", "add", "subtract", "multiply", "divide"]):
        task_type = "tool"

    else:
        task_type = "general"

    return {
        "task_type": task_type,
        "query": user_input
    }
