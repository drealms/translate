import subprocess
while True:
    inp = input('to english \n')
    with open('/home/ubuntu/ruwords', 'a') as file_object:
        file_object.write(inp + '\n')
    process = subprocess.Popen(['trans','-verbose','-s','ru','-t','en'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    process.stdin.write(inp)
    process.stdin.close()
    outcome = process.stdout.read()
    print(outcome)
