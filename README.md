# ACSI
 
wsl --set-version Ubuntu 2
<br/>
CP_p2:
- Programas para pasar los datos obtenidos del monitor top y vmstat a excel

<br/>
cd /mnt/c/Users/Sergi/Desktop/Ubuntu-ACSI<br/>
top -b -d10 -n360 | grep -i "Cpu(s):" >%CPU.txt<br/>
vmstat 15 240 >VmstatMem.txt<br/>
cat /proc/cpuinfo ==> visualizar info especifica de cada una de las cpus<br/>
lscpu ==> visualizar info de las cpus<br/>
lshw ==> visualizar info del sistema, apartado memory>size ==> Capcidad memoria<br/>
awk '{print $numcol}' nombreFichero.txt > NombreGuardarFichero.txt<br/>
