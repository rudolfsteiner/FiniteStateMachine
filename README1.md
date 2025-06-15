## Finite Automation

### Once for project
- Check python version. It should match the version in the `.python-version` file:
```
 python --version
```
- If it says the python version is not installed, install it by running:
```
pyenv install
```

- Init virtual environment

```
python -m venv venv
source venv/bin/activate

To configure, run:
```
pip install -r requirements.in

## Development

This can be tested locally by running the tests. To run the full suite of tests:
```
PYTHONPATH=. pytest
```

## Run
```
python3 app.py
```
