# pyTemplate
This is a Python project template that includes a basic structure for a Python application, including configuration, modules, tests, and utilities. It also includes a pre-configured [Poetry](https://python-poetry.org/) project and [Ruff](https://docs.astral.sh/ruff/) linting settings.

The project uses [Pydantic](https://docs.pydantic.dev/latest/) for handling environment variables, which are loaded from a `.env` file. This provides a type-safe and validated way of accessing and managing configuration settings.

## Table of Contents
1. [Template Structure](#template-structure)
2. [Setup](#setup)
3. [Usage](#usage)
4. [License](#license)

## Template Structure
The project structure is as follows:

```
pyTemplate
├── .env.example
├── .gitignore
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── docs
│   └── documentation.md
└── pytemplate
    ├── __init__.py
    ├── config.py
    ├── main.py
    ├── modules
    │   ├── __init__.py
    │   └── xmodule
    │       ├── __init__.py
    │       ├── module_helpers.py
    │       └── module.py
    ├── tests
    │   └── x
    │       └── x_test.py
    └── utils
        ├── __init__.py
        └── utils.py
```

- `.env.example`: Example environment variables file.
- `.gitignore`: Gitignore file to exclude certain files from version control.
- `LICENSE`: The project's license file.
- `poetry.lock`: Poetry's lock file, ensuring consistent dependency versions.
- `pyproject.toml`: Poetry's project configuration file.
- `README.md`: This README file.
- `docs/documentation.md`: Additional project documentation.
- `pytemplate/`: The main Python package directory.
  - `config.py`: Configuration module.
  - `__init__.py`: Package initialization file.
  - `main.py`: Entry point for the application.
  - `modules/`: Directory for project modules.
  - `tests/`: Directory for test cases.
  - `utils/`: Directory for utility modules.

## Setup
To set up the project, you'll need to have poetry installed. Then, follow these steps:

1. Clone the repository:
```sh
git clone https://github.com/ItsZcx/pyTemplate.git
```

2. Navigate to the project directory:
```sh
cd pyTemplate
```

3. Install the project dependencies using Poetry:
```sh
poetry install
```

4. (Optional) Create a virtual environment and activate it:
```sh
poetry shell
```

## Usage
To run the application, use the following command:
```sh
poetry run python pytemplate/main.py
```

To run the tests, use the following command:
```sh
poetry run pytest
```

## License
This project is licensed under the [MIT License](LICENSE).