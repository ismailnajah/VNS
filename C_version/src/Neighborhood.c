#include "Headers/Data.h"
 
#define MAX_NO_IMPROV 100   //500
#define MAX_NO_IMPROV_LS 50 //250

//number of neighborhoods structures
#define K_MAX 4

//set of neighborhoods structurs
void (*neighborhood[K_MAX])(Vector);

void N_Swap(Vector policy){
    int n = policy->size;
    for(int k=0;k<10;k++){
        int i=rand()%n;
        int j=rand()%n;
        while(i==j)
            j=rand()%n;
        
        swap(policy->get+i,policy->get+j);
    }
}    

void N_Reverse(Vector policy){
    int n = (int)(policy->size/2);
    int s = rand()%n;
    int e = s+3+rand()%(policy->size-s-3);
    for(int i=s+1,j=e-1;i<j;i++,j--){
        swap(policy->get+i,policy->get+j);
    }
    
}

void N_Traspose(Vector policy){
    int n = (int)(policy->size/2);
    int s = rand()%n;
    int k = rand()%10;
    int j=0;
    while(j<k){
        swap(policy->get+s,policy->get+s+1);
        s=(s+2)%policy->size;
        j++;
    }
}

void N_Insert(Vector policy){
    int n = (int)(policy->size/2);
    int k = rand()%10;
    int j = 0;
    while(j<k){
        int s = rand()%n;
        int e = s+2+rand()%(policy->size-s-2);// vec->size-1
        for(int i=s;i<e;i++){
            swap(policy->get+i,policy->get+i+1);
        }
        j++;
    }

}

Candidate best_neighbor(Candidate best,Data data,void(*neighberhood)(Vector)){
    
    int count = 0;
    do{
        //generate random solution from neighborhood
        Candidate candidate = copy_candidate(best);
        neighberhood(candidate->policy);
        candidate->cost = cost(candidate->policy,data);

        if(candidate->cost < best->cost){
            count=0;
            free_candidate(best);
            best = candidate;
        }else{
            count++;
            free_candidate(candidate);
        }
    }while(count < MAX_NO_IMPROV_LS);
    return best;
}

Candidate local_search_VND(Candidate best,Data data){
    //randomize the order of neighborhoods set to be used in VND
    int *l = random_seq(K_MAX);
    int j=0;

    while(j < K_MAX){
        Candidate candidate = copy_candidate(best);
        candidate = best_neighbor(candidate,data,neighborhood[ l[j] ]);

        if(candidate->cost < best->cost){
            free_candidate(best);
            best = candidate;
            //stay on the same neighborhood
        }else{
            free_candidate(candidate);
            //go to the next neighborhood
            j++;
        }
    }
    free(l);
    return best;
}

Candidate VNS(Data data){
    // initial solution based on LPT(Longest Processing Time)
    Candidate best = new_candidate(data->n);
    init_solution(data, best->policy);
    best->cost = cost(best->policy,data);

    //initialize the set of neighborhoods structurs
    neighborhood[0] = N_Swap;
    neighborhood[1] = N_Reverse;
    neighborhood[2] = N_Traspose;
    neighborhood[3] = N_Insert;

    // stopping condition variables
    int iter1=0,iter2=0,iter3=0;
    int lem = (int)(MAX_NO_IMPROV/2);

    //randomize the order of neighborhoods set
    int *k=random_seq(K_MAX);

    //select the first neighborhood
    int i=0;
    do{
        //generate random solution from neighborhood k[i] (shaking)
        Candidate candidate = copy_candidate(best);
        neighborhood[ k[i] ](candidate->policy);
        candidate->cost = cost(candidate->policy,data);
        
        //VND
        candidate = local_search_VND(candidate,data);
        //-------------------------------------------
        //move or not 
        if(candidate->cost < best->cost){
            free_candidate(best);
            best = candidate;
            printf(" %i \n",best->cost);
            iter2 = 0;
            iter3 = 0;
        }else{
            free_candidate(candidate);
            iter2++;
            iter3++;
        }
        iter1++;
        
        //cycle through all neighborhoods
        i= (i+1)%K_MAX;

    }while(iter2 < MAX_NO_IMPROV && iter1 < MAX_NO_IMPROV);
    free(k);
    
    return best;
}
