def merge_sort(array):
    if len(array) == 1:
        return array
    n = len(array);
    A = array[:n//2];
    B = array[n//2:];
    
    A = merge_sort(A);
    B = merge_sort(B);
    
    return merge(A,B)



def merge(A,B):
    C=[None]*(len(A)+len(B));
    k, i , j = 0,0,0;
    while(i<=len(A)-1 and j<=len(B)-1):
        if(A[i]<B[j]):
            C[k]=A[i];
            i = i+1;
            k = k+1;
        else:
            C[k]=B[j];
            j = j+1;
            k = k+1;
    while(i<=len(A)-1):
        C[k]=A[i];
        i = i+1;
        k = k+1;
    while(j<=len(B)-1):
        C[k]=B[j];
        j = j+1;
        k = k+1;
    return C;
            
        
    
        
