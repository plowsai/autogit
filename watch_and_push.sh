#!/bin/bash

echo "Watching for file changes every 5 minutes. Press Ctrl+C to exit."

while true; do
    # Check for changes
    if git diff --quiet; then
        echo "No changes detected."
    else
        echo "Changes detected."
        git add .

        # Get the list of changed files
        changes=$(git diff --cached --name-only | tr '\n' ', ' | sed 's/, $//')

        # Generate a commit message using OpenAI
        commit_message=$(python3 generate_commit_message.py "$changes")

        git commit -m "$commit_message"
        git push origin main
        echo "Changes pushed to GitHub with commit message: $commit_message"
    fi

    # Sleep for 5 minutes
    sleep 300
done 