from core.agent import Agent


def main():
    """
    Entry point for the AI Agent Framework.
    Initializes the agent and handles user interaction.
    """

    agent = Agent()

    print("AI Agent Framework")
    print("------------------")

    user_input = input("Enter your task: ")
    result = agent.run(user_input)

    print("\nAgent Output:")
    print(result)


if __name__ == "__main__":
    main()
