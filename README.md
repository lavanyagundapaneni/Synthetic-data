# Synthetic Academic Pathway Data Generation using Ollama
This repository contains a script to generate synthetic academic pathway data using the Ollama LLM with the LLaMA2 7B model. The generated data is designed to mimic academic records and is useful for various educational data analysis tasks.

Overview
The script generates synthetic academic pathway data and outputs it in a structured format (CSV). The process involves:

Initializing the LLM:
Setting up the Ollama LLM with the LLaMA2 7B model. from langchain_community.llms import Ollama

Generating Synthetic Data:
Using a predefined prompt template to generate synthetic entries.

Parsing Generated Entries:
Extracting and structuring the relevant information from the generated entries.

Creating a DataFrame:
Converting the structured data into a pandas DataFrame.

Saving the Data:
Exporting the DataFrame to a CSV file.
