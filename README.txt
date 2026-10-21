PERSONAL DIARY - README
=======================

Project Overview
----------------
This is a menu-driven personal diary application built using Python.
It allows a user to create, view, search, filter, edit, and delete diary
entries. Entries are stored in a local text file named diary.txt so they
remain available after the program closes.

Features
--------
1. Password protection with a maximum of three attempts.
2. Create diary entries with a date, title, mood, and multi-line text.
3. View saved diary entries.
4. Search entries by keyword (case-insensitive).
5. Filter entries by a date range.
6. Edit an existing entry.
7. Delete an entry after confirmation.
8. Display counts for each mood.
9. Encrypt and decrypt diary text using a Caesar cipher.
10. Store entries persistently in diary.txt.

Requirements
------------
- Python 3
- No external packages are required.
- The project is designed to use Python's built-in features without imports.

Files
-----
- main.py       : Main Python program (use your actual Python filename).
- diary.txt     : Data file created/updated by the application.
- README.txt    : Project information and instructions.
- sample_run.txt: Example console interaction.

How to Run
----------
1. Save your Python code in a file, for example main.py.
2. Open a terminal or command prompt in that folder.
3. Run:
       python main.py
4. Enter the diary password when prompted.
5. Choose an option from the menu and follow the prompts.
6. When writing a diary entry, type END on its own line to finish the text.

Diary Entry Format
------------------
The program stores entries in diary.txt using this structure:

ENTRY
DATE:21-10-2026
TITLE:Example title
MOOD:Happy
TEXT_START
Encrypted diary text goes here
TEXT_END

The diary text is encrypted using a Caesar cipher before it is saved and
decrypted when entries are loaded. The exact saved text will depend on the
entry. The '~' character is used to preserve line breaks in the encrypted
text, if your current write_entry() and read_entries() functions use that
approach.

Important Notes
---------------
- Use the same password in the authentication function that you set in code.
- Keep diary.txt in the same folder as the Python program.
- Existing entries saved before encryption was added may not display correctly
  when the new decryption logic is used. Test with a new entry first.
- A basic Caesar cipher is obfuscation, not strong security. Do not store
  highly sensitive information in this diary.
- Ensure the menu options match your functions. For example, option 7 can
  show mood statistics and option 8 can exit, depending on your menu.

Troubleshooting
---------------
- If no entries appear, confirm diary.txt is in the same folder as the program.
- If encryption/decryption looks incorrect, confirm both functions use the same
  shift value and that write_entry() encrypts text before saving.
- If a function name differs in your code, update the menu call to match it.