import pandas as pd
import re
from langchain_community.llms import Ollama

# Initialize the Ollama LLM with the desired model
llm = Ollama(model="llama2:7b")

def generate_synthetic_data(prompt, n_samples=20):
    synthetic_data = []
    for i in range(n_samples):
        try:
            response = llm.invoke(prompt)
            # Check if response is a dict and contains 'text'
            if isinstance(response, dict) and 'text' in response:
                text = response['text'].strip()
                if "Current Grade:" in text and "Future Course:" in text:
                    synthetic_data.append(text)
                else:
                    print(f"Unexpected response format at sample {i + 1}: {text}")
            else:
                print(f"Unexpected response format at sample {i + 1}: {response}")
        except Exception as e:
            print(f"Error at sample {i + 1}: {e}")
    return synthetic_data

# Define the prompt template based on the existing data structure
prompt_template = """Generate a synthetic academic pathway entry. Ensure each entry is unique:
Current Grade: (choose different grades from 9th,10th,11th)
Future Course: (choose various courses and universities)
Duration: (vary between 2 to 4 years)
Year: (choose different years between 2025 to 2030)
Category: K12
School: (choose different schools)
Degree: (choose different degrees like Bachelors, Masters)
Subject: (choose different subjects like Economics, Computer Science, etc.)
University: (choose different universities)
Country: (choose different countries)
Financial Status: (choose budget in numericals)
Stream: (choose different streams like mpc,bipc,cec,hec etc...)
Curriculum: (choose different curriculum like cbse,ssc,etc.... )
Please provide the response in the following format:
Current Grade: ...
Future Course: ...
Duration: ...
Year: ...
Category: ...
School: ...
Degree: ...
Subject: ...
University: ...
Country: ...
Financial Status: ....
Stream: ....
Curriculum: ....
"""

# Generate 100 synthetic entries using the LLaMA model via Ollama
print("Generating synthetic entries...")
synthetic_entries = generate_synthetic_data(prompt_template, n_samples=20)
print("Generation complete.")

# Function to parse generated entries
def parse_entry(entry):
    fields = re.split(r'\n', entry)
    values = [field.split(": ")[1] for field in fields if ": " in field]
    return values

# Process the generated entries to match the data structure
synthetic_data = [parse_entry(entry) for entry in synthetic_entries if parse_entry(entry)]

# Define columns
columns = ["Current Grade", "Future Course", "Duration", "Year", "Category", "Degree", "Subject", "University", "Country"]

# Convert to DataFrame
synthetic_df = pd.DataFrame(synthetic_data, columns=columns)

# Insert S.No column
synthetic_df.insert(0, "S.No", range(1, len(synthetic_df) + 1))

# Display the synthetic DataFrame
print(synthetic_df.head())

# Further processing or saving the DataFrame as needed
# For example, save to CSV
synthetic_df.to_csv('synthetic_data_tiny_llama.csv', index=False)
