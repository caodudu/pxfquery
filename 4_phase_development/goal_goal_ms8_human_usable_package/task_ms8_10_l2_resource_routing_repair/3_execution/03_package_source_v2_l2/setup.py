from pathlib import Path

from setuptools import find_packages, setup


def read_version() -> str:
    ns = {}
    exec((Path(__file__).parent / "src" / "pxfquery" / "version.py").read_text(), ns)
    return ns["__version__"]

setup(
    name="pxfquery",
    version=read_version(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["PyYAML>=6", "numpy>=1.23", "pandas>=1.5", "anndata>=0.9", "openai>=1.0"],
    entry_points={"console_scripts": ["pxfquery=pxfquery.cli:main"]},
    python_requires=">=3.10",
)
