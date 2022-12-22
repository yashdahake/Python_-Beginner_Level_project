global my_list
my_list = [ ]
while True:

    
    print("       Resturant Billing system   ")
    print("      #########################  ")
    print(" ----------------------------------- ")
    print("      FOOD MENU AND OTHER OPTIONS          ")#display text
    print(" -------------------------------------- ")
    print('''MENU CARD
            Food Item List
                 1.drinks
                 2.snacks
                 3.Thalis
                 4.Chinese
                 5.Exit
                 6.Display''')#display menu
    print("-----------------------------------------")
    # print(my_list) 
    menu_element=(input("ENTER NUMBER :"))
    
 
    
    def drinks():#function for drinks

            print("--------------drink list------------------")
            print('''
                    a.tea---15rs
                    b.coffee---20rs
                    c.lemon tea---15rs
                    d.black tea---10rs
                    ''')
            print("-------------------------------------------")
            #elements with price
            tea=15
            coffee=20
            lemontea=15
            blacktea=10
             
            while True:
                print('''
                         @--add_Item
                         #--order done
                         ''')
                process=input("add item or order done :")
                if(process=="@" or process=="add item" or process=="add" or process=="ADD ITEM"):
                    select_drinks=input("choice Your drinks :")
                    if(select_drinks=="a" or select_drinks=='tea' or select_drinks=="TEA" ):
                        my_list.append(tea)# print(my_list)  

                    elif(select_drinks=="b" or select_drinks=="coffee" or select_drinks=="COFFEE" or select_drinks=="B"):
                        my_list.append(coffee)
                    elif(select_drinks=="c" or select_drinks=="lemon tea" or select_drinks=="LEMON TEA" or select_drinks=="C"):
                         my_list.append(lemontea)
                    elif(select_drinks=="d" or select_drinks=="black tea" or select_drinks=="BLACK TEA" or select_drinks=="D"):
                        my_list.append(blacktea)
                    print(my_list)      
                        

                else:
                    break
                # def append_to_list(my_list, element):

                #     my_list.append(select_drinks)
                #     append_to_list(my_list, select_drinks)
                #     print(my_list)  
                
              

    #function for snacks
    def snacks():
        print("--------------------snacks list-----------------------")
        print('''
                 a.samosa---25rs
                 b.kachori---25rs
                 c.bread pakoda---25rs
                 d.Alo bonda---25rs
                 e.idlii---30rs
                 f.sambar vada---35rs
                 g.sambar samosa---35rs
                 h.plain dosa---45rs
                 i.masala dosa---60rs
                 ''')
        print("--------------------------------------------------------")
        somosa=25
        kachori=25
        bread_pakoda=25
        Alo_bonda=25
        Idlli=30
        sambar_vada=35
        sambar_somosa=35
        plain_dosa=45
        masala_dosa=60

        while True:
            print('''   
                        @--add_Item
                        #--order done
                        ''')
            process=input("add item or order done :")
            if(process=="@" or process=="add item" or process=="add" or process=="ADD ITEM"):
                    select_snacks=input("choice Your snacks :")
                    if(select_snacks=="a" or select_snacks=="somosa" or select_snacks=="SOMOSA" or select_snacks=="A"):
                        my_list.append(somosa)
                    elif(select_snacks=="b" or select_snacks=="kachori" or select_snacks=="KACHORI" or select_snacks=="B"):
                        my_list.append(kachori)
                    elif(select_snacks=="c" or select_snacks=="breadpakoda" or select_snacks=="BREADPAKODA" or select_snacks=="C"):
                        my_list.append(bread_pakoda)
                    elif(select_snacks=="d" or select_snacks=="Alo bonda" or select_snacks==" ALO BONDA" or select_snacks=="D"):
                        my_list.append(Alo_bonda)
                    elif(select_snacks=="e" or select_snacks=="idlii" or select_snacks=="IDLII" or select_snacks=="E"):
                        my_list.append(Idlli)
                    elif(select_snacks=="f" or select_snacks=="sambar somosa" or select_snacks==" SAMBAR SOMOSA" or select_snacks=="F"):
                        my_list.append(sambar_somosa)
                    elif(select_snacks=="g" or select_snacks=="plain dosa" or select_snacks=="PLAIN DOSA" or select_snacks=="G"):
                        my_list.append(plain_dosa)
                    elif(select_snacks=="i" or select_snacks=="masala dosa" or select_snacks=="MASALA DOSA" or select_snacks=="I"):
                        my_list.append(masala_dosa)

            else:
                break





    def thalis():  #function for thalis
        print("-------------------thalis----------------------")
        print(''' a.full thali---150rs
                  b.special thali---200rs
                  c.rice box---100rs''')
        print("------------------------------------------------")
        full_thali=150
        special_thali=200
        rice_box=100
        while True:
            print('''  
                        @--add_Item
                        #--order done
                        ''')
            process=input("add item or order done :")
            if(process=="@" or process=="add item" or process=="add" or process=="ADD ITEM"):
                    select_thalis=input("choice Your thalis :")
                    if(select_thalis=="A" or select_thalis=='a' or select_thalis=="full thali" or select_thalis=="FULL THALI"):
                        my_list.append(full_thali)
                    elif(select_thalis=="b" or select_thalis=="B" or select_thalis=="special thali" or select_thalis=="SPECIAL THALI"):
                        my_list.append(special_thali)
                    elif(select_thalis=="c" or select_thalis=="C" or select_thalis=="rice box" or select_thalis=="RICE BOX"):
                        my_list.append(rice_box)
            else:
                break






    def chinese(): #function for chinese
        print("-----------------------chinese items------------------------")
        print(''' 
                  a.noodles---70rs
                  b.rice---80rs
                  c.manchurian---90rs
                  d.manchurian noodles---100rs
                  e.manchurian rice---100rs
                  f.cocktail rice noodles---120rs
                  ''')
        print("--------------------------------------------------------------")
        noodles=70
        rice=80
        manchurian=90
        manchurian_noodles=100
        manchurian_rice=100
        cocktail_rice_noodles=120

        while True:
            print(''' 
                        @--add_Item
                        #--order done
                        ''')
            process=input("add item or order done :")
            if(process=="@" or process=="add item" or process=="add" or process=="ADD ITEM"):
                    select_chinese=input("choice Your drinks :")
                    if(select_chinese=="a" or select_chinese=="A" or select_chinese=="noodles" or select_chinese=="NOODLES"):
                        my_list.append(noodles)
                    elif(select_chinese=="b" or select_chinese=="B" or select_chinese=="rice" or select_chinese=="RICE"):
                        my_list.append(rice)
                    elif(select_chinese=="c" or select_chinese=="C" or select_chinese=="machurian" or select_chinese=="MANCHURAIN"):
                        my_list.append(manchurian)
                    elif(select_chinese=="d" or select_chinese=="D" or select_chinese=="manchurian noodles" or select_chinese=="MANCHURIAN NOODLES"):
                        my_list.append(manchurian_noodles)
                    elif(select_chinese=="e" or select_chinese=="E" or select_chinese=="manchurian rice" or select_chinese=="MANCHURIAN RICE"):
                        my_list.append(manchurian_rice)
                    elif(select_chinese=="f" or select_chinese=="F" or select_chinese=="cocktail rice noodles" or select_chinese=="NOODLES" or select_chinese=="COCKTAIL RICE NOODLES"):
                        my_list.append(cocktail_rice_noodles)
            else:
                break






    # def display_bill(my_list):
    #     print(my_list)
    
    
    
    
    #executing conditions:------
    if(menu_element=="1" or menu_element=="drinks"):
        drinks()
    elif(menu_element=="2" or menu_element=="snacks"):
        snacks()
    elif(menu_element=="3" or menu_element=="Thalis" ):
        thalis()
    elif(menu_element=="4" or menu_element=="chinese"):
        chinese()
    elif(menu_element=="5" or menu_element=="exit" or menu_element=="EXIT"):
        break
    elif(menu_element=="6" or menu_element=="display"):
        print(my_list)
        print("YOUR TOTAL BILL IS "+str(sum(my_list))+" Rs.")
        print("-------------------------------------")
        print("----------------THANK-YOU------------")
        print("-------------------------------------")

        break


