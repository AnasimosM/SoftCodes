@echo off
REM Windows git hook wrapper for prepare-commit-msg
REM Copy this file into .git\hooks\prepare-commit-msg.bat or call it from a shell.

SET REPO_ROOT=%~dp0\..\..
SET REPO_ROOT=%REPO_ROOT:~0,-1%
SET PYTHON=python
SET SCRIPT=%~dp0\..\auto_commit_message.py
SET COMMIT_MSG_FILE=%1

IF "%COMMIT_MSG_FILE%"=="" (
  echo prepare-commit-msg hook requires the commit message file path as first argument.
  EXIT /B 0
)

REM If commit message already contains content, don't overwrite
IF EXIST "%COMMIT_MSG_FILE%" (
  for /f "usebackq delims=" %%a in ("%COMMIT_MSG_FILE%") do (
    set LINE=%%a
    goto :HAS_CONTENT
  )
)
:HAS_CONTENT
IF DEFINED LINE (
  EXIT /B 0
)

"%PYTHON%" "%~dp0\..\auto_commit_message.py" --write "%COMMIT_MSG_FILE%" 2>nul
EXIT /B 0
