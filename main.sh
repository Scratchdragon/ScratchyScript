sudo apt-get install python3 || echo "python3 installed already or user without sudo permision"
sudo apt-get install g++ || echo "g++ installed already or user without sudo permision"
clear
chmod a+x src/compiler.py
./src/compiler.py
g++ -o run run.cpp; //rm run.cpp; chmod +x run