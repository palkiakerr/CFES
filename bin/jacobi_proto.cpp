#include<cstdio>
#include<cstdlib>
#include <gsl/gsl_linalg.h>
////////// Function Prototypes //////////

int readboundary(double tgt[], char src[50], int boundaryflag[]);

int solve_directmatrix(int dimension, double boundary[], int boundaryflag[]);
int solve_jacobirelax(int dim, double bpass[], int boundaryflag[], int threshold);

/////////////////////////////////////////


int main(int argc, char *argv[]){
	

	// Basic inputs from arguments, matrix size and filename
	int dimension;
	char filename[50];
	sscanf(argv[1], "%d", &dimension);
	sscanf(argv[2], "%s", filename);



	// Create and fill matrix, we use the naming convention for a normal
	// matrix problem i.e. Ax=b
	double b[dimension*dimension];

	// Secondary matrix to hold information on wether or not each entry
	// is a boundary condition and should be skipped in calulation
	int boundaryflag[dimension*dimension];

	// Reads in the file containing the problem
	readboundary(b, filename, boundaryflag);

	// Passes the matrix system (Ax=b) to the solver
	int threshold=5000;
	//solve_directmatrix(dimension, b, boundaryflag);
	solve_jacobirelax(dimension, b, boundaryflag, threshold);


	return 0;
}



int readboundary(double b[], char src[50], int boundaryflag[]){

	// b is the matrix (Ax=b) that holds information about the boundary conditions
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

    	// Read in the problem once character at a time
    	c = fgetc(fp);
    	
    	// Ignore newlines and stop ant the end of the file
    	if(c==EOF){break;}
    	if(c=='\n'){continue;}

    	// Remember which zeros and numbers are boundary conditions using a second vector
    	// called boundaryflag
    	if(c=='.'){
    		b[count]=0;
    		boundaryflag[count]=0;
    	}

    	// Shift ASCII table to turn che character for a number into the number itself
    	else{
    		b[count] = c-48;
    		boundaryflag[count] = 1;
    	}

    	count++;

    }

    fclose(fp);

   	// Return sucess
   	return 0;

}


int solve_directmatrix(int dim, double bpass[], int boundaryflag[]){

	// Create/Convert arrays into gsl matrix types
	// Create coefficients array and turn it into a matrix
	gsl_matrix *A = gsl_matrix_alloc(dim*dim,dim*dim);

	// Create b vector from passed array (boundary conditions)
	gsl_vector_view b = gsl_vector_view_array(bpass, dim*dim);

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
	
		
		if(i%dim != 0){
			gsl_matrix_set(A,i,i+1,-1);
		}

		if(i%dim != 1){
			gsl_matrix_set(A,i,i-1,-1);
		}

		if(i>=dim+1){
			gsl_matrix_set(A,i,i-dim,-1);
		}

		if(i<=(dim*dim -dim-1)){
			gsl_matrix_set(A,i,i+dim,-1);
		}
	}




	// Now solve the matrix sysstem Ax=b using LU Decomposition (the
	// direct matrix method)
	int s;

    gsl_permutation * p = gsl_permutation_alloc (dim*dim);

    gsl_linalg_LU_decomp (A, p, &s);

    gsl_linalg_LU_solve (A, p, &b.vector, x);

    gsl_vector_fprintf (stdout, x, "%g");

    gsl_permutation_free (p);
    gsl_vector_free (x);
    return 0;
}


int solve_jacobirelax(int dim, double bpass[], int boundaryflag[], int threshold){

	// Create/Convert arrays into gsl matrix types
	// Create diagonal and non-diagonal matrices for the jacobi method
	gsl_matrix *D = gsl_matrix_alloc(dim*dim,dim*dim);
	gsl_matrix *D_inverse = gsl_matrix_alloc(dim*dim,dim*dim);
	gsl_matrix *R = gsl_matrix_alloc(dim*dim,dim*dim);



	// Create b vector from passed array (boundary conditions)
	gsl_matrix_view b = gsl_matrix_view_array(bpass, dim*dim,1);



	// Now need to create the correct forms of the matrices to solve the problem
	// as the current matrices are empty/garbage data. See p1029 of numerical
	// recipies for what the matrix should look like (tri-diagonal with fringes)
	for(int i = 0; i < (dim*dim); i++){

		if(boundaryflag[i]==1){
			gsl_matrix_set(D,i,i,1);
			continue;
		}
	
		gsl_matrix_set(D,i,i,4);
	
		
		if(i%dim != 0){
			gsl_matrix_set(R,i,i+1,-1);
		}

		if(i%dim != 1){
			gsl_matrix_set(R,i,i-1,-1);
		}

		if(i>=dim+1){
			gsl_matrix_set(R,i,i-dim,-1);
		}

		if(i<=(dim*dim -dim-1)){
			gsl_matrix_set(R,i,i+dim,-1);
		}
	}




	// Now setup the inital guess matrix x_0 to be all zeros
	// x_0 is previous iteration and x_1 is current iteration
	gsl_matrix *x_0 = gsl_matrix_calloc(dim*dim,1);
	gsl_matrix *x_1 = gsl_matrix_alloc(dim*dim,1);

	int s;
    gsl_permutation * p = gsl_permutation_alloc(dim*dim);
    gsl_linalg_LU_decomp (D, p, &s);
    gsl_linalg_LU_invert(D, p, D_inverse);
    gsl_matrix_free (D);


    for(int i=0; i< threshold;i++){

    	// Perform R*x_0 using x_1 as an intermediary
    	gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1, R, x_0, 0, x_1);

    	// Perform Subtraction, result stored in b
    	gsl_matrix_sub(&b.matrix, x_1);

    	// Perform Final Matrix Mul
    	gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1, D_inverse, &b.matrix, 0, x_1);

    	gsl_matrix_memcpy(x_0,x_1);

    }

    gsl_matrix_fprintf (stdout, x_0, "%f");

    gsl_permutation_free (p);
    return 0;
}