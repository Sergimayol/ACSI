echo "EMPEZANDO LIMPIEZA DATOS"
./main.exe
sed -i 's/,1./,1/g' "output.txt"
echo "LIMPIEZA DATOS FINALIZADA"
