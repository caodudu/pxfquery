from setuptools import setup, find_packages

setup(
    name="pxfquery",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["PyYAML>=6"],
    entry_points={"console_scripts": ["pxfquery=pxfquery.cli:main"]},
    python_requires=">=3.10",
)
