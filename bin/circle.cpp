#include <cstdlib>
#include <cmath>
#include <cstdio>

int main(int argc, char *argv[]) 
{
    
    // Pass order
    //
    // 1: radius
    // 2: 1=filled, 0=not filled
    // 3: potential of circle
    // 4: x co-ord of center
    // 5: y co-ord of center
    // 6: dimension of problem
    // 7: pointer to map

    int radius;
    sscanf(argv[1],"%d", &radius);

    int filled;
    sscanf(argv[2],"%d", &filled);

    int magnitude;
    sscanf(argv[3],"%d",&magnitude);

    int x,y;
    sscanf(argv[4],"%d", &x);
    sscanf(argv[5],"%d", &y);

    int size;
    sscanf(argv[6],"%d", &size);


    // Pass the file pointer to write to here
    // currently operating on the file structure as an array of characters
    // to preserve the use of . symbol
    FILE *fp;
    fp=fopen("drawtest.txt","a");
    int i=0;
    int j=0;

    // Assume that we are passed the read-in file array
    // dummy defined below
    int map[size][size];



    // Begin drawing the circle

    for (i=0; i<size; i++)
    {
        for (j=0; j<size; j++)
        {
            double distance = sqrt((double)(i-y)*(i-y) + (j-x)*(j-x));
           
            if (distance>radius-0.5 && distance<radius+0.5)
            {
                map[i][j]=magnitude;
            }
            else if(distance < radius + 0.5 && filled==1){
                map[i][j] = magnitude;
            }
            else{
                map[i][j]=0;
            }
        }
    }

    for(int i = 0; i < size; i++){
        for(int j=0; j < size; j++){

            printf("%d",map[i][j]);

        }
        printf("\n");
    }

    fclose(fp);

    return 0;
}