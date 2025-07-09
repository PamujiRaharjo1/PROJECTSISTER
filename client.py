import socket

def connect_to_server(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(("127.0.0.1", port))
        print(f"Terhubung ke server di port {port}!\n")

        while True:
            response = client.recv(1024).decode()
            print(response)

            if "Pilihan:" in response:
                choice = input("Masukkan pilihan: ")
                client.send(choice.encode())

                if choice == "1" and port == 5555:  # Mendaftar mata kuliah
                    name = input("Masukkan Nama Anda: ")
                    client.send(name.encode())

                    course_code = input("Masukkan Kode Mata Kuliah: ")
                    client.send(course_code.encode())

                if choice == "2":  # Keluar
                    print("Keluar dari sistem.")
                    break

    except ConnectionRefusedError:
        print(f"Gagal terhubung ke server di port {port}! Pastikan server berjalan.")

    client.close()

if __name__ == "__main__":
    while True:
        print("\nAyo Pilih!!:")
        print("1. Pendaftaran Matakuliah ")
        print("2. Daftar Mahasiswa")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            connect_to_server(5555)
        elif pilihan == "2":
            connect_to_server(5556)
        elif pilihan == "3":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid!")
