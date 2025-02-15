import openai
import sys

def generate_commit_message(changes):
    openai.api_key = 'your-api-key-here'  # Replace with your OpenAI API key

    prompt = f"Generate a commit message for the following changes:\n{changes}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    changes = sys.argv[1]
    print(generate_commit_message(changes)) 