# cython-template-project

[![Build Status](https://gitlab.com/logan/cython-template-project/badges/pytest_doctest/build.svg)](https://gitlab.com/logan/cython-template-project/badges/pytest_doctest/build.svg)
[![Build Status](https://travis-ci.org/lgpage/cython-template-project.svg?branch=pytest_doctest)](https://travis-ci.org/lgpage/cython-template-project)

A small Cython template project with
[Gitlab-CI](https://gitlab.com/help/ci/README.md) or [Travis
CI](https://travis-ci.org/), [py.test](http://pytest.org/latest/), and
[sphinx](http://www.sphinx-doc.org/en/stable/) integration.

[Project pages](https://logan.gitlab.io/cython-template-project/), for
[Gitlab](https://gitlab.com/), with sphinx autodoc'ed API documentation are
built and served from the Gitlab-CI service.

# Building

Build without Cython:
```bash
$ python setup.py build_ext develop
```

Build with Cython:
```bash
$ python setup.py build_ext develop --use-cython
```

# Testing

Testing with tox and py.test:
```bash
$ pip install tox
$ python setup.py build_ext test
```

# Gitlab-CI

Continous integration is done using
[Gitlab-CI](https://gitlab.com/help/ci/README.md) with the required
[.gitlab-ci.yml](https://gitlab.com/help/ci/yaml/README.md) file.

The continous integration can also be done using [Travis
CI](https://travis-ci.org/) and the equivalent
[.travis.yml](https://docs.travis-ci.com/user/getting-started/) file.

The following is a summary of what works and what does not with CI:

- build: Yes (with and without cython)
- test:
    - tox: Yes
    - py.test: Yes
    - doctest: Yes (with a hack)
    - coverage: No
    - coveralls: No
- deploy:
    - sphinx docs: Yes
    - sphinx autodoc'ed API: Yes
    - serve Gitlab pages: Yes
    - serve Github pages: No (Was too lazy to try)

Note: Example of serving Github pages discussed
[here](https://github.com/steveklabnik/automatically_update_github_pages_with_travis_example)


# Editing the "proj" name

Take care to change the `proj` name in the following files:

- `setup.py`
- `tox.ini`
- `docs/apidoc.sh`
- `docs/source/conf.py`

Also take care to update `tests/*` and remove `docs/source/proj.*`
