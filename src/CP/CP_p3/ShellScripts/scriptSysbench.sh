#!/bin/bash
read res
echo "---------------------------------"
echo "Apartado 1.2"
echo "BENCHMARK: Sysbench carga = 25000"
for i in $(seq 1 10); do
    #time sysbench cpu --cpu-max-prime=25000 --threads=6 run >>sysbench25k.txt
    time sysbench cpu --cpu-max-prime=25000 --time=0 --threads=6 --max-requests=25000 run >>sysbench25k.txt
done
read res
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 50000"
for i in $(seq 1 10); do
    #time sysbench cpu --cpu-max-prime=50000 --threads=6 run >>sysbench50k.txt
    time sysbench cpu --cpu-max-prime=50000 --time=0 --threads=6 --max-requests=50000 run >>sysbench50k.txt
done
read res
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 100000"
for i in $(seq 1 10); do
    #time sysbench cpu --cpu-max-prime=100000 --threads=6 run >>sysbench100k.txt
    time sysbench cpu --cpu-max-prime=100000 --time=0 --threads=6 --max-requests=100000 run >>sysbench100k.txt
done
read res
echo "---------------------------------"
echo "BENCHMARK: Sysbench carga = 150000"
for i in $(seq 1 10); do
    #time sysbench cpu --cpu-max-prime=150000 --threads=6 run >>sysbench150k.txt
    time sysbench cpu --cpu-max-prime=150000 --time=0 --threads=6 --max-requests=150000 run >>sysbench150k.txt
done
echo "---------------------------------"
