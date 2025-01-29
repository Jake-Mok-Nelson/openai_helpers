import argparse

from agent_creator import create_swarm_agent
from generate_prompt import generate_prompt


def main():
    parser = argparse.ArgumentParser(description="OpenAI Swarm Agent Manager")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create a new Swarm Agent
    parser_swarm = subparsers.add_parser('create-swarm-agent', help='Create a new Swarm Agent')
    parser_swarm.add_argument('goal', type=str, help='The goal of the agent')
    parser_swarm.add_argument('--output', type=str, choices=['json', 'python'], default='python', help='Output format')
    parser_swarm.add_argument('--model', type=str, default='o1-mini', help='Model to use for prompt generation')
    parser_swarm.set_defaults(func=lambda args: create_swarm_agent(args.goal, args.model, args.output))

    # Improve a prompt
    parser_prompt = subparsers.add_parser('create-prompt', help='Create or improve a prompt')
    group = parser_prompt.add_mutually_exclusive_group(required=True)
    group.add_argument('--task', type=str, help='The task or prompt to improve')
    group.add_argument('--task-file', type=argparse.FileType('r'), help='File containing the task or prompt')
    parser_prompt.add_argument('--model', type=str, default='o1-mini', help='Model to use for prompt generation')
    parser_prompt.set_defaults(func=lambda args: generate_prompt(args.task or args.task_file.read(), args.model))

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
