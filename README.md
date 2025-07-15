# Upstox MCP Server

A Model Context Protocol (MCP) server for integrating Upstox trading functionality with AI assistants and applications.

## Overview

This MCP server provides tools and resources for interacting with Upstox trading APIs, allowing AI assistants to help with trading operations, market data retrieval, and portfolio management.

## Features

- 🔧 **Trading Tools**: Execute trades and manage orders
- 📊 **Market Data**: Access real-time and historical market data
- 💼 **Portfolio Management**: View and manage your trading portfolio
- 🔒 **Secure Authentication**: Uses Upstox OAuth for secure API access

## Prerequisites

- Python 3.12 or higher
- Upstox trading account
- Upstox API credentials

## Installation

### Option 1: Install from PyPI (when published)

```bash
pip install upstox-mcp-server
```

### Option 2: Install from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/upstox-mcp-server.git
   cd upstox-mcp-server
   ```

2. **Install dependencies**:
   
   Using uv (recommended):
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -e .
   ```

3. **For development**:
   ```bash
   # Using uv
   uv sync --dev
   
   # Or using pip
   pip install -e ".[dev]"
   ```

## Quick Setup

### 1. Get Your Upstox API Credentials
1. Visit [Upstox Developer Console](https://developer.upstox.com/)
2. Create a new app to get your API credentials
3. Note down your API Key, API Secret, and Redirect URI

### 2. Choose Your Client

The `config/` directory contains ready-to-use configuration files for popular MCP clients:

- **Claude Desktop**: Copy `config/claude_desktop_config.json` to:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
  - Linux: `~/.config/Claude/claude_desktop_config.json`

- **Cursor IDE**: Use `config/cursor_config.json` as reference for your Cursor settings

- **Continue.dev**: Copy `config/continue_config.json` to `~/.continue/config.json`

- **Zed Editor**: Merge `config/zed_settings.json` with your existing settings file

### 3. Set Your Credentials
Replace the placeholder values in your chosen configuration file:
```json
{
  "UPSTOX_API_KEY": "your_actual_api_key",
  "UPSTOX_API_SECRET": "your_actual_api_secret",
  "UPSTOX_REDIRECT_URI": "your_actual_redirect_uri"
}
```

### 4. Restart Your Client
Restart your MCP client to load the new configuration.

## Configuration

### 1. Upstox API Setup

1. Visit [Upstox Developer Console](https://developer.upstox.com/)
2. Create a new app to get your API credentials
3. Note down your:
   - API Key
   - API Secret
   - Redirect URI

### 2. Environment Variables

Create a `.env` file in your project directory:

```env
UPSTOX_API_KEY=your_api_key_here
UPSTOX_API_SECRET=your_api_secret_here
UPSTOX_REDIRECT_URI=your_redirect_uri_here
```

## Usage

### Running the MCP Server

#### Standalone Mode
```bash
upstox-mcp-server
```

Or using Python module:
```bash
python -m mcpserver
```

## Client Integration

The Upstox MCP server can be integrated with various MCP-compatible clients. Below are configuration examples for popular clients:

### 1. Claude Desktop

**For macOS** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "upstox": {
      "command": "upstox-mcp-server",
      "env": {
        "UPSTOX_API_KEY": "your_api_key_here",
        "UPSTOX_API_SECRET": "your_api_secret_here",
        "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
      }
    }
  }
}
```

**For Windows** (`%APPDATA%\Claude\claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "upstox": {
      "command": "upstox-mcp-server",
      "env": {
        "UPSTOX_API_KEY": "your_api_key_here",
        "UPSTOX_API_SECRET": "your_api_secret_here", 
        "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
      }
    }
  }
}
```

**For Linux** (`~/.config/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "upstox": {
      "command": "upstox-mcp-server",
      "env": {
        "UPSTOX_API_KEY": "your_api_key_here",
        "UPSTOX_API_SECRET": "your_api_secret_here",
        "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
      }
    }
  }
}
```

### 2. Cursor IDE

Cursor supports MCP through its settings. Add this to your Cursor settings:

**Method 1: Via Cursor Settings UI**
1. Open Cursor Settings (Cmd/Ctrl + ,)
2. Search for "MCP" or "Model Context Protocol"
3. Add a new MCP server with these details:
   - **Name**: `upstox`
   - **Command**: `upstox-mcp-server`
   - **Environment Variables**:
     ```
     UPSTOX_API_KEY=your_api_key_here
     UPSTOX_API_SECRET=your_api_secret_here
     UPSTOX_REDIRECT_URI=your_redirect_uri_here
     ```

**Method 2: Via Configuration File**
Add to your Cursor configuration file (`~/.cursor/config.json` or similar):
```json
{
  "mcp": {
    "servers": {
      "upstox": {
        "command": "upstox-mcp-server",
        "env": {
          "UPSTOX_API_KEY": "your_api_key_here",
          "UPSTOX_API_SECRET": "your_api_secret_here",
          "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
        }
      }
    }
  }
}
```

### 3. Continue.dev (VS Code Extension)

Add this to your Continue configuration file (`~/.continue/config.json`):

```json
{
  "models": [
    {
      "title": "GPT-4 with Upstox",
      "provider": "openai",
      "model": "gpt-4",
      "apiKey": "your_openai_api_key"
    }
  ],
  "contextProviders": [
    {
      "name": "mcp",
      "params": {
        "serverName": "upstox",
        "command": "upstox-mcp-server",
        "env": {
          "UPSTOX_API_KEY": "your_api_key_here",
          "UPSTOX_API_SECRET": "your_api_secret_here",
          "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
        }
      }
    }
  ]
}
```

### 4. Zed Editor

For Zed editor, add this to your settings file (`~/.config/zed/settings.json`):

```json
{
  "assistant": {
    "mcp_servers": {
      "upstox": {
        "command": "upstox-mcp-server",
        "env": {
          "UPSTOX_API_KEY": "your_api_key_here",
          "UPSTOX_API_SECRET": "your_api_secret_here",
          "UPSTOX_REDIRECT_URI": "your_redirect_uri_here"
        }
      }
    }
  }
}
```

### 5. Custom MCP Client

For custom implementations or other MCP clients, use this general configuration:

**Server Command**: `upstox-mcp-server`
**Transport**: `stdio`
**Environment Variables**:
```env
UPSTOX_API_KEY=your_api_key_here
UPSTOX_API_SECRET=your_api_secret_here
UPSTOX_REDIRECT_URI=your_redirect_uri_here
```

### 6. Docker Integration

You can also run the MCP server in a Docker container for consistent deployment:

**Dockerfile**:
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -e .

CMD ["upstox-mcp-server"]
```

