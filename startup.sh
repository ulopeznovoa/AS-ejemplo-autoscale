sudo apt update
sudo apt install -y python3-pip git
sudo pip3 install flask
git clone https://github.com/ulopeznovoa/AS-ejemplo-autoscale.git
sudo python3 AS-ejemplo-autoscale/server.py &
