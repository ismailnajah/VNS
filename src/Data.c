#include "Headers/Data.h"


Data getData(FILE *file){
    Data data = (Data)malloc(sizeof(struct Data));
    int n,m;
    fscanf(file,"%i %i",&n,&m);

    data->duration =(int*)malloc(n*sizeof(int));
    data->loading = (int*)malloc(n*sizeof(int));
    
    for (int i=0;i<n;i++){
        fscanf(file,"%i",data->duration+i);
    }

    for (int i=0;i<n;i++){
        fscanf(file,"%i",data->loading+i);
    }
    data->n = n;
    data->m = m;
    return data;
}


void showData(Data d){
    printf("### Data loaded ###\n");
    printf(" %i %i \n",d->n,d->m);

    for(int i=0;i<d->n;i++){
        printf(" %i ",d->duration[i]);
    }
    printf("\n");
    for(int i=0;i<d->n;i++){
        printf(" %i ",d->loading[i]);
    }
    printf("\n");

}

void freeData(Data d){
    free(d->duration);
    free(d->loading);
    free(d);
}