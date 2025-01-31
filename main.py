from agents.agent_cli import agent_cli
from helpers.run_loop import run_loop


if __name__ == "__main__":
    # Run the demo loop
    output = ""
    msg = """👋 Hello and welcome to the SwarmAgentCLI! 🚀 It's great to have you here.
    I'm ready to help you with:
    - Creating agents
    - Designing swarms
    - Generating or improving prompts

    How would you like to begin? 🤖
    
    Btw, you can always type 'exit' to leave the CLI. 🚪
    """
    run_loop(agent_cli, welcomeMessage=msg, debug=True)
