#!/bin/bash
echo "Setup Servidores A y B"
echo "Servidor A:"
for i in $(seq 1 10); do
    time sysbench cpu --cpu-max-prime=250000 --threads=2 run >>ServidorA.txt
done
echo "---------------------------------"
echo "Servidor B:"
for i in $(seq 1 10); do
    time stress-ng --cpu 4 --cpu-ops=300000 --log-file ServidorB.txt
done
echo "---------------------------------"
echo "Apartado 1.2"
echo "BENCHMARK: Sysbench carga = 25000"
time sysbench cpu --cpu-max-prime=25000 --threads=2 run >sysbench25k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 50000"
time sysbench cpu --cpu-max-prime=50000 --threads=2 run >sysbench50k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 100000"
time sysbench cpu --cpu-max-prime=100000 --threads=2 run >sysbench100k.txt
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 150000"
time sysbench cpu --cpu-max-prime=150000 --threads=2 run >sysbench150k.txt
echo "---------------------------------"
#cd /mnt/c/Users/Sergi/Desktop
#cd /media/sf_Compartido/Pract3
