# JSON2Mieru

JSON2Mieru is a simple Windows utility that converts Mieru JSON configuration files into `mierus://` share links.

## Features

- Convert Mieru JSON to `mierus://`
- Automatic domain detection from filename
- One-click copy to clipboard
- Standalone Windows executable

## Download

Download the latest version from the **Releases** page:

https://github.com/balerinka74/json2mieru/releases

## Quick Start

1. Download **JSON2Mieru.exe** from the Releases page.
2. Run the application.
3. Click **Select JSON**.
4. Choose a Mieru configuration file.
5. Copy the generated `mierus://` link.

## Build from source

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/main.py
```

Build the executable:

```bash
pyinstaller --onefile --windowed --name JSON2Mieru app/main.py
```

## License

MIT