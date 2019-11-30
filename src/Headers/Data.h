#ifndef H_DATA
#define H_DATA

#include <stdio.h>
#include <stdlib.h>

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

Data getData(FILE*);
void showData(Data);
void freeData(Data);


#endif
