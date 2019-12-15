#include "Headers/Data.h"
 
#define MAX_NO_IMPROV 50
#define MAX_NO_IMPROV_LS 25

//number of neighborhoods structures
#define K_MAX 4

//set of neighborhoods structurs
void (*neighborhood[K_MAX])(Candidate,Data);

void N_Swap(Candidate candidate,Data data){
    int n = candidate->policy->size;
    Candidate temp = copy_candidate(candidate);
    for(int i=0;i<n;i++){
        int j=rand()%n;
        while(i==j)
            j=rand()%n;
        swap(temp->policy->get+i,temp->policy->get+j);
        temp->cost = cost(temp->policy,data);

        if(temp->cost < candidate->cost){
            copy_candidate_values(temp,candidate);
            return;
        }
    }
    free_candidate(temp);
}    

void N_Reverse(Candidate candidate,Data data){
    int n = candidate->policy->size;

    for(int i=0;i<n;i++){
        Candidate temp = copy_candidate(candidate);
        int j=i+rand()%(n-i);
        for(int k=i,l=j;k<l;k++,l--){
            swap(temp->policy->get+k,temp->policy->get+l);
        }
        temp->cost = cost(temp->policy,data);
        if(temp->cost<candidate->cost){
            copy_candidate_values(temp,candidate);
            return;
        }else{
            free_candidate(temp);
        }
    }
    
}

void N_Transpose(Candidate candidate,Data data){
    int n = candidate->policy->size;
    Candidate temp = copy_candidate(candidate);
    for(int i=0;i<n-1;i++){
        swap(temp->policy->get+i,temp->policy->get+i+1);
        temp->cost = cost(temp->policy,data);

        if(temp->cost<candidate->cost){
            copy_candidate_values(temp,candidate);
            return;
        }else{
            swap(temp->policy->get+i,temp->policy->get+i+1);
        }
    }
    free_candidate(temp);
}

void N_Insert(Candidate candidate,Data data){
    int n = candidate->policy->size;
    for(int i=0;i<n;i++){
        Candidate temp = copy_candidate(candidate);
        int j=i+rand()%(n-i);
        for(int k=i;k<j;k++){
            swap(temp->policy->get+k,temp->policy->get+k+1);
        }
        temp->cost = cost(temp->policy,data);
        if(temp->cost<candidate->cost){
            copy_candidate_values(temp,candidate);
            return;
        }else{
            free_candidate(temp);
        }
    }
}

Candidate best_neighbor(Candidate best,Data data,void(*neighberhood)(Candidate,Data)){
    
    int count = 0;
    do{
        //generate random solution from neighborhood
        Candidate candidate = copy_candidate(best);
        neighberhood(candidate,data);
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
    neighborhood[2] = N_Transpose;
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
        neighborhood[ k[i] ](candidate,data);
        
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

    }while(iter2 < MAX_NO_IMPROV);
    free(k);
    return best;
}
