# Translate and Speak

Translate and Speak is a Python automation tool for English vocabulary learning. It monitors copied text, translates English words or short phrases into Hebrew, shows a macOS notification, and supports pronunciation-focused learning.

The idea is simple: reduce friction while studying. Instead of opening a translation site each time, the tool reacts to the user's natural clipboard workflow.

## Project Focus

- Clipboard automation
- English-to-Hebrew translation workflow
- Vocabulary learning support
- macOS notification integration
- Small productivity tool built in Python

## Key Features

- Monitors clipboard changes in the background
- Detects copied English text
- Translates short words or phrases into Hebrew
- Displays the translation through a desktop notification
- Copies the translated text back to the clipboard
- Designed for fast vocabulary lookup during reading or studying

## Technical Skills Demonstrated

- Python scripting and automation
- Clipboard event polling with `pyperclip`
- API/library integration for translation
- macOS command-line notification workflow
- Defensive handling of repeated clipboard values
- Building a tool around a real personal productivity need

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| Clipboard | pyperclip |
| Translation | googletrans |
| OS integration | terminal-notifier / subprocess |
| Platform | macOS-oriented workflow |

## How It Works

1. The script continuously checks the clipboard.
2. When new English text is copied, it sends the text for translation.
3. The Hebrew translation is displayed as a notification.
4. The translation is copied back to the clipboard for quick reuse.

## What I Learned

This project helped me practice turning a repetitive manual action into a useful automation. I worked with clipboard state, external libraries, subprocess calls, and user-facing feedback through system notifications.

It also taught me to think about automation from the user's perspective: the best tool is often the one that fits naturally into an existing workflow.

## Status

Personal productivity and vocabulary-learning tool.