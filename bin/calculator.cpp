#include<cstdio>
#include<cstdlib>
#include <gsl/gsl_linalg.h>
////////// Function Prototypes //////////

int readboundary(double tgt[], char src[50], int boundaryflag[]);

int solve(int dimension, double boundary[], int boundaryflag[]);

/////////////////////////////////////////


int main(int argc, char *argv[]){
	

	// Basic inputs from arguments
	int dimension;
	char filename[50];
	sscanf(argv[1], "%d", &dimension);
	sscanf(argv[2], "%s", filename);



	// Create and fill matrix, readboundary modifies
	// the matrix in-place
	double matrix[dimension*dimension];
	int boundaryflag[dimension*dimension];
	readboundary(matrix, filename, boundaryflag);


/*
	for(int x=0;x<(dimension*dimension);x++){

		printf("%.0f ",matrix[x]);

		if(((x+1)%dimension)==0){
			printf("\n");
		}
	}

	printf("\n");
*/

	solve(dimension, matrix, boundaryflag);
	return 0;

}



int readboundary(double tgt[], char src[50], int boundaryflag[]){

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

    	// Remember what zeros and number are boundaries using a second vector
    	// called boundaryflag
    	if(c=='.'){
    		tgt[count]=0;
    		boundaryflag[count]=0;
    	}

    	// Shift ASCII table
    	else{
    		tgt[count] = c-48;
    		boundaryflag[count] = 1;
    	}

    	count++;

    }

   	// Return sucess
   	return 0;

}


int solve(int dim, double variables[], int boundaryflag[]){

	// Create/Convert arrays into gsl matrix types
	// Create coefficients array and turn it into a matrix
	gsl_matrix *A = gsl_matrix_alloc(dim*dim,dim*dim);

	// Create b vector from passed array (boundary conditions)
	gsl_vector_view b = gsl_vector_view_array(variables, dim*dim);

	// Create empty "x" vector
	gsl_vector *x = gsl_vector_alloc(dim*dim);


	// Now need to create the correct forms of the matrices to solve the problem
	// as the current matrices are empty/garbage data. See p1029 of numerical
	// recipies for what the matrix should look like (tri-diagonal with fringes)
	for(int i = 0; i < (dim*dim); i++){

		if(boundaryflag[i]==1){
			gsl_matrix_set(A,i,i,1);
			continue;
		}
	
		gsl_matrix_set(A,i,i,4);
	
		
		if(i!=dim*dim-1){
			gsl_matrix_set(A,i,i+1,-1);
		}

		if(i!=0){
			gsl_matrix_set(A,i,i-1,-1);
		}

		if(i>=dim+1){
			gsl_matrix_set(A,i,i-dim,-1);
		}

		if(i<=(dim*dim -dim-1)){
			gsl_matrix_set(A,i,i+dim,-1);
		}
	}


	FILE *fp;
	fp = fopen("out.txt", "w");
	gsl_matrix_fprintf(fp,A,"%f");



	int s;

    gsl_permutation * p = gsl_permutation_alloc (dim*dim);

    gsl_linalg_LU_decomp (A, p, &s);

    gsl_linalg_LU_solve (A, p, &b.vector, x);

    gsl_vector_fprintf (stdout, x, "%g");

    gsl_permutation_free (p);
    gsl_vector_free (x);
    return 0;
 
}