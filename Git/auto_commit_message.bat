@echo off
REM Windows batch wrapper for auto_commit_message.py
REM Usage: run from repository folder or double-click. Copies suggestion to clipboard.

SET SCRIPT_DIR=%~dp0
SET PYTHON=python

REM Temp file for the generated message
SET TMPMSG=%TEMP%\auto_commit_msg.txt

"%PYTHON%" "%SCRIPT_DIR%auto_commit_message.py" > "%TMPMSG%" 2>nul
IF NOT EXIST "%TMPMSG%" (
  echo No staged changes or generator failed.
  EXIT /B 1
)

type "%TMPMSG%" | clip
echo Commit message copied to clipboard. Preview:
type "%TMPMSG%"
EXIT /B 0
