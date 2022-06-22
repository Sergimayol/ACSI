- Versión: wsl --set-version Ubuntu 2

- Comandos empleados:

```sh
top -b -d10 -n360 | grep -i "Cpu(s):" >%CPU.txt
vmstat 15 240 >VmstatMem.txt
awk '{print $numcol}' nombreFichero.txt > NombreGuardarFichero.txt
```
