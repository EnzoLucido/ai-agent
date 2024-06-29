# ai-agent

## Description
This project builds on top of Ollama to access real-time data. This allows it to answer questions about events after it's knowledge cutoff

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed [Python 3.12.0](https://www.python.org/downloads/release/python-3121/) or later is prefered. However [Python 3.8.0] or later should work as well.
- You have installed `pip`, the Python package installer. You can install it by following the instructions [here](https://pip.pypa.io/en/stable/installation/).

## Installation
# Clone the Repository
$ git clone https://github.com/EnzoLucido/ai-agent.git

# Install Ollama
Visit https://ollama.com/download and follow install instructions
$ ollama serve

In another terminal run 
$ ollama run llama3 

# Install Other Dependencies
$ pip install -r requirements.txt

## How to Use
Inside the folder, run
$ python main.py

