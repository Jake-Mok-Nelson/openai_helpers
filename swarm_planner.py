
def gather_requirements():
    prompt = """
Plan an OpenAI Swarm by gathering requirements from the user, determining the optimal number of agents to perform tasks, and deciding whether memory should be utilized. Emphasize assigning many granular tasks to multiple agents.

# Steps

1. **Gather Requirements:** Ask the user for detailed requirements to understand the scope and objectives of the swarm.
2. **Analyze Tasks:** Break down the requirements into granular tasks to assess the complexity and distribution.
3. **Determine Number of Agents:** Decide how many agents are needed based on the number and complexity of tasks.
4. **Decide on Memory Usage:** Assess whether memory should be incorporated based on task interdependencies and the need for context retention.
5. **Develop the Plan:** Outline the distribution of tasks among agents and specify memory usage where applicable.

# Output Format

Provide the output in JSON format with the following structure:

```json
{
  "requirements": "User-provided requirements",
  "number_of_agents": "Determined number of agents",
  "memory_usage": true or false,
  "task_distribution": "Detailed description of task assignments to each agent"
}
```

# Examples

**Input:**

- **Requirements:** Develop a customer support system that can handle inquiries, manage tickets, and provide follow-up reminders.

**Output:**

```json
{
  "requirements": "Develop a customer support system that can handle inquiries, manage tickets, and provide follow-up reminders.",
  "number_of_agents": 3,
  "memory_usage": true,
  "task_distribution": "Agent 1 handles customer inquiries, Agent 2 manages ticket creation and tracking, and Agent 3 provides follow-up reminders based on ticket status."
}
```

# Notes

- Ensure that tasks are as granular as possible to allow each agent to specialize effectively.
- Consider scalability when determining the number of agents.
- Memory usage should be decided based on whether agents need to retain context between tasks.
""".strip()

