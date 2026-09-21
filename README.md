# FletBox Snippets Creator

Snippet generator for **FletBox** (a JS-ish Flet-like UI framework). It builds
VSCode/Neovim-friendly snippet JSON files from Python source dictionaries,
keeping the `atributo: valor` snippet style.

## Repository layout

```
├── FletBox/                          # FletBox snippets output + sources
│   ├── FletBox.json                  # Combined snippets (attrs + widgets + modules)
│   ├── FletBox_widgets.json          # Widget snippets
│   ├── FletBox_attribute_widgets.json# Attribute/util snippets
│   ├── FletBox_modules_widgets.json  # Module templates (pages, components, helpers)
│   └── FletBox_snippets_creator/     # Source dictionaries (.py)
│       ├── FletBox_create_attributes_widgets.py
│       ├── FletBox_create_widgets.py
│       └── FletBox_create_modules_widgets.py
├── python/                           # Python (Flet) snippets: flet_*.json, python.json
├── ReactNative/                      # React Native snippets: ReactNative_*.json
├── fletbox_make_snippets.py          # Generates the FletBox JSON files
├── library_make_snippets.py          # Generates the python/ JSON files
├── react_make_snippets.py            # Generates the ReactNative/ JSON files
├── install_fletbox_snippet.sh        # Installs FletBox.json for Neovim
├── installer_snippets.sh             # Installs python.json into friendly-snippets
├── create_tutorial.py                # Helper script (FastAPI examples)
└── snippet_path/                     # FastAPI chat server + Neovim paths
```

## How it works

1. Snippets are authored as Python dictionaries, one key per snippet, value
   written in `atributo: valor` form:

   ```python
   'padding': 'padding: 16,',
   'createWidget': 'createWidget({ name: "MyWidget", ... }),'
   ```

2. The generator scripts convert each dict into snippet entries:

   ```json
   {
     "prefix": "padding",
     "description": "Make a FletBox widgets padding widget",
     "body": ["padding: 16,"]
   }
   ```

3. `FletBox.json` is the combined file: attributes are merged first and widgets
   last, so on name collisions the widget version wins (as the original export).

## Regenerate the JSON files

Run from the repository root:

```bash
python3 fletbox_make_snippets.py
```

Which rebuilds:
- `FletBox/FletBox_attribute_widgets.json`
- `FletBox/FletBox_widgets.json`
- `FletBox/FletBox_modules_widgets.json`
- `FletBox/FletBox.json` (combined)

Equivalent generators exist for the other ecosystems:
`python3 library_make_snippets.py` and `python3 react_make_snippets.py`.

## Install (Neovim)

```bash
bash install_fletbox_snippet.sh     # copies FletBox/FletBox.json → ~/.config/nvim/flet-box-snippets.json
```

## Current snippet counts

| File | Entries |
| --- | --- |
| `FletBox_widgets.json` | 248 |
| `FletBox_attribute_widgets.json` | 792 |
| `FletBox_modules_widgets.json` | 14 |
| `FletBox.json` (combined) | 1023 |