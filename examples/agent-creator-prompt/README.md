
```bash
python3 ./main.py create-prompt --task-file ./input.txt --model o1-mini
```

Results in the following output:

```bash
Create an OpenAI Swarm agent capable of performing a variety of tasks using prompt-engineering practices.

The agent must adhere to the provided JSON schema, ensuring all required fields are included and correctly formatted.

# Steps

1. Define the agent's name.
2. Select the appropriate model from the available options ("gpt-4o", "gpt-4o-mini", "o1", "o1-mini").
3. Develop a set of instructions that guide the agent's behavior.
4. List the functions the agent can perform.
5. Specify the tools the agent will have access to.
6. Determine whether the agent requires parallel tool calls.

# Output Format

The output should be a JSON object conforming to the provided `agent_schema`. Ensure all required fields are present and follow the specified types and descriptions. Do not include code blocks.

# Examples

**Example 1**

*Input:*

Create an agent named "TaskMaster" using the "gpt-4o" model. Instructions: "Manage and execute tasks efficiently." Functions: "create_task", "delete_task". Tools: "task_manager_api". Parallel Tool Calls: true.

*Output:*

{
  "name": "TaskMaster",
  "model": "gpt-4o",
  "instructions": "Manage and execute tasks efficiently.",
  "functions": ["create_task", "delete_task"],
  "tool_choice": ["task_manager_api"],
  "parallel_tool_calls": true
}

**Example 2**

*Input:*

Create an agent named "[AgentName]" using the "[Model]" model. Instructions: "[Instructions]". Functions: "[Function1]", "[Function2]". Tools: "[Tool1]". Parallel Tool Calls: [true/false].

*Output:*

{
  "name": "[AgentName]",
  "model": "[Model]",
  "instructions": "[Instructions]",
  "functions": ["[Function1]", "[Function2]"],
  "tool_choice": ["[Tool1]"],
  "parallel_tool_calls": [true/false]
}

# Notes

- Ensure that the `model` field strictly uses one of the specified options.
- All fields are required and must match the types defined in the JSON schema.
- Use clear and concise language in the `instructions` to guide the agent effectively.
- When providing placeholders in examples, ensure they are descriptive enough to illustrate the required format.
```