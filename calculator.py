def calculate(n1, process, n2):
    if process == "+":
        return n1 + n2
    elif process == "-":
        return n1 - n2
    elif process == "*":
        return n1 * n2
    elif process == "/":
        return n1 / n2
    else:
        return None
    
while True:

    lang = input("Choose your language (EN/TR), Dilini seç (TR/EN): ").lower()

    if lang not in ("tr","en"):
        print("Choose right language, Doğru dili seç.")
        continue

    while True:

        try:
            if lang == "tr":
                n1 = float(input("İlk sayıyı gir: "))
                process = input("İşlemini seç (+,-,*,/): ")
                n2 = float(input("İkinci sayıyı gir: "))
            else:
                n1 = float(input("Enter your first number: "))
                process = input("Choose your process (+,-,*,/): ")
                n2 = float(input("Enter your second number: "))

            result = calculate(n1, process, n2)

            if result is None:
                print("Yanlış işlemi seçtin." if lang=="tr" else "Wrong process.")
                continue

            print(f"{n1} {process} {n2} = {result:.2f}")
            break
            
        except ValueError:
            print("Sayı girip tekrar dene." if lang=="tr" else "Enter a valid number and try again.")
            continue
        except ZeroDivisionError:
            print("Bir sayıyı sıfıra bölemezsin tekrar dene" if lang=="tr" else "You cannot divide by zero try again.")
            continue

    break