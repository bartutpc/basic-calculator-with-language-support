def calculate(n1, p, n2):
    if p == "+":
        return n1 + n2
    elif p == "-":
        return n1 - n2
    elif p == "*":
        return n1 * n2
    elif p == "/":
        return n1 / n2
    else:
        return None
    
while True:

    lang = input("Choose your language (EN/TR), Dilini seç (EN/TR): ").lower().strip().replace(" ", "")

    if lang not in ("tr","en"):
        print("Please choose right language and try again, Lütfen doğru dili seçin ve tekrar deneyin.")
        continue

    while True:
        
        try:

            n1 = float(input("Enter first number: " if lang == "en" else "Birinci sayıyı gir: "))
            p = input("Choose your process (+,-,*,/): " if lang == "en" else "İşleminizi seçiniz (+,-,*,/): ")
            n2 = float(input("Enter second number: " if lang == "en" else "İkinci sayıyı gir: "))

            result = calculate(n1, p, n2)

            if result is None:
                print("Please choose right process and try again." if lang == "en" else "Lütfen doğru işlemi seçin ve tekrar deneyin.")
                continue

            print(f"{n1} {p} {n2} = {result:.2f}")

            while True:

                again = input("Do you want use calculator again? (yes/no): " if lang == "en" else "Hesap makinesini tekrar kullanmak istiyor musunuz? (evet/hayır): ").lower().strip().replace(" ", "")

                if again.lower().strip() in ("yes", "evet"):
                 break               
                 
                elif again.lower().strip() in ("no", "hayır"):
                 exit()

                else:
                 print("Please just answer yes or no and try again." if lang == "en" else "Lütfen sadece evet veya hayır olarak cevap verin ve tekrar deneyin.")
                 continue
            
        except ValueError:
            print("Please enter a valid number and try again" if lang == "en" else "Lütfen geçerli bir sayı girip tekrar deneyiniz.")
            continue
        except ZeroDivisionError:
            print("You cannot divide by zero please try again." if lang == "en" else "Bir sayıyı sıfıra bölemezsin lütfen tekrar deneyin.")
            continue
