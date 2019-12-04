#ifndef H_DATA
#define H_DATA

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>


/*
 * this structure will hold all the information recoverd from the files where
 *      n : is the number of orders 
 *      m : is the number of trasportations
 *      duration : is an array of intigers contains the round trips durations 
 *                 from the suplier to the customer
 *      loading : is an array of integers contation the loading duartion of each order
 * 
 */

struct Data{
    int n;
    int m;
    int *duration;
    int *loading;
};
typedef struct Data* Data;

/*
 * structur Vector has an arry of integers and its size
 */
struct Vector{
    int size;
    int *get;
};
typedef struct Vector* Vector;

/*
 *  structur Candidate is a candidate solution for the optimization problem,it has:
 *      cost : value given by the cost function applied on the policy
 *      policy: a Vector structure represents the order of orders
 */
struct Candidate{
    int cost;
    Vector policy;
};
typedef struct Candidate* Candidate;


//data functions
Data get_data(FILE* file);
void show_data(Data data);
void free_data(Data data);

// Variable Neighberhood Search functions
Candidate VNS(Data data);
Candidate local_search_VND(Candidate best, Data data);
int cost(Vector policy,Data data);
void init_solution(Data data, Vector policy);
Candidate best_neighbor(Candidate best, Data data, void(*neighborhood)(Vector));

//Neighborhoods structures
void N_Swap(Vector policy);
void N_Reverse(Vector policy);
void N_Transpose(Vector policy);
void N_Insert(Vector policy);




// Vector operations 
Vector new_vector(int size);
Vector copy_vector(Vector vec);
void free_vector(Vector vec);
void show_vector(Vector vec);

//Candidate operations
Candidate new_candidate(int size);
Candidate copy_candidate(Candidate src);
void free_candidate(Candidate candiate);
void show_candidate(Candidate candidate);

//utility functions
int index_of(Vector vec,int value);
int max(Vector vec);
int min(Vector vec);
void sort(Vector vec);
void swap(int* a,int* b);
int* random_seq(int size);
void error_handler(void* pointer,char* msg);


#endif
