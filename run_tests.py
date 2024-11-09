import subprocess

result = subprocess.run(['python', '-m','test.test_class'], capture_output=True, text=True)
print(result.stdout)

if result.stderr:
    print("Error:", result.stderr)