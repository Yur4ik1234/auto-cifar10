myfile = open ("ip.txt","rt")
contents = myfile.readlines()

for line in contents:
    print (line.replace("\n","")+ " ansible_become=yes ansible_ssh_user=adminuser ")