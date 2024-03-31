#!/bin/bash

PATH_DIR="/usr/local/bin"
INSTALL_DIR="$(pwd)" # Use the git clone directory

install() {

  # Create venv
  python -m venv "$INSTALL_DIR/venv" || { echo "Failed to create venv"; exit 1; }

  # Pip install dependencies to the venv
  "$INSTALL_DIR/venv/bin/pip" install pygame pillow || { echo "Failed to pip install necessary libraries"; exit 1; }

  # Make screenshots directory
  if [ ! -d "$INSTALL_DIR/screenshots" ]; then
    mkdir "$INSTALL_DIR/screenshots" || { echo "Failed to create screenshots directory"; exit 1; }
  fi

  # Modify python shebang
  local SCRIPT_PATH="$INSTALL_DIR/meth.py"

  if [ -f "$SCRIPT_PATH" ]; then
    sed -i "1s|^#!/path/to/venv/bin/python$|#!$INSTALL_DIR/venv/bin/python|" "$SCRIPT_PATH" || { echo "Failed to modify shebang"; exit 1; }
    echo "Shebang modified successfully"

    # chmod +x meth.py
    chmod +x "$SCRIPT_PATH" || { echo "Failed to chmod +x the script"; exit 1; }
    echo "Made meth.py executable"

    # symlink meth.py to path
    sudo ln -s "$SCRIPT_PATH" "$PATH_DIR/meth" || { echo "Failed to create symlink"; exit 1; }
    echo "Successfully symlinked $SCRIPT_PATH to $PATH_DIR/meth"

  else
    echo "meth.py not found: $SCRIPT_PATH"
  fi

  # Move meth.desktop
  local DESKTOP_FILE="$INSTALL_DIR/meth.desktop"
  local DEST_DIR="$HOME/.local/share/applications"

  if [ -f "$DESKTOP_FILE" ]; then
    mkdir -p "$DEST_DIR" || { echo "Failed to create directory: $DEST_DIR"; exit 1; }
    mv "$DESKTOP_FILE" "$DEST_DIR" || { echo "Failed to move desktop file"; exit 1; }
    echo "Successfully moved desktop file"

  else
    echo "Desktop file not found: $DESKTOP_FILE"
  fi

  echo "Installation complete!"

}

# Main
install
exit 0