# Python Static File Generator

A lightweight Python-based static site generator that converts Markdown files to HTML with support for inline styling, links, and modular content blocks.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)

## Overview

This project is a static site generator that processes Markdown content from the `content/` directory and converts it into HTML pages using a template system. It's designed to be simple, extensible, and easy to maintain.

## Features

- **Markdown to HTML Conversion**: Converts Markdown files to static HTML pages
- **Template Engine**: Uses Jinja2-style templating for consistent page layouts
- **Modular Architecture**: Organized into blocks, inline processors, and nodes for easy extension
- **Link Extraction**: Automatically processes links in content
- **Node System**: Advanced text node processing (text nodes, leaf nodes, parent nodes)
- **Comprehensive Testing**: Full test suite for all modules
- **Static Asset Management**: Handles CSS, images, and other static files

## Project Structure

```
python_static_file_generator/
├── src/                          # Main source code
│   ├── main.py                   # Entry point
│   ├── blocks/                   # Markdown block processing
│   │   ├── block_utils.py        # Block utilities and conversion
│   │   └── tests/                # Block tests
│   ├── inline/                   # Inline markdown processing
│   │   ├── link_extractor.py     # Link extraction
│   │   ├── splits.py             # Text splitting utilities
│   │   └── tests/                # Inline tests
│   ├── nodes/                    # HTML node representation
│   │   ├── html_node.py          # Generic HTML nodes
│   │   ├── text_node.py          # Text node types
│   │   ├── leaf_node.py          # Leaf nodes
│   │   ├── parent_node.py        # Parent/container nodes
│   │   └── tests/                # Node tests
│   └── os_utils/                 # File system utilities
│       ├── utils.py              # Directory and page generation
│       └── tests/                # OS utility tests
├── content/                      # Markdown source files
│   ├── index.md                  # Homepage
│   ├── blog/                     # Blog posts
│   │   ├── glorfindel/
│   │   ├── majesty/
│   │   └── tom/
│   └── contact/                  # Contact page
├── public/                       # Generated HTML output
├── docs/                         # Alternative output directory
├── static/                       # Static assets (CSS, images)
│   ├── index.css
│   └── images/
├── template.html                 # HTML template for pages
├── build.sh                      # Build script (with base path)
├── main.sh                       # Local development script
├── test.sh                       # Test runner script
└── README.md                     # This file
```

## Installation

### Prerequisites

- Python 3.12+ (required)

### Dependencies

This project uses only Python standard library modules—no external dependencies required!

## Usage

### Quick Start

**Local Development (with live server):**
```bash
./main.sh
```
Generates the site and starts an HTTP server on port 8888.

**Production Build (GitHub Pages):**
```bash
./build.sh
```
Generates the site with base URL `https://aggelosar.github.io/python_static_file_generator/`


### Building the Site

The generation process follows a two-step flow:

1. **Initialize Static Assets** - The generator cleans and recreates the output directory, then copies all static files (CSS, images, etc.) from `static/` to the destination folder to ensure assets are available.

2. **Generate HTML Pages** - The generator recursively scans the `content/` directory for Markdown files, processes each one by:
   - Extracting the page title (first heading)
   - Converting Markdown to HTML
   - Injecting content into the template
   - Rewriting all relative asset paths to use the configured base path
   - Writing the final HTML to the corresponding location in the destination folder

The directory structure in `content/` is mirrored exactly in the output, maintaining your site's organizational hierarchy.

### Adding Content

1. Create a Markdown file in the `content/` directory (e.g., `content/about.md`)
2. The generator automatically converts it to HTML maintaining the directory structure
3. Include a top-level heading in your Markdown—it becomes the page title

### Template System

The `template.html` defines the layout for all pages. Available variables:
- `{{ Title }}` - Extracted from first heading in Markdown
- `{{ Content }}` - Generated HTML from Markdown content

## Development

### Project Modules

- **blocks**: Handles block-level Markdown elements (paragraphs, lists, etc.)
- **inline**: Processes inline Markdown (bold, italic, links, etc.)
- **nodes**: Internal representation of HTML elements as a tree structure
- **os_utils**: File system operations and page generation

### Extending the Generator

To add new features:

1. **New block types**: Add to `src/blocks/block_utils.py`
2. **New inline styles**: Add to `src/inline/splits.py`
3. **Custom processing**: Modify node classes in `src/nodes/`

## Testing

Run the full test suite:
```bash
./test.sh
```

Or manually with Python's unittest:
```bash
python3 -m unittest discover -s src
```

Tests are organized by module:
- `src/blocks/tests/`
- `src/inline/tests/`
- `src/nodes/tests/`
- `src/os_utils/tests/`

## License

This project is licensed under the MIT License. See the LICENSE file for details.

MIT License

Copyright (c) 2026 Aggelos Arelakis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

## Author

**Aggelos Arelakis**
