# Axelrod's Simulation Environment

A simple and interactive simulation tool inspired by Axelrod's classic tournaments, allowing you to easily create, test, and analyze your own game-theoretic strategies.

## Features

- **Customize Strategies:** Write and test your own strategy against genaric strategies.
- **Quick Simulation:** Instantly run tournaments to see how your strategy performs.
- **Easy-to-use:** Designed for simplicity and accessibility.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/rexmhall09/Axelrods-Simulation-Environment.git
cd Axelrods-Simulation-Environment
```

Run a tournament simulation:

```bash
python main.py
```

## Adding Your Strategy

Create your own strategy by adding a Python file to the `strategies` directory:

```python
def strategy(history):
    # Your strategy logic here
    return "C"  # "C" for cooperate or "D" for defect
```
