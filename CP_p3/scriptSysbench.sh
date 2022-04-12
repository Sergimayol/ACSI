#!/bin/bash
echo "---------------------------------"
echo "Apartado 1.2"
echo "BENCHMARK: Sysbench carga = 25000"
time sysbench cpu --cpu-max-prime=25000 --threads=8 run >sysbench25k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 50000"
time sysbench cpu --cpu-max-prime=50000 --threads=8 run >sysbench50k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 100000"
time sysbench cpu --cpu-max-prime=100000 --threads=8 run >sysbench100k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 150000"
time sysbench cpu --cpu-max-prime=150000 --threads=8 run >sysbench150k.txt
echo "---------------------------------"
#cd /mnt/c/Users/Sergi/Desktop
#cd /media/sf_Compartido/Pract3