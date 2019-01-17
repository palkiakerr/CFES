#include<cstdio>
#include<cstdlib>

////////// Function Prototypes //////////

int convert(char to_convert);

int readboundary(float tgt[], char src[50]);

/////////////////////////////////////////


int main(int argc, char *argv[]){
	

	// Basic inputs from arguments
	int dimension;
	char filename[50];
	sscanf(argv[1], "%d", &dimension);
	sscanf(argv[2], "%s", filename);



	// Create and fill matrix, readboundary modifies
	// the matrix in-place
	float matrix[dimension*dimension];
	readboundary(matrix, filename);



	for(int x=0;x<(dimension*dimension);x++){

		printf("%.0f ",matrix[x]);

		if(((x+1)%dimension)==0){
			printf("\n");
		}
	}

	printf("\n");

	return 0;

}



int readboundary(float tgt[], char src[50]){

// tgt is array to write values to
// src is the string holding file location


	// Open src and check for bad file
	FILE *fp;
	fp = fopen(src, "r");
	if ( fp == NULL )
    {
        printf("Could not open file\n");
    }


    // Read the file's characters into the tgt array, skipping newlines
    // tgt size must be sufficient (defined outsie this function)
   	char c;
   	int count = 0;
   	
    while(1){
    	c = fgetc(fp);
    	
    	if(c==EOF){break;}
    	if(c=='\n'){continue;}

    	if(c=='.'){tgt[count]=0;}

    	// Shift ASCII table
    	else{tgt[count] = c-48;}

    	count++;

    }

   	// Return sucess
   	return 0;

}
