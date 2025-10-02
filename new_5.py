import subprocess


cmd = "date"
returned_output = subprocess.check_output(cmd)
print('Результат выполнения команды:', returned_output.decode("utf-8"))