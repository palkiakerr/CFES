#include <cstdlib>
#include <cmath>
#include <cstdio>

int main(int argc, char *argv[]) 
{
    
    // Pass order
    //
    // 1: x of point 1
    // 2: y of point 1
    //
    // 3: x of point 2
    // 4: y of point 2

    // 5: 1=filled, 0=not filled
    // 6: potential of retangle
    // 7: dimension of problem


    int x1,y1,x2,y2;
    sscanf(argv[1],"%d", &x1);
    sscanf(argv[2],"%d", &y1);
    sscanf(argv[3],"%d", &x2);
    sscanf(argv[4],"%d", &y2);

    int filled;
    sscanf(argv[5],"%d", &filled);

    int magnitude;
    sscanf(argv[6],"%d", &magnitude);

    int size;
    sscanf(argv[7],"%d", &size);

    // Assume that we are passed the read-in file array
    // dummy defined below
    int map[size][size];


    for(int i = 0; i < size; i++){
        for(int j=0; j < size; j++){
            map[i][j]=0;
        }
    }

/////////////////////////////////////////////////
////////// Remove code above this line///////////
/////////////////////////////////////////////////
    // Begin drawing the circle
    int i=0;
    int j=0;

    for (i=0; i<size; i++){

        if(i==y1 || i==y2){

            for(j=0; j<size; j++){

                if(j>=x1 && j <=x2){

                    map[i][j]=magnitude;
                }
            }
        }


        if(i>y1 && i<y2){

            if(filled==0){
                map[i][x1]=magnitude;
                map[i][x2]=magnitude;
            }

            else{
                for(j=0; j<size; j++){
                    if(j>=x1 && j <=x2){
                        map[i][j]=magnitude;
                    }
                }
            }
        }
    }


    for(i = 0; i < size; i++){
        for(j=0; j < size; j++){

            printf("%d",map[i][j]);

        }
        printf("\n");
    }


    return 0;
}