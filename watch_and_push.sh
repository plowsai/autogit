#!/bin/bash

echo "Watching for file changes. Press Ctrl+C to exit."

# Watch for changes in the current directory
inotifywait -m -e close_write --format '%w%f' . | while read MODFILE
do
    echo "File $MODFILE has been modified."
    git add .
    read -r -p "Enter commit message: " commit_message
    git commit -m "$commit_message"
    git push origin main
    echo "Changes pushed to GitHub."
done 