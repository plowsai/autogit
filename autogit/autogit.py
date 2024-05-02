import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        self.commit_changes()

    def commit_changes(self):
        try:
            # Add all changes to the staging area
            subprocess.run(['git', 'add', '.'], check=True)
            # Commit the changes
            subprocess.run(['git', 'commit', '-m', 'Automatic commit'], check=True)
            # Push the changes to the remote repository
            subprocess.run(['git', 'push'], check=True)
            print("Changes committed and pushed to GitHub.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    path = '.' # Path to watch, use '.' for current directory
    event_handler = AutoCommitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
