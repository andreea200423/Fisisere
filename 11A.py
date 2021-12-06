lista1 = []
note=[]
with open("C:/Users/User/Desktop/studii.txt", "r")as f:
    lista = f.readlines()
    for i in lista:
        lista1.append(i[0:-1])
print("nme", "prenume", "nota", "obiect")
for i in lista1:
    print(i)
    for a in i.split():
        if a.isdigit():
            note.append(int(a))
print("nota medie e: ", sum(note)/len(note))
with open("germana.txt", "w") as g:
    p=[]
    s=0
    g.write("nume "+ "prenume "+ "nota "+  "obiect" + "\n")
    for i in lista1:
        if i[-3:-1]=="an":
            g.write(str(i)+"\n")
            for a in i.split():
                if a.isdigit():
                    z.append(int(a))
    g.write("nota medie a clasei germane e: "+ str(round(sum(p)/len(p), 2)))
with open("engleza.txt", "w") as e:
    v=[]
    s=0
    e.write("nume "+ "prenume "+ "nota "+  "obiectul"+"\n")
    for i in lista1:
        if i[-3:-1]=="ez":
            e.write(str(i)+"\n")
            for a in i.split():
                if a.isdigit():
                    v.append(int(a))
    e.write("nota medie a clasei engleze e: " + str(round(sum(v)/len(v), 2)))

                                    


