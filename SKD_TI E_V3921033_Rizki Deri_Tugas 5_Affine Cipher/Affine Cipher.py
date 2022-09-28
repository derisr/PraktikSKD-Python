#Mencari bilangan yang koprima
def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 

#Menghitung MMI
def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None
  else: 
    return x % m 
 
# enkripsi plaintext
# E = (a*x + b) % 26 
def enkripsi(text, key): 
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ]) 


# dekripsi chipertext
# D(E) = (a^-1 * (E - b)) % 26
def dekripsi(cipher, key): 
  return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ]) 


#form pemilihan menu
def main(): 
    print(" ")
    print("--------------- AFFINE CHIPER ---------------")
    print("1. Enkripsi")
    print("2. Eekripsi")
    print("3. Keluar dari program")
    print("---------------------------------------------")
    menu = input("Masukkan Pilihan Anda : ") 


    if menu == '1': #menu enkripsi
        text = input("Masukkan Plaintext    : ") #masukkan text yang akan di enkripsi
        key = [7, 10]
        enkripsi_text = enkripsi(text,key)
        print('')
        print('Plaintext             : ', text)
        print('Ciphertext            : ', enkripsi_text)
    elif menu == '2': #menu dekripsi
        text = input("Masukkan Ciphertext   : ") #masukkan text yang akan di dekripsi
        key = [7, 10]
        dekripsi_text = dekripsi(text,key)
        print('')
        print('Ciphertext            : ', text)
        print('Plaintext             : ', dekripsi_text)
    elif menu == "3": #menu keluar
        exit()
    else: #jika input salah / tidak tersedia dalam pilihan
        print("Pilihan yang anda masukkan tidak tersedia")
    
    print(" ")


if __name__ == '__main__': 
  main() 