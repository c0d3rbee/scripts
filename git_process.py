import subprocess
import os

def clone_repo(url, dest_dir, branch="main"):
    try:
        subprocess.run(['git', 'clone', '-b', branch, url, dest_dir], check=True)
        print(f"Cloned repository: {url} (branch: {branch})")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {url} (branch: {branch})\n{e}")
        return False

def run_maven_command(command, dir):
    try:
        subprocess.run(['mvn', command], cwd=dir, check=True)
        print(f"Maven command '{command}' executed successfully in {dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing Maven command '{command}' in {dir}\n{e}")
        return False

def main():
    with open('repo_urls.txt', 'r') as f:
        for line in f:
            url, branch = line.strip().split()
            repo_name = url.split('/')[-1].split('.')[0]
            dest_dir = os.path.join('cloned_repos', repo_name)
    
            if clone_repo(url, dest_dir, branch):
                # List of Maven commands to execute
                commands = ['clean', 'compile', 'test', 'package']
    
                for command in commands:
                    if not run_maven_command(command, dest_dir):
                        break  # Stop processing if a command fails

if __name__ == '__main__':
    main()
