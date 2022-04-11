sysbench --test=cpu --cpu-max-prime=10000 --num-threads=4 run
time stress-ng --cpu 8 --cpu-ops=1000
