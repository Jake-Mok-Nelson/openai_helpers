import argparse

from agent_creator import create_swarm_agent
from generate_prompt import generate_prompt

def main():
    parser = argparse.ArgumentParser(description="OpenAI Swarm Agent Manager")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    parser_swarm = subparsers.add_parser('create-swarm-agent', help='Create a new Swarm Agent')
    parser_swarm.add_argument('goal', type=str, help='The goal of the agent')
    parser_swarm.add_argument('--output', type=str, choices=['json', 'python', 'print'], default='print', help='Output format')
    
    parser_swarm.set_defaults(func=lambda args: create_swarm_agent(args.goal, args.output))

    parser_prompt = subparsers.add_parser('improve-prompt', help='Improve a prompt')
    parser_prompt.add_argument('task_or_prompt', type=str, help='The task or prompt to improve')
    parser_prompt.set_defaults(func=lambda args: print(generate_prompt(args.task_or_prompt)))

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
