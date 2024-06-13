# A package is a collection of Python modules bundled together. and packages also have 
# different versions. pandas is a package and it also have different versions such as
# Pandas 0.1.0 , Pandas 0.8.0, Pandas 0.17.0 etc. agar ap koi ek version use kr rhy ho
# or phir ek doosra version a gya to jab ap doosra install kro gy to vo doosra pehly
# valy ko replace kr de ga, agar hm chahty hn k dono versions hmary paas ho to hm ek
# virtual environment bna le gy or us k ander doosra version rakh len gy , isi trah agr
# mazeed bhi usi package ka koi or version chahye to ek or virtual enivironment
# bna kr vo version vha install kr len gy, yani is trah mery pas 3 versions ho gi, 
# ek global computer vala or doosry 2 virtual enivironments valy

# don't use >>> while using power shell, write your commands directly


steps:
1- create folder(say flder1) in file explorer
2- open powershell
3- to open powershell to that folder , write command: cd C:\Users\J11\Downloads\python_venv 
4- create virtual environment by writing this command:  python -m venv myenv(y krty hi
flder1 k ander ek nia folder myenv k name s automatically ban jay ga, yani apki virtual environment ban gi,
by the way, myvenv is name of virtual environment jo k "python_venv" valy folder
 k ander bni h (myenv k naam s))

5- now activate this virtual environment :  myenv\Scripts\activate.ps1 and use myenv\Scripts\activate.bat for terminal
6- ab y virtual environment activate ho gi, yha kuch bhi install kr lo , or yha install
kia gia koi bhi package or us ka koi bhi version global compluter m mojood versions
and packages pr affect nhi kry ga 
---> if i want to install specific version of that package, i can do it like that: pip install pandas==1.4.4(without space)
---> python and powershell are different programming environmments, import python ka kyword h 
or is ko python k ander yani python likh kr enter maro or phir >>> k ander likho
7- to deactivate that virtual environment, type "deactivate" , vo bhi python k baher a Kr 
===>> agar m n is virtual environment k ander pandas "1.4.4" install kia hua h or global
      computer k ander version 1.5.2 h or mujy 1.4.4 ko use krna h to m simple
      is virtual environment ko activate kr lu gi or phir import krny s vhi vala version
      use ho ga yani 1.4.4 hi
==========>>>>>> bry projects jab bnaty hn to us hr project k liye ek alag virtual
                environment hi bnai jati h ta k jo lo bhi us pr kaam kr rhy hn Vo 
                sab hi vhi virtual environemt apny system k ander bnay or packages k ek
                jesy versions hi use kryn
8- agar koi bht bra project h jis m bht saary packages use huy hn or m n vo project
apny dost ko bhejna h to m esa nhi kru gi k saary k saary packages or un k versions page
pr likh kr send kru, m "pip freeze" ko use kru gi, pip freeze ek environmant k ander
jitny bhi packages mojod h un sab ko show krva deta h. m pip freeze ko ek file m ander 
daalu gi yani is trah: pip freeze > requirments.txt  iss sy ek requirments ki file bny
gi jis k ander saary packages or un k versions likhy ho gy
9- ab y .txt ki file ap k dost k pass gi or vo sirf y command pip install -r requirements.txt
run kry ga or us ki virtual environment k ander saaaryyy vo vali packaes install ho
jay gy,,, agar is pip install -r requirements.txt command s error a jay to esy likhna, 
phir error nhi ay ga : python -m pip install -r requirements.txt




# !!!!!!!!!!!!!!!  VIRTUAL ENVIRONMENT IN VS CODE  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if you wanna open your packages installed in virtual environement is vs code or more 
clearly if i speak is that if you wanna open your virtual environment in vs code
then create a folder say "nimra", open it in vs code , make a .py file and then open terminal
of vs code in that folder then create virtual environment in that terminal, when you 
write the command python -m venv my_virtual , then instantly the "my_virtual" folder
will create in your "nimra" folder , it means that "my_virtual" is the name of 
virtual environment that is created in your "nimra" folder, and that's all