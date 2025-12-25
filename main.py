from core.agent import Agent


def main():
    """
    Entry point for the AI Agent Framework.
    """

    print("AI Agent Framework")
    print("------------------")

    agent = Agent()

    user_input = input("Enter your task: ")
    output = agent.run(user_input)

    print("\nAgent Output:")
    print(output)


if __name__ == "__main__":
    main()
