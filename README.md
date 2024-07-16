# Synthetic Academic Pathway Data Generation using Ollama
This repository contains a script to generate synthetic academic pathway data using the Ollama LLM with the LLaMA2 7B model. The generated data is designed to mimic academic records and is useful for various educational data analysis tasks.

The script generates synthetic academic pathway data and outputs it in a structured format (CSV). The process involves:

## 1.Initializing the LLM:
Setting up the Ollama LLM with the LLaMA2 7B model. from langchain_community.llms import Ollama
inline code 
` import pandas as pd
import re
from langchain_community.llms import Ollama

# Initialize the Ollama LLM with the desired model
llm = Ollama(model="llama2:7b")`

## 2.Generating Synthetic Data:
Using a predefined prompt template to generate synthetic entries.

## 3.Parsing Generated Entries:
Extracting and structuring the relevant information from the generated entries.

## 4.Creating a DataFrame:
Converting the structured data into a pandas DataFrame.

## 5.Saving the Data:
Exporting the DataFrame to a CSV file.
