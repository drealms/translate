import subprocess
while True:
    inp = input('to russian /n')
    with open('/home/ubuntu/enwords', 'a') as file_object:
        file_object.write(inp + '\n')
    process = subprocess.Popen(['trans','-s','en','-t','ru'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    process.stdin.write(inp)
    process.stdin.close()
    print(process.stdout.read())