**Docker Compose** (`docker-compose.yml`):
```yaml
version: '3.8'
services:
  upstox-mcp-server:
    build: .
    environment:
      - UPSTOX_API_KEY=${UPSTOX_API_KEY}
      - UPSTOX_API_SECRET=${UPSTOX_API_SECRET}
      - UPSTOX_REDIRECT_URI=${UPSTOX_REDIRECT_URI}
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
```

## Configuration Tips

### Environment Variable Management

**Option 1: Using .env file**
Create a `.env` file in your project directory:
```env
UPSTOX_API_KEY=your_api_key_here
UPSTOX_API_SECRET=your_api_secret_here
UPSTOX_REDIRECT_URI=your_redirect_uri_here
```

**Option 2: System Environment Variables**
```bash
# Add to your shell profile (.bashrc, .zshrc, etc.)
export UPSTOX_API_KEY="your_api_key_here"
export UPSTOX_API_SECRET="your_api_secret_here"
export UPSTOX_REDIRECT_URI="your_redirect_uri_here"
```

**Option 3: Client-specific Environment**
Most MCP clients allow you to set environment variables directly in their configuration files as shown in the examples above.

### Troubleshooting Client Integration

1. **Server Not Starting**:
   - Ensure `upstox-mcp-server` is installed and in your PATH
   - Check that Python 3.12+ is available
   - Verify environment variables are set correctly

2. **Permission Issues**:
   ```bash
   # Make sure the server executable has proper permissions
   chmod +x $(which upstox-mcp-server)
   ```

3. **Environment Variables Not Loading**:
   - Use absolute paths for .env files
   - Ensure no extra spaces in variable assignments
   - Check client-specific documentation for environment variable syntax

4. **Testing the Server**:
   ```bash
   # Test the server directly
   upstox-mcp-server --help
   
   # Run in debug mode
   UPSTOX_DEBUG=true upstox-mcp-server
   ```

### Advanced Configuration

For production deployments, consider:

1. **Logging Configuration**:
   ```env
   LOG_LEVEL=INFO
   LOG_FILE=/var/log/upstox-mcp-server.log
   ```

2. **Rate Limiting**:
   ```env
   UPSTOX_RATE_LIMIT=100  # requests per minute
   ```

3. **Timeout Settings**:
   ```env
   UPSTOX_TIMEOUT=30  # seconds
   ```

#### With MCP Client

The server can be integrated with any MCP-compatible client using the configurations provided in the "Client Integration" section above.

## Available Tools

Currently available:
- `helloWorld`: Basic connectivity test

*More Upstox-specific tools will be added in future versions.*

## Development

### Setting up Development Environment

1. **Clone and install**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/upstox-mcp-server.git
   cd upstox-mcp-server
   uv sync --dev
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

3. **Code formatting**:
   ```bash
   black src/
   isort src/
   ```

4. **Type checking**:
   ```bash
   mypy src/
   ```

### Project Structure

```
upstox-mcp-server/
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py      # Entry point
│       └── server.py        # Main server implementation
├── config/                  # Ready-to-use client configurations
│   ├── claude_desktop_config.json
│   ├── cursor_config.json
│   ├── continue_config.json
│   └── zed_settings.json
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker container definition
├── pyproject.toml          # Project configuration
├── README.md               # This file
├── uv.lock                 # Dependency lock file
├── .env.example            # Environment variables template
└── .gitignore              # Git ignore patterns
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `pytest`
5. Format code: `black src/ && isort src/`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## Security

- Never commit API credentials to version control
- Use environment variables for sensitive configuration
- Follow Upstox API security best practices
- Report security vulnerabilities via GitHub Issues

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is for educational purposes. Trading involves risk. Use at your own discretion. The authors are not responsible for any financial losses.

## Support

- 📚 [Upstox API Documentation](https://upstox.com/developer/api-documentation)
- 🔧 [MCP Specification](https://modelcontextprotocol.io/)
- 🐛 [Report Issues](https://github.com/YOUR_USERNAME/upstox-mcp-server/issues)
- 💬 [Discussions](https://github.com/YOUR_USERNAME/upstox-mcp-server/discussions)

---

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username in the URLs above.
