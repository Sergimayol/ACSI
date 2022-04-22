# ACSI
- Versión: wsl --set-version Ubuntu 2
- Prácticas: 
  - CP_px (x: 1-7)
- Comandos empleados: 
```sh
cd /mnt/c/Users/Sergi/Desktop/Ubuntu-ACSI 
cd /mnt/c/Users/Sergi/Documents/GitHub/ACSI 
top -b -d10 -n360 | grep -i "Cpu(s):" >%CPU.txt 
vmstat 15 240 >VmstatMem.txt 
cat /proc/cpuinfo ==> visualizar info especifica de cada una de las cpus 
lscpu ==> visualizar info de las cpus 
lshw ==> visualizar info del sistema, apartado memory>size ==> Capcidad memoria 
awk '{print $numcol}' nombreFichero.txt > NombreGuardarFichero.txt 
sysbench --test=cpu --cpu-max-prime=10000 --num-threads=4 run 
time stress-ng --cpu 8 --cpu-ops=1000 --log-file nombreFich.txt 
time top -b -d30 -n180 | grep -i "MiB Mem\|%CPU(s):" > nombreFich.txt
```