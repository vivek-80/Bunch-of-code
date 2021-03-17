import tkinter as tk
import math as m

root=tk.Tk()

root.geometry("450x300")

enc_var=tk.StringVar()


lm=[]
def remove(string):
    return "".join(string.split())
def encryp(str, k):
	l1=[]
	l2=[]
	en=""
	for i in range(len(str)):
		if i %k == 0:
			sub = str[i:i+k]
			lst = []
			for j in sub:
				lst.append(j)
			l1.extend(lst)
	for i in range(k):
		if i!=0:
			print('',end='')
		for j in range(i,len(l1),k):
			lm.append(l1[j])
	for r in lm:
		en+=r
	lbl.config(text = "Provided Input: "+en)
	if en!='':
		lbl.config(text='')
	
	
def submit():
    s = enc_var.get()
    st= remove(s)
    l=len(st)
    r=m.floor(m.sqrt(l))
    c=m.ceil(m.sqrt(l))
    encryp(st,c)
    enc_var.set("")



msg = tk.Label(root, text = 'Message', font=('calibre',10, 'bold'))



name_entry = tk.Entry(root,textvariable = enc_var, font=('calibre',10,'normal'))


sub_btn= tk.Button(root,text = 'Encrypt', command = submit)


lbl = tk.Label(root, text = "")


msg.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=1,column=1)
lbl.grid(row=2,column=2)




root.mainloop()
