#include "Headers/Data.h"
#define MAX(x,y) ((x)<(y)?(y):(x))

Data get_data(FILE *file){
    Data data = (Data)malloc(sizeof(struct Data));
    error_handler(data,"get_data");
    int n,m;
    fscanf(file,"%i %i",&n,&m);

    data->duration =(int*)malloc(n*sizeof(int));
    error_handler(data->duration,"get_data");

    data->loading = (int*)malloc(n*sizeof(int));
    error_handler(data->loading,"get_data");
    
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

void show_data(Data data){
    printf("### Data loaded ###\n");
    printf(" %i %i \n",data->n,data->m);

    for(int i=0;i<data->n;i++){
        printf(" %i ",data->duration[i]);
    }
    printf("\n");
    for(int i=0;i<data->n;i++){
        printf(" %i ",data->loading[i]);
    }
    printf("\n");

}

void free_data(Data data){
    free(data->duration);
    free(data->loading);
    free(data);
}

// Cost function to evaluate a particulare solution

int cost(Vector policy,Data data){
    Vector m = new_vector(data->m);
    int cost = 0;
    for(int i=0;i < policy->size;i++){

        int index = index_of(m,min(m));
        cost = data->loading[ policy->get[i] ] + MAX(cost,m->get[index]);
        m->get[index] = cost + data->duration[ policy->get[i] ];
    }
    int return_value = max(m);
    free_vector(m);
    return return_value;
}

// generate the initial solution based on LPT(longest processing time)
void init_solution(Data data, Vector policy){
    for( int i=0; i < policy->size; i++){
        policy->get[i] = i;
    }
    int change=1;
    while(change > 0){      
        change = 0;
        for (int i = 0; i < data->n - 1; i++){
            if (data->duration[ policy->get[i] ] < data->duration[ policy->get[i+1] ]){
                int temp = policy->get[i+1];
                policy->get[i+1] = policy->get[i];
                policy->get[i] = temp;
                change++;
            }
        }
    }
}



// Vector functions
Vector new_vector(int size){
    Vector v = (Vector)malloc(sizeof(struct Vector));
    error_handler(v,"new_vector");
    v->get = (int*)calloc(size,sizeof(int));
    error_handler(v->get,"new_vector");
    v->size = size;
    return v;
}

void free_vector(Vector vec){
    free(vec->get);
    free(vec);
}

void show_vector(Vector vec){
    printf("[ ");
    for(int i=0;i<vec->size;i++){
        printf("%i ",vec->get[i]);
        if(i!=vec->size-1)
            printf(",");
    }
    printf("] size : %i\n",vec->size);
}

Vector copy_vector(Vector vec){
    Vector copy = new_vector(vec->size);
    for(int i=0;i<copy->size;i++){
        copy->get[i] = vec->get[i];
    }
    return copy;
}


// Candidate functions
Candidate new_candidate(int size){
    Candidate c = (Candidate)malloc(sizeof(struct Candidate));
    error_handler(c,"new_candidate");
    c->cost = 0;
    c->policy = new_vector(size);
    return c;
}

Candidate copy_candidate(Candidate src){
    Candidate c = (Candidate)malloc(sizeof(struct Candidate));
    error_handler(c,"copy_candidate");
    c->cost = src->cost;
    c->policy = copy_vector(src->policy);
    return c;
}

void copy_candidate_values(Candidate src,Candidate dist){
    free_vector(dist->policy);
    dist->cost = src->cost;
    dist->policy = copy_vector(src->policy);
    free_candidate(src);
}

void show_candidate(Candidate candidate){
    show_vector(candidate->policy);
    printf("C_max =  %i\n",candidate->cost);
}

void free_candidate(Candidate candidate){
    free_vector(candidate->policy);
    free(candidate);
}

//utility functions
int max(Vector vec){
    int value = vec->get[0];
    for(int i=1;i<vec->size;i++){
        if( value < vec->get[i])
            value = vec->get[i];
    }
    return value;
}

int min(Vector vec){
    int value = vec->get[0];
    for(int i=1;i<vec->size;i++){
        if( value > vec->get[i])
            value = vec->get[i];
    }
    return value;
}

int index_of(Vector vec,int value){
    for(int i=0;i < vec->size;i++){
        if(vec->get[i]== value)
            return i;
    }
}

void swap(int *a,int *b){
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int* random_seq(int size){
    int *seq =(int*)calloc(size,sizeof(int));
    error_handler(seq,"random_seq");
    int value,j;
    for(int i=0;i<size;i++){
        do{
            value = rand()%size;
            for(j=0;j<i;j++){
                if(seq[j] == value)
                    break;
            }
        }while(j!=i);
        seq[i] = value;
    }
    return seq;
}

void error_handler(void *pointer,char *msg){
    if(pointer==NULL){
        perror(msg);
        exit(EXIT_FAILURE);
    }
}