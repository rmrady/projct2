from tkinter import*
import sqlite3 as sql
from tkinter import messagebox
from tksheet import Sheet

class GUI(Tk):
    '''
     2022 
    '''
    def __init__(self):
        Tk.__init__(self)
        GUI.main(self)
#-------------------------------------------------------------------------------------------------------------------------------------
    def main(self):
        self.geometry("560x450+400+200")
        self.title("Warehousing")
        self.configure(bg = "cadetblue")
    
        self.frm1 =Frame(padx = 48 , pady = 15,bg = "cadetblue")
        self.frm1.place(x = 10 , y = 10)
        self.frm2 =Frame(padx = 48 , pady = 15,bg = "cadetblue")
        self.frm2.place(x = 10 , y = 110)
        
        config = {'master':self.frm1,'bg' : "cadetblue",'font':('Tahoma',10,'bold'), 'relief':'raised','fg':'white','bd':0}
        self.lbl = Label(**config, text = 'Warehousing is the receipt of goods and items from different parts of')
        self.lbl.grid(row = 1 ,column = 1)

        self.lbl1 = Label(**config,text = 'the company or others outside the company and their maintenance')
        self.lbl1.grid(row = 2 ,column = 1)

        self.lbl2 = Label(**config, text = 'in accordance with the rules and principles of warehousing.')
        self.lbl2.grid(row = 3 ,column = 1)

        self.lbl3 = Label(self.frm2,text = ":نام کاربري",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl3.grid(row = 1 ,column = 1, padx =230, pady = 10)
        self.ent1_m = Entry(self.frm2, width = 18 , font =('Tahoma',15,'bold'),justify = RIGHT,bg = "pink", fg ='white', selectborderwidth =3)
        self.ent1_m.grid(row = 2 ,column = 1, padx =230, pady = 10)

        self.lbl4 = Label(self.frm2,text = ":رمز عبور",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl4.grid(row = 3 ,column = 1, padx =230, pady = 10)
        self.ent2_m = Entry(self.frm2, width = 18 , font =('Tahoma',15,'bold'),justify=RIGHT, show = '*', bg = "pink", fg ='white', selectborderwidth =3)
        self.ent2_m.grid(row = 4 ,column = 1, padx =230, pady =10 )

        self.but =Button(self.frm2,command = lambda : GUI.obor(self),text = "بعدي", bd= 4,font =('Tahoma',10,'bold'),bg ="teal",fg ='white',width = 12, height =1)
        self.but.grid(row = 5 ,column = 1, padx =230, pady = 20)

        
    def obor(self):
        self.name = (self.ent1_m .get())
        self.id1= (self.ent2_m.get())
        f=open("rmz.txt", mode="a+",encoding="utf-8")
        if "rmz.txt" == "":
            sum1 = self.name +','+ self.id1
            f.write(sum1)
        else:
            with open("rmz.txt")as f:
                data=f.read()
                data1 = data.split(",")
            if data1[0] == self.name and  data1[1] == self.id1:
                GUI.top1(self)
            
            else:
                messagebox.showinfo("اخطار","نام يا رمز کاربري اشتباه است")
   

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def top1 (self):
        self.top = Toplevel()
        self.top.geometry("560x450+400+200")
        self.top.title("Warehousing")
        self.top.configure(bg = "cadetblue")

        self.frm_top1 =Frame(self.top, padx = 48 , pady = 15,bg = "cadetblue")
        self.frm_top1.place(x = 10 , y = 10)

        self.but1 =Button(self.frm_top1,command = lambda : GUI.list_kala(self),text = "ورود کالا به انبار", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but1.grid(row = 1 ,column = 1, padx =30, pady = 10)

        self.but2 =Button(self.frm_top1,command = lambda : GUI.fak_kharid(self),text = "فاکتور خريد", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but2.grid(row = 1 ,column = 2, padx =30, pady = 10 )

        self.but3 =Button(self.frm_top1,command = lambda : GUI.frosh(self),text = "فروش کالا", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but3.grid(row = 2 ,column = 1, padx =30, pady = 10 )

        self.but4 =Button(self.frm_top1,command = lambda : GUI.fak_frosh(self),text = "فاکتور فروش", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but4.grid(row = 2 ,column = 2, padx =30, pady = 10 )

        self.but5 =Button(self.frm_top1,command = lambda : GUI.sbt_chack(self),text = "ثبت چک", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but5.grid(row = 3 ,column = 1, padx =30, pady = 10 )

        self.but6 =Button(self.frm_top1,command = lambda : GUI.atl_chack(self),text = "اطلاعات چک ها", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but6.grid(row = 3 ,column = 2, padx =30, pady = 10 )

        self.but7 =Button(self.frm_top1,command = lambda : GUI.customer(self),text = "تعريف مشتري", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but7.grid(row = 4 ,column = 1, padx =30, pady = 10 )

        self.but8 =Button(self.frm_top1,command = lambda : GUI.atlat_customer(self),text = "اطلاعات مشتريان", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but8.grid(row = 4 ,column = 2, padx =30, pady = 10 )

        self.but9 =Button(self.frm_top1,command = lambda : GUI.exit(self),text = "خروج", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but9.grid(row = 5 ,column = 1, padx =30, pady = 10 )

        self.but10 =Button(self.frm_top1,command = lambda : GUI.stock(self),text = "موجودي انبار", bd= 10,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 15, height =1)
        self.but10.grid(row = 5 ,column = 2, padx =30, pady = 10 )

        
    def exit(self):
        messagebox.askquestion("خروج","ايا ميخواهيد از برنامه خارج شويد؟؟" )
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def  list_kala(self):
        self.top = Toplevel()
        self.top.geometry("560x450+400+200")
        self.top.title("Warehousing")
        self.top.configure(bg = "cadetblue")
        self.frm1 =Frame(self.top, padx = 48 , pady = 15,bg = "cadetblue")
        self.frm1.place(x = 10 , y = 10)
        self.frm2 =Frame(self.top, padx = 48 , pady = 15,bg = "cadetblue")
        self.frm2.place(x = 10 , y = 390)
        

        lbl1 = Label(self.frm1,text = ":کدکالا",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl1.grid(row = 1 ,column = 1, padx =50, pady = 10)
        self.entl1 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl1.grid(row = 2,column =1 , padx =7, pady =0 )
        
        lbl2 = Label(self.frm1,text = ":قيمت خريد",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl2.grid(row = 3 ,column = 1, padx =50, pady = 10)
        self.entl2 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl2.grid(row = 4,column =1 , padx =7, pady =0 )

        lbl3 = Label(self.frm1,text = ":تاريخ توليد",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl3.grid(row = 5 ,column = 1, padx =50, pady = 10)
        self.entl3 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl3.grid(row = 6,column =1 , padx =7, pady =0 )

        lbl4 = Label(self.frm1,text = ":نوع کالا",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl4.grid(row = 7 ,column = 1, padx =50, pady = 10)
        self.entl4 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl4.grid(row = 8,column =1 , padx =7, pady =0 )
        
        lbl9 = Label(self.frm1,text = ":ادرس کالا در انبار",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl9.grid(row = 9 ,column = 1, padx =50, pady = 10)
        self.entl0 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl0.grid(row = 10,column =1 , padx =7, pady =0 )

        lbl5 = Label(self.frm1,text = ":عنوان",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl5.grid(row = 1 ,column = 0, padx =50, pady = 10)
        self.entl5 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl5.grid(row = 2,column =0 , padx =7, pady =0 )

        lbl6 = Label(self.frm1,text = ":قيمت فروش",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl6.grid(row = 3 ,column = 0, padx =50, pady = 10)
        self.entl6 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl6.grid(row = 4,column =0 , padx =7, pady =0 )

        lbl7 = Label(self.frm1,text = ":تاريخ انقضا",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl7.grid(row = 5 ,column = 0, padx =50, pady = 10)
        self.entl7 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl7.grid(row = 6,column =0 , padx =7, pady =0 )

        lbl8 = Label(self.frm1,text = ":واحدسنجش",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl8.grid(row = 7 ,column = 0, padx =50, pady = 10)
        self.entl8 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl8.grid(row = 8,column =0 , padx =7, pady =0 )

        lbl9 = Label(self.frm1,text = ":موجودي در انبار",bg ="cadetblue", font =('Tahoma',12,'bold'))
        lbl9.grid(row = 9 ,column = 0, padx =50, pady = 10)
        self.entl9 = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.entl9.grid(row = 10,column =0 , padx =7, pady =0 )


        self.but =Button(self.frm2,command = lambda : GUI.get1(self),text = "ثبت اطلاعات", bd= 5,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 20, height =1)
        self.but.grid(row = 1 ,column = 1, padx =127, pady = 3)

    def get1(self):
        data = []
        self.id1 = (self.entl1.get())
        self.pric_kh = (self.entl2.get())
        self.data_t = (self.entl3.get())
        self.type_k = (self.entl4.get())
        self.adress = (self.entl0.get())
        self.name = (self.entl5.get())
        self.pric_ph = (self.entl6.get())
        self.data_n = (self.entl7.get())
        self.unit = (self.entl8.get())
        self.mojod = (self.entl9.get())
        data= [self.id1,self.pric_kh,self.data_t,self.type_k,self.adress,self.name,self.pric_ph,self.data_n,self.unit,self.mojod]
        return GUI.insert1(self,data)

    def table1(self):
        command = '''
                CREATE TABLE T1(id1 INTEGER PRIMERY KEY,
                pric_kh INTEGER,data_t INTEGER,type_k TEXT,
                adress TEXT,name TEXT,pric_ph INTEGER,data_n INTEGER ,
                unit INTEGER ,mojod INTEGER)
                '''
        cur.execute(command)
        con.commit()


    def insert1 (self,data):
        command = '''
              INSERT INTO T1 (id1, pric_kh ,data_t, type_k, adress, name, pric_ph, data_n , unit,mojod )VALUES (?,?,?,?,?,?,?,?,?,?)
              '''
        try :
            cur.execute(command,data)
##            messagebox.showinfo("seve","ذخيره شد")
            
        except:
            print("no!!!")

        else:
            con.commit()
#------------------------------------------------------------------------------------------------------------------------------            
    def  frosh(self):
        self.top = Toplevel()
        self.top.geometry("560x450+400+200")
        self.top.title("Warehousing")
        self.top.configure(bg = "cadetblue")
        self.frm1 =Frame(self.top, padx = 48 , pady = 15,bg = "cadetblue")
        self.frm1.place(x = 10 , y = 10)

        self.lbl1 = Label(self.frm1,text = ":اسم محصول",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl1.grid(row = 1 ,column = 1, padx =1, pady = 10)
        self.ent1_f = Entry(self.frm1, width = 8 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.ent1_f.grid(row = 1,column =0 , padx =1, pady =10 )

        self.lbl2 = Label(self.frm1,text = ":قيمت",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl2.grid(row = 2 ,column = 1, padx =1, pady = 10)
        self.ent2_f = Entry(self.frm1, width = 28 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.ent2_f.grid(row = 2,column =0 , padx =1, pady =10 )

        self.lbl3 = Label(self.frm1,text = ": نوع دسته بندي",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl3.grid(row = 3 ,column = 1, padx =1, pady = 10)
        self.ent3_f = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.ent3_f.grid(row = 3,column =0 , padx =1, pady =10 )

        self.lbl4 = Label(self.frm1,text = ":تعداد درخواستي",bg ="cadetblue", font =('Tahoma',12,'bold'))
        self.lbl4.grid(row = 4 ,column = 1, padx =1, pady = 10)
        self.ent4_f = Entry(self.frm1, width = 5 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
        self.ent4_f.grid(row = 4,column =0 , padx =1, pady =10 )

        self.but =Button(self.frm1,command = lambda : GUI.get2(self),text = "خريد", bd= 5,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 20, height =1)
        self.but.grid(row = 5 ,column = 0, padx =0, pady = 20)

    def get2(self):
        data = []
        self.name = (self.ent1_f.get())
        self.pric = (self.ent2_f.get())
        self.type_k = (self.ent3_f.get())
        self.tada = (self.ent4_f.get())
        data= [self.name,self.pric,self.type_k,self.tada ]
        return GUI.insert2(self,data)

    def table2(self):
        command = '''
                CREATE TABLE T2 (name TEXT,
                pric INTEGER NOT NULL UNIQUE,
                type_k TEXT NOT NULL UNIQUE,
                tada INTEGER NOT NULL UNIQUE)
                '''
        cur.execute(command)
        con.commit()


    def insert2 (self,data):
        command = '''
              INSERT INTO T2 (name, pric, type_k,tada)VALUES (?,?,?,?)
              '''
        try :
            cur.execute(command,data)
        except:
            print("no!!!")

        else:
            con.commit()

##    def showepc(self):
##        self.id1 = (self.ent1_f.get())
##        ta1 =self.ent4_f.get()
##        ta1 = int(ta1)
##        command = 'SELECT * FROM T1 WHERE id1 ={}'.format(self.id1)
##        dat = cur.execute(command)
##        dat = list(dat)
##        tada = (dat[0][9])
##        if tada >= ta1:
##            rezalt = tada - ta1
##            print (rezalt)
##        else:
##            print ("no!")
#-------------------------------------------------------------------------------------------------------------------------------
    def  fak_kharid(self):
        self.top = Toplevel()
        self.top.geometry("560x450+400+200")
        self.top.title("factor")
        self.top.configure(bg = "cadetblue")
        command = 'SELECT * FROM T1 '
        dat = cur.execute(command)
        dat = list(dat)
        i = 0
        lst =[]
        for i in range(len(dat)):
            a = ((dat[i][5]) , (dat[i][3] ), (dat[i][1]) ,(dat[i][9]))
            lst = lst + [a]
          
        self.sheet = Sheet(self.top, data = lst,theme = "dark blue" , headers =["شده خريداري کالا نام", "کالا نوع","خريد قيمت","تعداد" ] ,height= 450, width = 560,align = "center")
        self.sheet.grid(row = 1 ,column = 1, sticky = "nswe")

#--------------------------------------------------------------------------------------------------------------------------------
    def  fak_frosh(self):
         self.top = Toplevel()
         self.top.geometry("560x450+400+200")
         self.top.title("factor")
         self.top.configure(bg = "cadetblue")
         command = 'SELECT * FROM T2 '
         dat = cur.execute(command)
         dat = list(dat)
         self.sheet = Sheet(self.top, data = dat,theme = "dark blue", headers =["شده فروخته کالا نام","کالا نوع", "فروش قيمت","تعداد" ] ,height= 450, width = 560,align = "center")
         self.sheet.grid(row = 2 ,column = 1)
         
#------------------------------------------------------------------------------------------------------------------------

    def sbt_chack(self):
         self.top = Toplevel()
         self.top.geometry("560x450+400+200")
         self.top.title("chack")
         self.top.configure(bg = "cadetblue")
         self.frm1 =Frame(self.top, padx = 5 , pady = 1,bg = "cadetblue")
         self.frm1.place(x = 10 , y = 10)

         self.lbl1 = Label(self.frm1,text = ":شماره سريال چک",bg ="cadetblue", fg ='white', font =('Tahoma',12,'bold'))
         self.lbl1.grid(row = 0 ,column = 2, padx =77, pady = 10)
         self.ent1_s = Entry(self.frm1, width = 10 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent1_s.grid(row = 0,column =1 , padx =7, pady =10 )

         self.lbl2 = Label(self.frm1,text = ":شماره حساب",bg ="cadetblue", fg ='white',font =('Tahoma',12,'bold'))
         self.lbl2.grid(row = 2 ,column = 2, padx =77, pady = 10)
         self.ent2_s = Entry(self.frm1, width = 25 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent2_s.grid(row = 2,column =1 , padx =7, pady =10 )

         self.lbl3 = Label(self.frm1,text = ":نام شعبه",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl3.grid(row = 3 ,column = 2, padx =77, pady = 10)
         self.ent3_s = Entry(self.frm1, width = 15, font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent3_s.grid(row = 3,column =1 , padx =7, pady =10 )

         self.lbl4 = Label(self.frm1,text = ":نام بانک",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl4.grid(row = 4 ,column = 2, padx =77, pady = 10)
         self.ent4_s = Entry(self.frm1, width = 12 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent4_s.grid(row = 4,column =1 , padx =7, pady =10 )

         self.lbl5 = Label(self.frm1,text = ":به نام",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl5.grid(row = 5 ,column = 2, padx =77, pady = 10)
         self.ent5_s = Entry(self.frm1, width = 23 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent5_s.grid(row = 5,column =1 , padx =7, pady =10 )
         
         self.lbl6 = Label(self.frm1,text = ":تاريخ وصول",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl6.grid(row = 6 ,column = 2, padx =77, pady = 10)
         self.ent6_s = Entry(self.frm1, width =10 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent6_s.grid(row = 6,column =1 , padx =7, pady =10 )

         self.lbl7 = Label(self.frm1,text = ":به مبلغ",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl7.grid(row = 7 ,column = 2, padx =77, pady = 10)
         self.ent7_s = Entry(self.frm1, width = 18 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent7_s.grid(row = 7,column =1 , padx =7, pady =10 )



         self.but =Button(self.frm1,command = lambda : GUI.get3(self),text = "ثبت", bd= 5,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 20, height =1)
         self.but.grid(row = 8 ,column = 1, padx =0, pady = 20)
         
    def get3(self):
        data3 = []
        self.sh_chack = (self.ent1_s.get())
        self.sh_hesab = (self.ent2_s.get())
        self.n_shoba = (self.ent3_s.get())
        self.n_bank = (self.ent4_s.get())
        self.name = (self.ent5_s.get())
        self.data= (self.ent6_s.get())
        self.mablagh = (self.ent7_s.get())
        data3= [self.sh_chack,self.sh_hesab,self.n_shoba ,self.n_bank ,self.name,self.data,self.mablagh ]
        return GUI.insert3(self,data3)

         

    def table3(self):
        command = '''
                CREATE TABLE T3(sh_chack INTEGER PRIMERY KEY,
                sh_hesab INTEGER NOT NULL UNIQUE,
                n_shoba TEXT NOT NULL UNIQUE,
                n_bank TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL UNIQUE,
                data INTEGER NOT NULL UNIQUE ,
                mablagh INTEGER NOT NULL UNIQUE )
                '''
        cur.execute(command)
        con.commit()


    def insert3 (self,data):
        command = '''
              INSERT INTO T3 (sh_chack,sh_hesab,n_shoba ,n_bank ,name,data,mablagh )VALUES (?,?,?,?,?,?,?)
              '''
        try :
            cur.execute(command,data)
        except:
            print("no!!!")

        else:
            con.commit()

#---------------------------------------------------------------------------------------------------------------------------         
    def atl_chack(self):
        self.top = Toplevel()
        self.top.geometry("560x450+400+200")
        self.top.title("chack")
        self.top.configure(bg = "cadetblue")
        command = 'SELECT * FROM T3 '
        dat = cur.execute(command)
        dat = list(dat)
        i = 0
        lst =[]
        for i in range(len(dat)):
            a = ((dat[i][0]) , (dat[i][1] ), (dat[i][2]) ,(dat[i][3]), (dat[i][4]), (dat[i][5]), (dat[i][6]))
            lst = lst + [a]
          
        
        self.sheet = Sheet(self.top, data =lst, headers =[": چک سريال شماره",":حساب شماره"," :شعبه نام"," :نام به"," :وصول تاريخ",":مبلغ به"] ,theme = "dark blue",height= 450, width = 560,align = "center")
        self.sheet.grid(row = 1 ,column = 1, sticky = "nswe")

         
#------------------------------------------------------------------------------------------------------------------------------------------------------
    def customer(self):
         self.top = Toplevel()
         self.top.geometry("560x450+400+200")
         self.top.title("customer")
         self.top.configure(bg = "cadetblue")
         self.frm1 =Frame(self.top, padx = 5 , pady = 1,bg = "cadetblue")
         self.frm1.place(x = 10 , y = 10)

         self.lbl0 = Label(self.frm1,text = ":ID",bg ="cadetblue", fg ='white', font =('Tahoma',12,'bold'))
         self.lbl0.grid(row = 0 ,column = 2, padx =77, pady = 10)
         self.ent0_co = Entry(self.frm1, width = 5 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent0_co.grid(row = 0,column =1 , padx =7, pady =10 )

         self.lbl2 = Label(self.frm1,text = ":نام,نام خانوادگي",bg ="cadetblue", fg ='white',font =('Tahoma',12,'bold'))
         self.lbl2.grid(row = 2 ,column = 2, padx =77, pady = 10)
         self.ent2_co = Entry(self.frm1, width = 20 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent2_co.grid(row = 2,column =1 , padx =7, pady =10 )

         self.lbl3 = Label(self.frm1,text = ": شماره ملي",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl3.grid(row = 3 ,column = 2, padx =77, pady = 10)
         self.ent3_co = Entry(self.frm1, width = 15 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent3_co.grid(row = 3,column =1 , padx =7, pady =10 )

         self.lbl4 = Label(self.frm1,text = ":محل سکونت",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl4.grid(row = 4 ,column = 2, padx =77, pady = 10)
         self.ent4_co = Entry(self.frm1, width = 25 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent4_co.grid(row = 4,column =1 , padx =7, pady =10 )

         self.lbl5 = Label(self.frm1,text = ":شماره تماس",bg ="cadetblue",fg ='white', font =('Tahoma',12,'bold'))
         self.lbl5.grid(row = 5 ,column = 2, padx =77, pady = 10)
         self.ent5_co = Entry(self.frm1, width = 15 , font =('Tahoma',14,'bold'),justify=RIGHT, bg = "pink", fg ='black', selectborderwidth =3)
         self.ent5_co.grid(row = 5,column =1 , padx =7, pady =10 )

         self.but =Button(self.frm1,command = lambda : GUI.get4(self),text = "ثبت", bd= 5,font =('Tahoma',12,'bold'),bg ="teal",fg ='white',width = 20, height =1)
         self.but.grid(row = 6 ,column = 1, padx =0, pady = 20)

    def get4(self):
        data4 = []
        self.id1 = (self.ent0_co.get())
        self.last_name = (self.ent2_co.get())
        self.national = (self.ent3_co.get())
        self.adress = (self.ent4_co.get())
        self.number = (self.ent5_co.get())
        data4= [self.id1,self.last_name,self.national,self.adress,self.number]
        return GUI.insert4(self,data4)

         

    def table4(self):
        command = '''
                CREATE TABLE T4 (id1 INTEGER PRIMERY KEY,
                last_name TEXT NOT NULL UNIQUE,
                national INTEGER NOT NULL UNIQUE,
                adress TEXT NOT NULL UNIQUE,
                number INTEGER)
                '''
        cur.execute(command)
        con.commit()


    def insert4 (self,data):
        command = '''
              INSERT INTO T4 (id1,last_name ,national, adress, number)VALUES (?,?,?,?,?)
              '''
        try :
            cur.execute(command,data)
        except:
            print("no!!!")

        else:
            con.commit()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def atlat_customer(self):
         self.top = Toplevel()
         self.top.geometry("560x450+400+200")
         self.top.title("customer")
         self.top.configure(bg = "cadetblue")
         command = 'SELECT * FROM T4 '
         dat = cur.execute(command)
         dat = list(dat)
         i = 0
         lst =[]
         for i in range(len(dat)):
            a = ((dat[i][0]) , (dat[i][1] ), (dat[i][2]) ,(dat[i][3]), (dat[i][4]))
            lst = lst + [a]
            
         self.sheet = Sheet(self.top, data = lst ,theme = "dark blue" , headers =[":ID",":نام",":  ملي شماره",": سکونت محل ",": تماس شماره "] ,height= 450, width = 560,align = "center")
         self.sheet.grid(row = 1 ,column = 1, sticky = "nswe")

         
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
    def stock(self):
         self.top = Toplevel()
         self.top.geometry("560x450+400+200")
         self.top.title("stock")
         self.top.configure(bg = "cadetblue")
##         self.frm =Frame(self.top, padx = 5 , pady = 1,bg = "cadetblue")
##         self.frm.grid(row = 1 ,column = 1, sticky = "nswe")
         command = 'SELECT * FROM T1 '
         dat = cur.execute(command)
         dat = list(dat)
         i = 0
         lst =[]
         for i in range(len(dat)):
            a = ((dat[i][5]), (dat[i][6]), (dat[i][9]), (dat[i][4]))
            lst = lst + [a]
         self.sheet = Sheet(self.top, data = lst ,theme = "dark blue" , headers =[" کالا نام", "قيمت","موجودي","انبار در کالا ادرس" ] ,height= 450, width = 560,align = "center")
         self.sheet.grid(row = 1 ,column = 1, sticky = "nswe")

         

         
   

#-------------------------------------------------------------------------------------------------------------------------------------
con = sql.connect("Wareho.db")
cur = con.cursor()     


obj = GUI()
##obj.table1()
##obj.table2()
##obj.table3()
##obj.table4()
obj.mainloop()
