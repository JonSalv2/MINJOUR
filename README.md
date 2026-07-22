# MINJOUR

A minimalistic journaling app for the terminal.

Open the app, type your thought, close the app. Entries are timestamped and saved to a JSON file of your choice, so you can keep separate journals for different topics (work, dreams, ideas, etc.).

---

## Features

- Create a new journal file or open an existing one (automatically get timestamped)
- Read all entries in a chosen journal
- Delete entries by ID (IDs auto-reindex)
- Access Multiple journals; each stored as its own `.json` file in the `entries/` directory

---

## Download and run (macOS)

1. Go to the [Releases](../../releases) page and download the latest `MINJOUR.app.zip`.
2. Double-click the zip to unpack it. You'll get `MINJOUR.app`.
3. Drag `MINJOUR.app` into your `Applications` folder (optional but recommended).
4. Double-click `MINJOUR.app`and a Terminal window will open running MINJOUR.

> **First launch:** macOS will show a warning that the app is from an unidentified developer. Right-click `MINJOUR.app` → **Open** → **Open** in the dialog. macOS remembers the choice, so subsequent launches work with a normal double-click.

The app runs natively on both Apple Silicon and Intel Macs.

---

## Running from source

Requires **Python 3.9+**.

```bash
git clone https://github.com/JonSalv2/MINJOUR.git
cd MINJOUR
python3 main.py
```

No third-party dependencies — MINJOUR uses only the Python standard library.

---

## Usage

On launch you'll see:

```
Press (n) to create a new file
Press (o) to open an existing file
Press (q) to quit
```

Once a journal is open:

```
press (enter) for a new entry
press (r)     to read your entries
press (d)     to delete an entry
press (m)     to return to main menu
press (q)     to quit
```

---

## Project structure

```
MINJOUR/
├── main.py           # Entry point and main menu loop
├── actions.py        # Add, read, delete entry logic
├── file_io.py        # File naming, listing, and JSON I/O
├── entries/          # Your journal files live here (gitignored)
├── main.spec         # PyInstaller build configuration
├── MINJOUR.icns      # macOS app icon
└── MINJOUR.command   # Double-clickable launcher (macOS)
```

---

## Building from source 

*You don't need this section to use MINJOUR.*

Grab the pre-built app from the [Releases](../../releases) page. These instructions are for contributors or anyone who wants to compile a native binary themselves.

The included [main.spec](main.spec) auto-detects your operating system, so the same command produces the right output on any platform:

```bash
pip install pyinstaller
pyinstaller main.spec
```

| Host OS | What you get in `dist/` |
|---|---|
| **macOS** | `MINJOUR.app` (universal2 — runs on Intel + Apple Silicon) and a `minjour/` folder with the raw binary |
| **Windows** | `minjour/` folder containing `minjour.exe` |
| **Linux** | `minjour/` folder containing the `minjour` binary |

PyInstaller builds are platform-specific. Therefore, a build on macOS produces a Mac binary only. To ship on other operating systems, run the same command on each target OS.

### Custom icons

- macOS: the spec uses `MINJOUR.icns` (included).
- Windows: drop a `MINJOUR.ico` file next to `main.spec` and the spec will pick it up automatically. If it's missing, the build still succeeds, and the executable just uses the default PyInstaller icon.
- Linux: no icon is embedded (Linux desktop icons are typically set via a `.desktop` file, outside the scope of this project).

### macOS-specific notes

- **Gatekeeper warning on first launch.** Because MINJOUR is not signed with an Apple Developer certificate, macOS will show *"MINJOUR can't be opened because Apple cannot check it for malicious software"* the first time the app is opened. Right-click `MINJOUR.app` → **Open** → **Open** in the confirmation dialog. macOS remembers the choice, so subsequent launches work with a normal double-click.
- **Universal2 build requirement.** Producing a universal2 binary requires a universal2 Python. The official installer from [python.org](https://python.org/downloads/macos) provides one; Homebrew's Python does not. If you want to build for only the host architecture, change `target_arch='universal2'` to `target_arch=None` in [main.spec](main.spec).
- **`MINJOUR.command`** is a fallback shell launcher for anyone who wants to run the raw binary from the source tree without going through the `.app`.

---

## License

MIT
