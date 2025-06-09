# Machine Learning Conference Workshop (MLCon)

This repository contains the code written during the MLCon Munich 2025 Workshop, along with related presentations and resources.

## Table of Contents

- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
- [Makefile Commands](#makefile-commands)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This repo will contain the code written during the Workshop along with the Presentations.

## Setup Instructions

Follow these steps to set up your development environment:

```bash
# 1. Clone the repository
git clone <repository-url>
cd MLCon_25S/MLCon

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies using Makefile
make requirements
```

## Makefile Commands

| Command            | Description                                 |
|--------------------|---------------------------------------------|
| `make requirements`| Install all Python dependencies from requirements.txt |
| `make test`        | Run the test suite                          |
| `make clean`       | Remove temporary files and build artifacts  |
| `make lint`        | Run code linters (if configured)            |

## Folder Structure

```
MLCon_25S/
└── MLCon/
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── 1_FiftyOne/
    ├── 2_LabelStudio/
    ├── data/
    └── ...
```

- `Makefile`: Automates setup and development tasks.
- `requirements.txt`: Lists Python dependencies.
- `1_FiftyOne/`, `2_LabelStudio/`: Workshop modules and code.
- `data/`: Datasets and related files.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements, bug fixes, or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
