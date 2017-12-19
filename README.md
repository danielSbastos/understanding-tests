# Understanding Tests in Python

This repository contains 4 `*.py` files in the root dir that will be used in order to help exemplify how unit tests can be written in Python. The slides for this presentation are in [20171212-tests-python-joinville](https://github.com/magrathealabs/presentations)

- [Dependencies](#dependencies)
- [Setup](#setup)
- [Summary](#summary)
- [Code Quality](#code_quality)

## Dependencies

- Python > 3.5.x

## Setup

`pip install -r requirements.txt`

## Summary (file and their tests)

- [file_actions.py](https://github.com/danielSbastos/understanding-tests/blob/master/file_actions.py) has tests regarding mocks, stubs and no test doubles at all.
    - [test_file_actions_doubles.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_file_actions_doubles.py) uses uber's test doubles lib, https://github.com/uber/doubles.
    - [test_file_actions_mock.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_file_actions_mock.py) has unittest.mock, https://github.com/testing-cabal/mock, lib in order to mock methods.
    - [test_file_actions_no_doubles.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_file_actions_no_doubles.py) exemplifies that test doubles are not always needed in tests.

- [joinville.py](https://github.com/danielSbastos/understanding-tests/blob/master/joinville.py) exemplifies how to use the 5 test doubles, dummy, stub, fake, spy and mock.
    - [test_joinville_dummy.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_joinville_dummy.py) explains test dummies by testing `joinville.py`.
    - [test_joinville_stub.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_joinville_stub.py) explains test stubs.
    - [test_joinville_fake.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_joinville_fake.py) explains test fakes.
    - [test_joinville_spy.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_joinville_spy.py) explains test spies.
    - [test_joinville_mock.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_joinville_mock.py) explains test mocks.

- [post.py](https://github.com/danielSbastos/understanding-tests/blob/master/post.py) helps us understand how to mock http requests in unit tests.
    - [test_post.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_post.py) contains tests that uses mocks to test HTTP requests.

- [user.py](https://github.com/danielSbastos/understanding-tests/blob/master/user.py) contains a simple class with user functionalities that evidences that test doubles are not needed all the time when tests are done.
    - [test_user.py](https://github.com/danielSbastos/understanding-tests/blob/master/tests/test_user.py) tests `user.py` with no test doubles.<

## Code Quality

[tox](https://github.com/tox-dev/tox) is used in order to run tests with [pytest](https://github.com/pytest-dev/pytest) and code quality and lintage with [pep8](https://github.com/pycqa/pycodestyle).
