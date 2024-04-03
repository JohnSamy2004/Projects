#include <stdio.h>
#include <windows.h>

void main()
{
    int pos = 1;
    char ch;

    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    drawbox();
    show_cursor(0);
do{
    SetConsoleTextAttribute(console, 15);
    gotoxy(60, 12); printf("1)Add new record                ");
    gotoxy(60, 13); printf("2)Update new record             ");
    gotoxy(60, 14); printf("3)Delete new record             ");
    gotoxy(60, 15); printf("4)Exit                          ");
    SetConsoleTextAttribute(console, 10);
    gotoxy(60, 16); printf("--------------------------------");
    SetConsoleTextAttribute(console, 1);
    gotoxy(60, 17); printf("info about the creator :)");
    gotoxy(60, 18); printf("Name: John Samy");
    gotoxy(60, 19); printf("Age: 19");
    gotoxy(60, 20); printf("Hobby: Programming\n");

    switch(pos)
    {
        case 1:
            SetConsoleTextAttribute(console, 240);
                gotoxy(60, 12); printf("1)Add new record                ");
            break;
        case 2:
            SetConsoleTextAttribute(console, 240);
                gotoxy(60, 13); printf("2)Update new record             ");
            break;
        case 3:
            SetConsoleTextAttribute(console, 240);
                gotoxy(60, 14); printf("3)Delete new record             ");
            break;
        case 4:
            SetConsoleTextAttribute(console, 240);
                gotoxy(60, 15); printf("4)Exit                          ");
            break;
    }
    ch = getch();
    if (ch == -32)ch = getch();
    if (ch == 72 || ch == 77){pos--; if (pos == 0) pos = 4;}
    else if (ch == 80 || ch == 75){pos++; if (pos == 5) pos = 1;}
        }
    while (ch != 13 || pos != 4);
    exit;
}

void gotoxy(int x, int y)
{
    COORD c = {0, 0};
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),c);
}

void drawbox(void)
{
    int i;
    gotoxy(59, 11);printf("%c", 201);
    for (i = 1; i < 33; i++)printf("%c", 205);
    printf("%c", 187);

    gotoxy(59, 12);printf("%c", 186);
    for (i= 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 13);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 14);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 15);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 16);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 17);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 18);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 19);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 20);printf("%c", 186);
    for (i = 1; i < 33; i++)printf("%c", 32);
    printf("%c", 186);

    gotoxy(59, 21); printf("%c", 200);
    for (i = 1; i < 33; i++) printf("%c", 205);
    printf("%c", 188);
}

void show_cursor(int flag)
{
    HANDLE out = GetStdHandle(STD_OUTPUT_HANDLE);

    CONSOLE_CURSOR_INFO info;
    GetConsoleCursorInfo(out, &info);
    info.bVisible = flag;
    SetConsoleCursorInfo(out, &info);
}
