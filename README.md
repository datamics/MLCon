# Machine Learning Conference Workshop (MLCon)

This repository contains the code, notebooks, and presentations from the MLCon Munich 2025 Workshop, focusing on efficient machine learning workflows using tools like FiftyOne and Label Studio.

## Table of Contents

- [Project Description](#project-description)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This repository provides hands-on resources for the MLCon Workshop, including code, data, and presentations for practical sessions on machine learning data curation, labeling, and experiment tracking.

## Folder Structure

```
MLCon/
├── 1_FiftyOne/           # Notebooks and resources for FiftyOne
│   ├── 1. Check Installation and basics.ipynb
│   └── fiftyone_root/
├── 2_LabelStudio/        # Notebooks for Label Studio
│   └── 1. Create Labeling Project.ipynb
├── data/                 # Workshop datasets
│   └── winequality.csv
├── Makefile              # Automation for setup and running tools
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore
├── .python-version
└── .venv/                # Virtual environment (not tracked)
```

## Setup Instructions

Follow these steps to set up your environment:

```bash
# 1. Clone the repository
git clone <repository-url>
cd MLCon_25S/MLCon

# 2. (Recommended) Use the provided Makefile for setup
make setup

# Alternatively, set up manually:
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Makefile Commands

| Command               | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| `make setup`          | Install Python 3.12 (if needed), create venv, install requirements|
| `make install`        | Install Python dependencies from requirements.txt                |
| `make run fiftyone`   | Launch the FiftyOne app (for dataset visualization)              |
| `make run labelstudio`| Launch the Label Studio app (for data labeling)                  |
| `make check`          | Check if Python 3.12 is installed                                |

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements, bug fixes, or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
