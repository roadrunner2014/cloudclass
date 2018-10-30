# -------- deploy.sh ------------
#!/bin/bash
echo "Welcome to Openstack deploying instance..."
echo ""

echo "Active Deployments"
openstack server list
echo ""

echo "Please enter an instance name"
read INSTANCE_NAME
echo ""

echo "List images"
openstack image list
echo ""

echo "Please select an image from the list"
read IMAGE_NAME
echo ""

echo "List Flavors"
openstack flavor list
echo ""

echo "Please select a Flavor from the list"
read FLAVOR_NAME
echo ""

echo "List Networks"
openstack network list
echo ""

echo "Choose your network"
read NETWORK_LIST
echo ""

echo "Please enter a key name"
read KEY_NAME
openstack keypair create $KEY_NAME > ~/.ssh/$KEY_NAME
chmod 600 ~/.ssh/$KEY_NAME 

#chmod 507 test.txt  
#111 111 111
#101 111 111 
#001 111 111
echo ""
# echo "User can read & write"

openstack server create --key-name $KEY_NAME --image $IMAGE_NAME --flavor $FLAVOR_NAME $INSTANCE_NAME
sleep 5
#FLOATING_IP $(openstack  floating ip create public | grep floating_ip_address) | awk '{print $4}'

#openstack server add floating ip $INSTANCE_NAME "$FLOATING_IP" --insecure
echo "-------------------------------------------------------"
echo " use {$KEY_NAME} for key to access node"
echo "Floating IP is : {$FLOATING_IO}"
echo "-------------------------------------------------------"
echo "ssh -i ~/.ssh/$KEY_NAME username@$FLOATING_IP"
