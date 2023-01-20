# BlameRufus

## Dependency & Installation

I employ the open-source Git Python API `GitPython` for the project. To install requirements for this solution, run
```commandline
pip3 install -r requirements.txt
```

## Run the Solution

As required, there's only one command line argument `--git_dir`, which I set the default value as `.` the current repository. To run the solution, execute
```commandline
python3 BlameRufus.py --git_dir ${TARGET_DIRECTORY}
```
for result.