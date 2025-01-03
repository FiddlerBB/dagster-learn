# dagster_learn

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## Getting started

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `dagster_learn/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_learn_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_learn_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.

# NOTE
Some note for developing purpose

## Init project 
First we need to install dagster via pip

```bash
pip install dagster
```

To init project put down command
```bash
dagster project scaffold --name <my-dagster-project>
```

Modify the requirements and run

```bash
make init
```

After installing the reqs, create `.env` file, this file should be put where the project will be run
Ex: `/dagster-learn/.env`
Create a key with `API_KEY=<your API key from Open Weather>`
Ref: https://openweathermap.org/


## Run Dagster locally and keep storage persist
Follow the dagster.yaml file, the storage will be specify in there

https://docs.dagster.io/guides/running-dagster-locally

The base_dir are exported when running `make run`