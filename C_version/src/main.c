#include "Headers/Data.h"
#define DEFAULT_URL "../c500t3"


int main(){
    srand(time(NULL));


    FILE *file = fopen(DEFAULT_URL,"r");
    error_handler(file,"main");
    
    Data data = get_data(file);
    Candidate best = VNS(data);
    show_candidate(best);
    free_candidate(best);
    
    free_data(data);
    fclose(file);
    return 0;
}



