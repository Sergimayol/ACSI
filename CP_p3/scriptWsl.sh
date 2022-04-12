#!/bin/bash
echo "Setup Servidores A y B"
echo "Servidor A:"
for i in $(seq 1 10); do
    time sysbench cpu --cpu-max-prime=250000 --threads=8 run >>ServidorA.txt
done
echo "---------------------------------"
echo "Servidor B:"
for i in $(seq 1 10); do
    time stress-ng --cpu 8 --cpu-ops=300000
done