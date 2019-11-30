#include "Headers/Data.h"

int main(){
    FILE *file = fopen("test","r");
    Data d = getData(file);
    showData(d);
    freeData(d);
    fclose(file);
    return 0;
}