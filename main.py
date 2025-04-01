import openai
import os

def generate_software(project_name, description, model="gpt-4o-mini"):
    """Generates software code based on a project description using GPT-4o-mini or GPT-4o."""
    api_key = "OPENAI_KEY_HERE"  # Ensure your API key is set as an environment variable
    if not api_key:
        raise ValueError("Missing OpenAI API key. Set it as an environment variable: OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)
    prompt = f"""
    You are an AI software generator. Generate a simple {project_name} project in python based on the following description:
    {description}
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful software generator AI."},
                  {"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    description = input("Enter project description: ")
    print("\nGenerating software...\n")
    software_code = generate_software(project_name, description)
    with open(f"{project_name}.py", "w") as file:
        file.write(software_code)
    print(f"Software generated and saved as {project_name}.py")
