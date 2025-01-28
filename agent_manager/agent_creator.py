import json
from openai import OpenAI
client = OpenAI()

   
def save_agent_python_to_file(agent_name, code_template):
   with open(f"{agent_name}.py", "w") as f:
      f.write(code_template)
   print(f"Agent code saved to {agent_name}.py")

def save_agent_json_to_file(agent_name, json_response):
   with open(f"{agent_name}.json", "w") as f:
      f.write(json.dumps(json_response, indent=3))
   print(f"Agent JSON saved to {agent_name}.json")


# Returns the new agent name and the Python code template
def create_python_agent_code(json_response):
   
   agent_name = json_response["name"]
   agent_model = json_response["model"]
   agent_instructions = json_response["instructions"]
   agent_functions = json_response.get("functions", [])
   agent_tool_choice = json_response.get("tool_choice", [])
   agent_parallel_tool_calls = json_response.get("parallel_tool_calls", False)
   code_template = f"""
from swarm import Agent, Swarm
client = Swarm()

my_agent = Agent(
   name="{agent_name}",
   instructions="{agent_instructions}",
   model="{agent_model}",
   functions={agent_functions},
   tool_choice={agent_tool_choice},
   parallel_tool_calls={agent_parallel_tool_calls}
)

"""
   return agent_name, code_template

# Create a new Swarm agent based on the user's goal
# and output the agent details in the specified format
def create_swarm_agent(goal: str, output_method: str):
   print(f"Creating a new OpenAI Swarm agent with the goal: {goal}")
   conversation = [
      {
         "role": "system",
         "content": [
         {
            "type": "text",
            "text": "Create a new OpenAI Swarm agent using prompt engineering principles. Interact with the user to gather the agent's goals and requirements, then generate detailed instructions for the agent. The output must specify all necessary components to create a functional agent.\n\n# Steps\n\n1. **Gather Requirements:**\n   - Engage with the user to understand the specific goal or task for the agent.\n   - Determine any unique requirements or constraints the agent must comply with.\n\n2. **Define Agent Details:**\n   - Choose an appropriate name for the agent that reflects its function or purpose.\n   - Select the most suitable model for the agent based on its task complexity and reasoning needs.\n\n3. **Create Agent Instructions:**\n   - Draft detailed and clear instructions for the agent to follow.\n   - Ensure the instructions simulate reasoning and decision-making processes where applicable.\n\n4. **Identify Functions and Tools:**\n   - List any specific functions the agent must have access to for performing its tasks.\n   - Specify any additional tools the agent needs to utilize.\n\n5. **Determine Parallel Tool Calls:**\n   - Decide if parallel tool calls are necessary for the agent's operations based on the task requirements.\n\n# Output Format\n\nThe output should be formatted as a JSON object with the following keys:\n\n- `name`: A string representing the agent's name.\n- `model`: A string representing the selected model. Options include `gpt-4o` (default), `gpt-4o-mini`, `o1`, or `o1-mini`.\n- `instructions`: A string or array of strings, detailing the instructions for the agent.\n- `functions`: An optional array of strings identifying the functions available to the agent.\n- `tool_choice`: An optional array of strings naming tools the agent will require.\n- `parallel_tool_calls`: An optional boolean indicating if parallel tool calls are supported.\n\n# Examples\n\n**Example Input:**\n\n- User Goal: \"Create a customer support agent that handles inquiries about product features and pricing efficiently.\"\n\n**Example Output:**\n\n```json\n{\n  \"name\": \"ProductSupportAgent\",\n  \"model\": \"gpt-4o\",\n  \"instructions\": \"The agent should respond to user inquiries regarding product features and pricing with accurate information and a friendly tone. Simulate reasoning by suggesting additional related products"
         }
         ]
      },
      {
         "role": "user",
         "content": goal
      }
   ]
   response = client.chat.completions.create(
      model="gpt-4o",
      messages=conversation,
      response_format={
         "type": "json_schema",
         "json_schema": {
               "name": "agent_schema",
               "schema": {
                  "type": "object",
                  "required": [
                     "name",
                     "model",
                     "instructions",
                     "functions",
                     "tool_choice",
                     "parallel_tool_calls"
                  ],
                  "properties": {
                     "name": {
                           "type": "string",
                           "description": "The agent's name."
                     },
                     "model": {
                           "enum": [
                              "gpt-4o",
                              "gpt-4o-mini",
                              "o1",
                              "o1-mini"
                           ],
                           "type": "string",
                           "description": "The agent's model."
                     },
                     "functions": {
                           "type": "array",
                           "items": {
                              "type": "string"
                           },
                           "description": "A list of functions that should be accessible to the agent to perform its tasks."
                     },
                     "tool_choice": {
                           "type": "array",
                           "items": {
                              "type": "string"
                           },
                           "description": "Any tools that the agent will need access to."
                     },
                     "instructions": {
                           "type": "string",
                           "description": "A set of instructions for the agent."
                     },
                     "parallel_tool_calls": {
                           "type": "boolean",
                           "description": "Whether parallel tool calls will be required."
                     }
                  },
                  "additionalProperties": False
               },
               "strict": True
         }
      },
      temperature=1,
      max_completion_tokens=2048,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
   )
   
   
   
   json_response = json.loads(response.choices[0].message.content)
   if type(json_response) == str:
      try:
         json_response = json.loads(json_response)
      except:
         print(f"Error: {json_response}")
         exit(1)

   # Create the the template to output to file or print to stdout
   agent_name, python_code = create_python_agent_code(json_response)
   
   if output_method == "json":
      save_agent_json_to_file(agent_name, json_response)
   elif output_method == "python":
      save_agent_python_to_file(agent_name, python_code)
   else:
      print(python_code)
