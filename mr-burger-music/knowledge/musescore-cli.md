# MuseScore CLI Reference

**CLI path:** `/Applications/MuseScore 4.app/Contents/MacOS/mscore`
**Version:** MuseScore4 4.6.5
**Last verified:** 2026-03-21

---

## Basic Usage

```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.pdf input.musicxml
```

The `-o` / `--export-to` flag sets the output file. Format is inferred from the output file extension.

Input file is the final positional argument.

---

## Export Commands

### PDF
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.pdf input.musicxml
```

### MP3
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.mp3 input.musicxml
```
Optional: set bitrate with `-b <kbps>` (e.g., `-b 128`)

### PNG
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.png input.musicxml
```
Optional: set DPI with `-r <DPI>` (e.g., `-r 300`); trim with `-T <margin>`

### SVG
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.svg input.musicxml
```

### Batch job (JSON)
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -j job.json
```
job.json format: `[{"in": "input.mscz", "out": ["output.pdf", "output.mp3"]}]`

---

## Input Formats

Verified accepted formats:
- `.musicxml` — **confirmed working** (tested 2026-03-21 with MusicXML 3.1 partwise)
- `.xml` — accepted (MusicXML)
- `.mxl` — compressed MusicXML
- `.mscz` — MuseScore native (compressed)
- `.mscx` — MuseScore native (XML)
- `.mid` / `.midi` — MIDI import
- `.gp`, `.gp4`, `.gp5`, `.gpx` — Guitar Pro

**Important:** `.musicxml` extension is fully supported in MuseScore 4 CLI (this was unreliable in some MuseScore 3 builds).

---

## Exit Codes and Error Handling

- **Exit 0:** Success — output file was created.
- **Non-zero exit:** Failure — check stderr for error message.
- **Qt QML warnings** (e.g., `Invalid QML element name "IconCode"`) are **noise** — they appear on exit 0 and can be ignored. They are internal Qt registration warnings, not errors.

To suppress Qt noise and capture real errors only:
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.pdf input.musicxml 2>&1 | grep -v "qt.qml"
```

To check exit code:
```bash
"/Applications/MuseScore 4.app/Contents/MacOS/mscore" -o output.pdf input.musicxml 2>/dev/null
echo "Exit: $?"
```

---

## MusicXML Notes

- MuseScore 4 uses MusicXML 3.1 partwise format natively
- `.mscz` = ZIP archive containing `.mscx` (XML) + fonts/images
- `.mscx` = uncompressed MuseScore XML (different from MusicXML)
- For score-writer, always generate MusicXML 3.1 (not `.mscx`) and pass it directly via CLI
- `<divisions>4</divisions>` is a reliable base: quarter=4, half=8, whole=16, eighth=2

---

## Known Limitations / Notes

- MuseScore 4 CLI is headless but **does** initialize the Qt graphics stack — first run on a machine may be slow
- No `-q` / `--quiet` flag to suppress Qt warnings — filter stderr with `grep -v "qt.qml"` if needed
- MP3 export requires MuseScore's built-in audio engine; confirmed working on macOS with the installed app
- Score parts export: `-P` flag exports score + parts as separate PDFs
- MuseScore 4 enforces score validation; malformed MusicXML may produce non-zero exit with an error in stderr

---

## Quick Reference

| Goal | Command |
|------|---------|
| Export PDF | `mscore -o out.pdf in.musicxml` |
| Export MP3 | `mscore -o out.mp3 in.musicxml` |
| Export PNG (300 DPI) | `mscore -r 300 -o out.png in.musicxml` |
| Export SVG | `mscore -o out.svg in.musicxml` |
| MP3 with bitrate | `mscore -b 192 -o out.mp3 in.musicxml` |
| Batch job | `mscore -j job.json` |
| Check version | `mscore --version` |
| Get help | `mscore --help` |

`mscore` = `/Applications/MuseScore 4.app/Contents/MacOS/mscore` (alias for brevity above)
