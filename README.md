# IDA Plugin Template 

A Cookiecutter template for creating an IDA plugin. This template helps you quickly scaffold an IDA Python plugin

## Prerequisites

- Python 3.10+
- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- [pipx](https://pipx.pypa.io/)



## Quick Start

1. **Generate a new plugin from this template:**
   ```bash
   pipx run cookiecutter gh:HexRaysSA/ida-plugin-template 
   ```

   If you want to create the folder directly inside the .plugins dir of IDA 
   
   On linux & mac 
   ```bash
   pipx run cookiecutter gh:HexRaysSA/ida-plugin-template -o $HOME/.idapro/plugins
   ```

   On windows  
   ```bash
   pipx run cookiecutter gh:HexRaysSA/ida-plugin-template -o "%APPDATA%\Hex-Rays\IDA Pro\plugins"
   ```

2. **Fill in the prompted information:**
   - Plugin name (e.g., "IDA Test Plugin")
   - Author name and email
   - Description
   - Version

3. **Navigate to your new extension:**
   ```bash
   cd your-generated-project-name
   ```
   
## License

MIT
