import os
import time

def welcome_grades():
    print("=======================================================")
    print("||        PENILAIAN PRAKTIKUM SEMESTER GENAP         ||")
    print("=======================================================")
    print('||       Developer by Aliza Nurfitrian [ALL]         ||')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    
def menu():
    welcome_grades()
    
    nama = input("|| Nama Praktikan: ")
    print("-------------------------------------------------------")
    tp = float(input("Nilai (TP): "))
    
    if tp >= 85:
        print("Nilai Akhir (TP): 85")
    elif tp >= 61:
        print("Nilai Akhir (TP): 70")
    elif tp >= 16:
        print("Nilai Akhir (TP): 55")
    else:
        print("Nilai Akhir (TP): 0")
    print("-------------------------------------------------------")
    
    ta = float(input("Nilai (TA): "))
    
    if ta >= 85:
        print("Nilai Akhir (TA): 85")
    elif ta >= 61:
        print("Nilai Akhir (TA): 70")
    elif ta >= 16:
        print("Nilai Akhir (TA): 55")
    else:
        print("Nilai Akhir (TA): 0")
    print("-------------------------------------------------------")
    
    print("=-=-=-=-=-=--=-=-=-=- Nilai Max. 85 -=-=-=-=-=-=-=-=-=-=-")
    d1 = float(input("Nilai Membuat Aplikasi (D1): "))
    d2 = float(input("Nilai Aktif Operasi Alat (D2): "))
    d3 = float(input("Nilai Diskusi Kelompok (D3): "))
    d4 = float(input("Nilai Perancangan Aplikasi (D4): "))
    
    hasil = (d1+d2+d3+d4)
    print("Nilai Jurnal + FITB: ", hasil)
    print("-------------------------------------------------------")
    
    jurnal = float(input("Nilai Mandiri I1: "))
    
    if jurnal >= 85:
        print("Nilai Mandiri Akhir (I1): 85")
    elif jurnal >= 61:
        print("Nilai Mandiri Akhir (I1): 70")
    elif jurnal >= 16:
        print("Nilai Mandiri Akhir (I1): 55")
    else:
        print("Nilai Mandiri Akhir (I1): 0")
    print("-------------------------------------------------------")
    
    analisa = float(input("Nilai (TK) I2: "))
    
    if analisa >= 85:
        print("Nilai Akhir (TK) I2: 85")
    elif analisa >= 61:
        print("Nilai Akhir (TK) I2: 70")
    elif analisa >= 16:
        print("Nilai Akhir (TK) I2: 55")
    else:
        print("Nilai Akhir (TK) I2: 0")
    print("-------------------------------------------------------\n")
    
    print("Proses akumulasi....")
    time.sleep(3)
    print("\nSelesai!!")  
    os.system('pause')
    os.system('cls')
    menu() 

# all function
if __name__ == "__main__":
    menu()