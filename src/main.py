from cryptography.fernet import Fernet
import base64
import uuid

def GenerateKey():
    Key = Fernet.generate_key()
    KeyUUID = str(uuid.uuid4())
    with open(f"keys/{KeyUUID}.key","wb") as File:
        File.write(Key)
        File.close()
    return Key,KeyUUID

if __name__ == "__main__":
    DefaultUUID = ""
    print("[INFO]: Initalizing")
    while True:
        Mode = input("[INPUT][E|D] Enter Mode: ").lower()
        if Mode == "e":
            print("[INFO]: Selected Encryption")
            Key,EncryptUUID = GenerateKey()
            K = Fernet(Key)
            InputString = input("[INPUT][TYPE:STR] Text: ")
            Tokens = K.encrypt(InputString.encode())
            Tokens = base64.b64encode(Tokens)
            with open(f"tokens/{EncryptUUID}.bin","wb") as File:
                File.write(Tokens)
                File.close()
            print("[INFO]: Tokens Encrypted")
            print(f"[INFO]: Output UUID")
            print(EncryptUUID)
            DefaultUUID = EncryptUUID
        elif Mode == "d":
            print("[INFO]: Selected Decryption")
            EncryptUUID = input("[INPUT][TYPE:STR] UUID: ")
            if EncryptUUID == "":
                EncryptUUID = DefaultUUID
            try:
                with open(f"keys/{EncryptUUID}.key","rb") as File:
                    KeyContents = File.read()
                    File.close()
                with open(f"tokens/{EncryptUUID}.bin","rb") as File:
                    Tokens = File.read()
                    File.close()
                Tokens = base64.b64decode(Tokens)
                K = Fernet(KeyContents)
                Text = K.decrypt(Tokens)
                print("[INFO]: Decrypted")
                with open(f"tokens/{EncryptUUID}.txt","w") as File:
                    File.write(Text.decode())
                    File.close()
            except Exception as Error:
                print("[ERROR]: Check your uuid, or add the files into /keys and /tokens")
                print(Error)
        else:
            print("[WARN]: Invalid Mode")