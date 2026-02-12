#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(int argc, char const *argv[]) {
    if (argc < 3) return 1; // نحتاج IP ورقم المنفذ

    const char* ip = argv[1];
    int port = std::stoi(argv[2]);

    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) return 1;

    struct sockaddr_in serv_addr;
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    

    // تحويل العنوان من نص إلى صيغة ثنائية
    if (inet_pton(AF_INET, ip, &serv_addr.sin_addr) <= 0) return 1;

    // محاولة الاتصال (Timeout قصير جداً للسرعة)
    struct timeval tv;
    tv.tv_sec = 1; // ثانية واحدة كحد أقصى
    tv.tv_usec = 0;
    setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (const char*)&tv, sizeof tv);

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        std::cout << "CLOSED" << std::endl;
    } else {
        std::cout << "OPEN" << std::endl;
    }

    close(sock);
    return 0;
}