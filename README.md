# cython-template-project

![Build Status](https://gitlab.com/logan/cython-template-project/badges/master/build.svg)

A small Cython template project with
[Gitlab-CI](https://gitlab.com/help/ci/README.md),
[py.test](http://pytest.org/latest/), and
[sphinx](http://www.sphinx-doc.org/en/stable/)
integration.

[Project pages](https://logan.gitlab.io/cython-template-project/)
with sphinx autodoced API documentation are built and served from the
Gitlab-CI service.

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

The following is a summary of what works and what does not with Gitlab-CI:

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

# Editing the "proj" name

Take care to change the `proj` name in the following files:

- `setup.py`
- `tox.ini`
- `docs/apidoc.sh`
- `docs/source/conf.py`

Also take care to update `tests/*` and remove `docs/source/proj.*`
