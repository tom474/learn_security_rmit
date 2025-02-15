import subprocess


def safe_execute(command, args):
    try:
        # Use a list to pass the command and arguments to avoid shell injection
        result = subprocess.run([command] + args, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


# Example usage
command = "ls"
args = ["-l", "/home/user"]
output = safe_execute(command, args)
print(output)
