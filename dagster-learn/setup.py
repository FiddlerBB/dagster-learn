from setuptools import find_packages, setup

setup(
    name="dagster_learn",
    packages=find_packages(exclude=["dagster_learn_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "polars",
        "dlt"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
