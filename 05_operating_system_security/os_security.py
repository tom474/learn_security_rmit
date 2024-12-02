import subprocess

def safe_execute(command, arguments):
     try:
         # Use a list to pass the command and arguments to avoid shell injection
         result = subprocess.run([command] + arguments, check=True, text=True, capture_output=True)
         return result.stdout
     except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


# Example usage
cmd = "ls"
args = ["-l", "/home/user"]
output = safe_execute(cmd, args)
print(output)
