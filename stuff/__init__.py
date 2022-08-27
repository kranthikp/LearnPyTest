#dunder init file

#---------------------------------
#commands and Configs - chapter 7
#---------------------------------
### Commands ###
# python -m pytest --help: to get all command details in pytest
# python -m pytest: to run pytest
# python -m pytest --verbose: to run pytest with more data in output
# python -m pytest --quiet: to get o/p in brief console
# python -m pytest --junit-xml report.xml: to get junit xml report

### Configs ###
# pytest.ini #most common one
# proper conventions, loaded in root dir are must

#adding config file to our project


#chapter 8 filter testcaes
# to run specific test file:
# python -m pytest tests/test_accum.py
# python -m pytest tests/test_math.py

# to run specific testcase within test file:
# python -m pytest tests/test_math.py::test_one_plus_one
# python -m pytest tests/test_math.py::test_one_plus_two

# to run specific test file or case which contain string:
# python -m pytest -k one
# python -m pytest -k "one and not accum"

##### Note:
# any test can have any markers
# when you marker do specify in pytest.ini file
# python -m pytest -m math

#------------------------------------------------------------------------------
# any test can have any markers
# user can register/create customized markers in pytest.ini

## Most commonly used are
# skip - always skip a test function
# skipif - skip a test function if a certain condition is met
# xfail - produce an "expected failure" outcome if a certain condition is met
# parametrize -  to perform multiple calls to the same test function
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# setting testpaths in config file will allow easily modularize code flow

## testpaths
# [pytest]
# testpaths = testing doc

## usefixtures
# [pytest]
# usefixtures =
        # clean_db

## xfail_strict
# [pytest]
# xfail_strict = True

## Registering markers
# [pytest]
# markers =
    # slow: marks tests as slow (deselect with -m "not slow"
    # serial

#------------------------------------------------------------------------------
