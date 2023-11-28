## Pytest Module

**Advantages**

- Can run multiple tests in parallel, reducing text execution time.
- Allows us to skip a subset of test during execution.
- Allows us to run a subset of the entire test suite.
- Easy to learn and use.

**Installing Pytest**

```
source testing_env/bin/activate
pip install pytest
pytest -h
```

## running tests

- Test discovery - `pytest`
- Specify a test file - `pytest tests/test_main.py`
- Running a specific test suite - `pytest -k TestExample`
- Run a subset of tests - `pytest -k <subset>`
- Verbosity - `pytest -v` `pytest -k multiply -v`


> Selects tests to run based on a substring of matching test names
> Select test groups to run based on the markers applied.
`@pytest.mark.<group_name>`
`pytest -m <group_name>`

### Registering markers

- Create a file called `pytest.ini` in the root directory
- Register markers inside the file
