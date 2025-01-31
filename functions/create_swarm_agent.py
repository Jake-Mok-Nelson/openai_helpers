import json
import logging
from openai import OpenAI


from functions.generate_prompt import generate_prompt
from helpers.is_pre_o1 import is_pre_o1
client = OpenAI()


# Returns the new agent name and the Python code template
def create_python_agent_code(json_response):
   
   agent_name = json_response["name"]
   agent_model = json_response["model"]
   agent_instructions = json_response["instructions"]
   agent_functions = json_response.get("functions", [])
   agent_tool_choice = json_response.get("tool_choice", [])
   agent_parallel_tool_calls = json_response.get("parallel_tool_calls", False)
   code_template = f"""my_agent = Agent(
   name="{agent_name}",
   instructions="{agent_instructions}",
   model="{agent_model}",
   functions={agent_functions},
   tool_choice={agent_tool_choice},
   parallel_tool_calls={agent_parallel_tool_calls}
)

"""
   return code_template

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

# Create a new Swarm agent based on the user's goal
# and output the agent details in the specified format
def create_swarm_agent(goal: str, model: str = "o1-mini"):
   try:
      conversation = [
         {
            "role": "user",
            "content": [
            {
               "type": "text",
               "text": """Create an OpenAI Swarm agent capable of performing a variety of tasks using prompt-engineering practices.

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
            """
            }
            ]
         },
         {
            "role": "user",
            "content": goal
         }
      ]
      response = client.chat.completions.create(
         model=model,
         messages=conversation,
         # set a field for the response format if the model is not pre-o1
         # response_format=response_format if is_pre_o1(model) else None,
         temperature=1,
         max_completion_tokens=2048 if is_pre_o1(model) else None,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
      )
      
      prev_response = response.choices[0].message.content
      
      # Validate the response format if the model is not pre-o1
      # pre-o1 had format_response field
      if not is_pre_o1(model):
         response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
               {
                     "role": "user", 
                     "content": f"""
         Given the following data, format it with the given response format: {prev_response}
         """
               }
            ],
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
         )

         # print(response.choices[0].message.parsed)
      
      
      json_response = json.loads(response.choices[0].message.content)

      if type(json_response) == str:
         try:
            json_response = json.loads(json_response)
         except:
            print(f"Error: {json_response}")
            exit(1)
            
      agent_prompt_for_improvement = """
      You are agent """ + json_response["name"] + """.
      
      Instructions: """ + json_response["instructions"] + """.
      
      The can use the following functions: """ + ", ".join(json_response["functions"]) + """
      
      And the following tools: """ + ", ".join(json_response["tool_choice"]) + """
      """
      
      improved_prompt = generate_prompt(agent_prompt_for_improvement, model)
      if not improved_prompt:
         logging.error("Failed to generate an improved prompt.")
         exit(1)
      
      # merge the json response with the improved prompt
      json_response['instructions'] = improved_prompt
      
      return create_python_agent_code(json_response)
   except Exception as e:
      print(f"An error occurred: {e}")
      exit(1)
