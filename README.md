# openai_helpers

Misc tools for OpenAI

## Description

This repository contains various tools and utilities for working with OpenAI's API. The primary functionality includes creating a new Swarm agent with a specified goal and output format, as well as generating prompts using OpenAI's API.

**Warning:** Each function in this application uses the OpenAI Apis and may make multiple calls to an o1-mini model by default.
You can override the model with the `--model` flag for most commands.


## Installation

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

### Creating a Swarm Agent

To create a new Swarm agent, use the following command:

```bash
python cli/main.py create-swarm-agent "Your goal here" --output [json|python|print]
```

Replace `"Your goal here"` with the desired goal for the agent and choose the output format (`json`, `python`, or `print`).

### Improving a Prompt

To improve a prompt using OpenAI's API, use the following command:

```bash
python cli/main.py improve-prompt "Your task or prompt here"
```

Replace `"Your task or prompt here"` with the task or prompt you want to improve.

## Examples

### Creating a Swarm Agent

Example command to create a Swarm agent with a goal and output the Python code:

```bash
python cli/main.py create-swarm-agent "Create a customer support agent" --output python
```

### Improving a Prompt

Example command to improve a prompt:

```bash
python cli/main.py improve-prompt "Improve the following prompt: 'Translate the following English text to French.'"
```

### Generating Prompts

Example usage of the `generate_prompt` function in `cli/generate_prompt.py`:

```python
from cli.generate_prompt import generate_prompt

task_or_prompt = "Improve the following prompt: 'Translate the following English text to French.'"
generated_prompt = generate_prompt(task_or_prompt)
print(generated_prompt)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

