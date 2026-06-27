from pathlib import Path

from setuptools import find_packages, setup


def read_version() -> str:
    ns = {}
    exec((Path(__file__).parent / "src" / "pxfquery" / "l5_presentation" / "version.py").read_text(), ns)
    return ns["__version__"]

setup(
    name="pxfquery",
    version=read_version(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["PyYAML>=6"],
    entry_points={"console_scripts": ["pxfquery=pxfquery.l5_presentation.cli:main"]},
    python_requires=">=3.10",
)
