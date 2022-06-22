- Versión: wsl --set-version Ubuntu 2

- Comandos empleados:

```sh
top -b -d10 -n360 | grep -i "Cpu(s):" >%CPU.txt
vmstat 15 240 >VmstatMem.txt
awk '{print $numcol}' nombreFichero.txt > NombreGuardarFichero.txt
sysbench --test=cpu --cpu-max-prime=10000 --num-threads=4 run
time stress-ng --cpu 8 --cpu-ops=1000 --log-file nombreFich.txt
time top -b -d30 -n180 | grep -i "MiB Mem\|%CPU(s):" > nombreFich.txt
time sysbench cpu --cpu-max-prime=50000 --time=0 --threads=6 --max-requests=50000 run
```
