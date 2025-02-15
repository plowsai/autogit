#!/bin/bash

echo "Press Enter to push changes to GitHub. Press Ctrl+C to exit."

while true; do
    read -r -p ""  # Wait for Enter key press
    git add .
    read -r -p "Enter commit message: " commit_message
    git commit -m "$commit_message"
    git push origin main
    echo "Changes pushed to GitHub. Press Enter to push again."
done 