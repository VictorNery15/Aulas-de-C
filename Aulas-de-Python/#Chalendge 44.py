#Chalendge 44
print(f"\n{" VICTOR SHOPS ":=^40}")
pr = float(input("\nHow much does your product cost?: $"))
pay = str(input("\nWhat will the payment method be?: ")).strip()
pay = pay.lower()
if pay == "dinheiro" or pay == "cheque" or pay == "check" or pay == "money" or pay == "cash" or pay == "pix":
    print(f"\nYou will pay ${pr - (pr * 10/100):.2f} for this product, becuse you are using ''{pay.upper()}'' as the payment method.\nThis entitle you to a 10% of discount.\n")
elif pay == "cartao" or pay == "cartão" or pay == "card" :
    ins = int(input(f"\nHow many installments will you put on the {pay}?: "))
    if ins == 1:
        print(f"\nYou will pay ${pr - (pr * 5/100):.2f} for this product, because you are using your ''CARD'' to pay in a single installment.\nThis entitles you to a 5% of discount.\n")
    elif ins == 2:
        print(f"\nYou will pay ${pr:.2f} in 2 installments of ${pr/2:.2f} for this product.\n")
    elif ins >= 3:
        pri = pr + (pr*20/100)
        print(f"\nYou will pay ${pri:.2f} in {ins} installments of ${pri / ins:.2f} for this product, because you are using your ''CARD'' to pay in three or more installments.\nThis will add 20% interest.\n")
    else:
        print("\nERR ALERT!!\nTry again please!")
else:
    print("\nERR ALERT!!\nThere was a error. Try again and pay attention to the payment method!\n")