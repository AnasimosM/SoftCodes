Auto commit message helper
==========================

This repo includes a small utility that inspects staged changes and generates a conservative suggested commit message.
It's intended as a helper to speed up writing commit messages (you should still review/edit the suggestion).

Files added:

- `auto_commit_message.py` - generator script. Run it to print a suggested message or use `--write <commit-msg-file>` to
  write into git's commit message file.
 - `git-hooks/prepare-commit-msg` - an example Unix-style git hook that calls the script.
 - `git-hooks/prepare-commit-msg.bat` - a Windows batch hook wrapper for cmd.exe.
 - `auto_commit_message.bat` - convenience batch wrapper that runs the generator and copies the suggestion to the clipboard.

Installation (simple)
---------------------

1. Copy the hook into your repository hooks directory.

   For Unix/macOS or Git Bash (POSIX hook):

   On Windows (cmd.exe) you can install the batch wrapper instead:

   ```powershell
   copy git-hooks\prepare-commit-msg.bat .git\hooks\prepare-commit-msg.bat
   copy auto_commit_message.bat .git\hooks\auto_commit_message.bat
   ```

   On Unix/macOS (or Git Bash on Windows):

   ```bash
   mkdir -p .git/hooks
   cp git-hooks/prepare-commit-msg .git/hooks/prepare-commit-msg
   chmod +x .git/hooks/prepare-commit-msg
   ```

2. Ensure Python is available on PATH so the hook can run `python` or `python3` (or adjust the batch to point to your python.exe).

3. Stage changes as usual and run `git commit` (no -m). The hook will populate the initial message. You can then edit it in your editor.

Using with PyCharm
------------------
Two recommended options:

A) Install the git hook in the repository as above. When you use PyCharm's Commit dialog (VCS -> Commit), the hook will
run when Git creates the commit message if you commit via the standard Git flow (without passing a message via
command-line flags). Note: PyCharm may create the message in its own UI; the hook is most reliable when committing via
the integrated Git tooling that ultimately runs the native git commands.

B) Use the script as an External Tool to generate a message and paste it into the PyCharm commit message box (recommended on Windows):

- Settings -> Tools -> External Tools -> Add
- Name: Auto Commit Message
- Program: python (or full path to python.exe)
-- Arguments: $ProjectFileDir$\\auto_commit_message.bat
-- Working directory: $ProjectFileDir$

If you prefer to run Python directly, set Program to the full path of python.exe and Arguments to `$ProjectFileDir$\\auto_commit_message.py`.

When you run this external tool, it will print a suggestion to stdout. You can configure the tool to show the output in
a dialog and copy/paste the suggested message into the commit dialog.

Notes and caveats
-----------------

- The script uses simple heuristics and is intentionally conservative. It will not replace a carefully written message —
  you should always review.
- It only inspects staged changes (`git add`ed). Make sure you stage what you want to include in the commit before using
  this.
 - On Windows, the behavior of hooks depends on how Git and your shell are configured. Use the batch hook (`prepare-commit-msg.bat`)
   for reliable cmd.exe execution, or use the External Tool approach.

Customization ideas
-------------------

- Add language-specific checks (e.g. look for TODO or FIXME markers).
- Integrate with an LLM (requires API keys and network access) to produce more natural summaries.

If you'd like, I can convert the hook into a Windows .bat wrapper or add integration instructions specific to your
PyCharm version.
