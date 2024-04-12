from __future__ import annotations

import os
import shutil
from itertools import chain
from itertools import product

import nox


@nox.session
def tests(session: nox.Session) -> None:
    """Run the tests."""
    session.install("pytest")
    session.install(".[dev]")
    session.run("pytest", "--cov=logoizer", "-vvv")
    session.run("coverage", "report", "--ignore-errors", "--show-missing")
    # "--fail-under=100",


@nox.session
def cli(session: nox.Session) -> None:
    """Test the command line interface."""
    session.install(".")
    session.run("logoize", "--version")
    session.run("logoize", "--help")

    with session.chdir(session.create_tmp()):
        for fmt, theme in product(("png", "svg"), ("dark", "light")):
            output = f"foo-{theme}.{fmt}"
            session.run(
                "logoize", "foo", f"--format={fmt}", f"--theme={theme}", "-o", output
            )
            assert os.path.exists(output)


@nox.session
def lint(session: nox.Session) -> None:
    """Look for lint."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")

    # towncrier(session)


@nox.session
def towncrier(session: nox.Session) -> None:
    """Check that there is a news fragment."""
    session.install("towncrier")
    session.run("towncrier", "check", "--compare-with", "origin/main")


@nox.session
def docs(session: nox.Session) -> None:
    """Build the docs."""
    session.install(".[doc]")

    session.chdir("docs")
    if os.path.exists("_build"):
        shutil.rmtree("_build")
    session.run("sphinx-apidoc", "--force", "-o", "api", "../logoizer")
    session.run("sphinx-build", "-b", "html", "-W", ".", "_build/html")


@nox.session
def build(session: nox.Session) -> None:
    """Build sdist and wheel dists."""
    session.install("pip")
    session.install("wheel")
    session.install("setuptools")
    session.run("python", "--version")
    session.run("pip", "--version")
    session.run(
        "python", "setup.py", "bdist_wheel", "sdist", "--dist-dir", "./wheelhouse"
    )


@nox.session
def release(session):
    """Tag, build and publish a new release to PyPI."""
    session.install("zest.releaser[recommended]")
    session.install("zestreleaser.towncrier")
    session.install(".")
    session.run("fullrelease")


@nox.session
def publish_testpypi(session):
    """Publish wheelhouse/* to TestPyPI."""
    session.run("twine", "check", "wheelhouse/*")
    session.run(
        "twine",
        "upload",
        "--skip-existing",
        "--repository-url",
        "https://test.pypi.org/legacy/",
        "wheelhouse/*.tar.gz",
    )


@nox.session
def publish_pypi(session):
    """Publish wheelhouse/* to PyPI."""
    session.run("twine", "check", "wheelhouse/*")
    session.run(
        "twine",
        "upload",
        "--skip-existing",
        "wheelhouse/*.tar.gz",
    )


@nox.session(python=False)
def clean(session):
    """Remove all .venv's, build files and caches in the directory."""
    PROJECT = "logoizer"
    ROOT = os.path.dirname(__file__)

    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("wheelhouse", ignore_errors=True)
    shutil.rmtree(f"src/{PROJECT}.egg-info", ignore_errors=True)
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    shutil.rmtree(".venv", ignore_errors=True)
    for p in chain(ROOT.rglob("*.py[co]"), ROOT.rglob("__pycache__")):
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()
