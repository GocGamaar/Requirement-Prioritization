# Requirement-Prioritization
Prioritization of Requirements of a Software Project using Evolutionary Algorithms

**Tech Stack**
- Python (Evolutionary Algorithms)
- Jupyter Notebook (Data handling & backend logic)
- NodeJS & Express (UI & Server)

## How to run
**If Docker is installed**:
Run `docker build -t req-prio .` (Installing numpy and pandas will take some time, gotta bear with it)

Then, when in repo directory, run `docker run --rm -p 8888:8888 -v $(pwd)/:/code --name instance req-prio`

Open and Execute _BMS Requirements.ipynb_


**If without Docker**:
- Create a Python venv
- Run `pip install -r requirements.txt`
- Run `jupyter notebook`
- Open and execute _BMS Requirements.ipynb_