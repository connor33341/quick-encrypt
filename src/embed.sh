cython --embed -3 main.py
timeout 1
gcc -o main main.c $(python3.12-config --embed --includes) $(python3.12-config --embed --libs)