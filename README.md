# cloud class homework

#under /home/ubuntu/cloudclass/  
git clone https://github.com/roadrunner2014/cloudclass.git 
python trapSerial.py 1.0 5.0 100000   # single processor calculation for area under function
mpiexec --allow-run-as-root -n 10 python trapParallelize-1.py 1.0 5.0 100000
