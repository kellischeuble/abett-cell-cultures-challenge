Cell Cultures Challenge

### Assignments

[task instructions](https://github.com/kellischeuble/abett-cell-cultures-challenge/blob/main/CodingChallenge1.pdf)  
```
Task: grid of cell culture medium has (L) for livable, and (.) for unlivable.

Rules:
    - will grow if a livable area is empty and there are no adjacent cell cultures 
    - will die if a livable area//culture is surrounded by four other adjacent cultures
    - everything else stays the same
```

### Install

create virtual environment with pipenv

`pip install pipenv`  
`pipenv install -r requirements.txt`  
`pipenv shell`  

or from your own virtual environment with Python 3.8 using

`pip install -r requirements.txt`

### Usage

In main directory (same level as README and Pipfile):

`export PYTHONPATH=./`  
`make run_experiment`

### Testing

`make test`

### TODOs:

```
- Expand on testing
- Add error handling 
```
