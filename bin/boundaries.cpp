// WIP, Maintainer: Kerr Maxwell
#include "boundaries.h"
//will need to include ifstream to read from files either here or earlier

int readboundary(int *tgt, char src[50]){

// tgt is array to write values to
// src is the string holding file location


	// Open src and check for bad file
	FILE *fp;
	fp = fopen(src, "r");
	if ( fp == NULL )
    {
        printf( "Could not open file %s", src);
        return 1;
    }


    // Read the file's characters into the tgt array, skipping newlines
   	char c;
   	int count = 1;
    while ((c = getc(fin)) != EOF) {
   	     if (c != '\n'){
   	     	tgt[count]=c;
   	    }
   	    count++;
   	}


   	// Returns a pointer to the filled vector
   	return tgt;

}
