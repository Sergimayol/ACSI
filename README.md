# ACSI
 
wsl --set-version Ubuntu 2
CP_p2:
- Programas para pasar los datos obtenidos del monitor top y vmstat a excel
cd /mnt/c/Users/Sergi/Desktop/Ubuntu-ACSI
top -b -d10 -n360 | grep -i "Cpu(s):" >%CPU.txt
vmstat 15 240 >VmstatMem.txt
cat /proc/cpuinfo ==> visualizar info especifica de cada una de las cpus
lscpu ==> visualizar info de las cpus
lshw ==> visualizar info del sistema, apartado memory>size ==> Capcidad memoria
awk '{print $numcol}' nombreFichero.txt > NombreGuardarFichero.txt
