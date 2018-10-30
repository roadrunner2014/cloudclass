# cloud class homework

# under /home/ubuntu/cloudclass/  
git clone https://github.com/roadrunner2014/cloudclass.git 

# single processor calculation for area under function
python trapSerial.py 1.0 5.0 100000

# Parallelized version to calculate area under the function
mpiexec --allow-run-as-root -n 10 python trapParallelize-1.py 1.0 5.0 100000
