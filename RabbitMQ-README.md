# Step 1 – Install Erlang
# First, use the following commands to add erlang apt repository on your system. You can simply download erlang repository package from its official website and install on your system.
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
sudo dpkg -i erlang-solutions_1.0_all.deb
# Now, you can install erlang package on your system using the following command. This will install all of its dependencies as well.
sudo apt-get update
sudo apt-get install erlang erlang-nox
# Step 2 – Install RabbitMQ Server
# After installing requirements, now enable RabbitMQ apt repository on your system. Also you need to import rabbitmq signing key on your system. Use the following commands to do this.
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
# After that update apt cache and install RabbitMQ server on your system.
sudo apt-get update
sudo apt-get install rabbitmq-server
# Step 3 – Manage RabbitMQ Service
# After completing installations, enable the RabbitMQ service on your system. Also, start the RabbitMQ service. Use one the below methods sysvinit for older systems or systemctl for the latest operating system.
# Using Init –
sudo update-rc.d rabbitmq-server defaults
sudo service rabbitmq-server start
sudo service rabbitmq-server stop
# Uisng Systemctl –
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl stop rabbitmq-server
# Step 4 – Create Admin User in RabbitMQ
# By default rabbitmq creates a user named “guest” with password “guest”. You can also create your own administrator account on RabbitMQ server using following commands. Change password with your own password.
sudo rabbitmqctl add_user admin password 
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
# Step 5 – Setup RabbitMQ Web Management Console
# RabbitMQ also provides and web management console for managing the entire RabbitMQ. To enable web management console run following command on your system. The web management console helps you for managing RabbitMQ server.
sudo rabbitmq-plugins enable rabbitmq_management
# RabbitMQ dashboard starts on port 15672. Access your server on the port to get dashboard. Use the username and password created in step 4

