def generate_pipeline(language: str):

    if language.lower() == "python":

        return """
name: Python CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: pytest
"""

    elif language.lower() == "nodejs":

        return """
name: Node.js CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Dependencies
        run: npm install

      - name: Run Tests
        run: npm test
"""

    return "Unsupported language"