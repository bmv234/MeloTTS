# MeloTTS

A Text-to-Speech system supporting multiple languages.

## Requirements

- Python >= 3.12
- PyTorch >= 2.2.0
- See requirements.txt for full list of dependencies

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install the package:
```bash
pip install -r requirements.txt
```

3. Download required models:
```bash
python -m unidic download
```

## Usage

You can use MeloTTS through either the command line interface or the web interface.

### Command Line Interface

```bash
melotts "Hello, world!" output.wav -l EN
```

### Web Interface

```bash
melo-ui
```

Then open your browser at http://localhost:7860

## Supported Languages

- English (EN)
- Spanish (ES)
- French (FR)
- Chinese (ZH)
- Japanese (JP)
- Korean (KR)

## License

See LICENSE file for details.
