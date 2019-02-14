#include <gtk/gtk.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
//#include <gsl/gsl_linalg.h>
//#include <gsl/gsl_splinalg.h>

int type;
int dimension;
float matrix[200][200];
FILE *f;

typedef struct {
  GtkWidget *w_comboboxtext_options;
  GtkWidget *w_lbl_sel_text;
  GtkWidget *w_sbtn_quantity;
  GtkWidget *w_btn_matrix;
  GtkWidget *w_lbl_user1;
  GtkWidget *w_lbl_user2;
  GtkWidget *w_lbl_user3;
  GtkWidget *w_lbl_user4;
  GtkWidget *w_lbl_user5;
  GtkWidget *w_lbl_user6;
  GtkWidget *w_sbtn_user1;
  GtkWidget *w_sbtn_user2;
  GtkWidget *w_sbtn_user3;
  GtkWidget *w_sbtn_user4;
  GtkWidget *w_sbtn_user5;
  GtkWidget *w_tbtn_user;
  GtkWidget *w_btn_add_object;
  GtkWidget *w_btn_generate;
} app_widgets;

int main(int argc, char *argv[])
{
    
    GtkBuilder      *builder; 
    GtkWidget       *window;
    app_widgets     *widgets = g_slice_new(app_widgets);

    //initialise GTK builder and window
    gtk_init(&argc, &argv); 
    builder = gtk_builder_new();
    gtk_builder_add_from_file (builder, "window_main.glade", NULL);
    window = GTK_WIDGET(gtk_builder_get_object(builder, "window_main"));

    //initialise widgets
    widgets->w_comboboxtext_options = GTK_WIDGET(gtk_builder_get_object(builder, "comboboxtext_options"));
    widgets->w_lbl_sel_text = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_sel_text"));
    widgets->w_sbtn_quantity = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_quantity"));
    widgets->w_btn_matrix = GTK_WIDGET(gtk_builder_get_object(builder, "btn_matrix"));
    widgets->w_lbl_user1 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user1"));
    widgets->w_lbl_user2 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user2"));
    widgets->w_lbl_user3 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user3"));
    widgets->w_lbl_user4 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user4"));
    widgets->w_lbl_user5 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user5"));
    widgets->w_lbl_user6 = GTK_WIDGET(gtk_builder_get_object(builder, "lbl_user6"));
    widgets->w_sbtn_user1 = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_user1"));
    widgets->w_sbtn_user2 = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_user2"));
    widgets->w_sbtn_user3 = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_user3"));
    widgets->w_sbtn_user4 = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_user4"));
    widgets->w_sbtn_user5 = GTK_WIDGET(gtk_builder_get_object(builder, "sbtn_user5"));
    widgets->w_tbtn_user = GTK_WIDGET(gtk_builder_get_object(builder, "tbtn_user"));
    widgets->w_btn_add_object = GTK_WIDGET(gtk_builder_get_object(builder, "btn_add_object"));
    widgets->w_btn_generate = GTK_WIDGET(gtk_builder_get_object(builder, "btn_generate"));

    //connect builder and signals
    gtk_builder_connect_signals(builder, widgets);
    g_object_unref(builder);
    gtk_widget_show(window);                
    gtk_main();
    g_slice_free(app_widgets, widgets);
 
    return 0;
}
 
// called when window is closed
void on_window_main_destroy()
{
    gtk_main_quit();
}

//Show Option button clicked by user
void on_btn_show_option_clicked(GtkButton *button, app_widgets *app_wdgts) {

  gchar *item_text = 0; //selected item text from text combo box
  int object_type;
 
  //get selected item text from GtkComboBoxText object
  item_text = gtk_combo_box_text_get_active_text(GTK_COMBO_BOX_TEXT(app_wdgts->w_comboboxtext_options));
  if (item_text == NULL) {
    //return if no text found in combo box
    return;
  }
  
  gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_sel_text), item_text);

  //Determines what type of object user is inputting
  if (strcmp(item_text, "Point") == 0) {object_type=1;}
  if (strcmp(item_text, "Rectangle") == 0) {object_type=2;}
  if (strcmp(item_text, "Circle") == 0) {object_type=3;}

  //Requirements for every type of entry
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user1), "Enter x-coordinate:");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user2), "Enter y-coordinate:");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user5), "Enter magnitude of circle (<100,000):");
  
  //Requests the user for inputs corresponding to object types
  switch(object_type) {
  case 1 ://Point
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user3), "N/A");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user4), "N/A:");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user6), "N/A");
   break;
  case 2 : //Rectangle
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user3), "Enter length:");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user4), "Enter height");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user6), "(Optional) Fill the Rectangle?");
   break;
  case 3 : //Circle
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user3), "Enter radius");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user4), "N/A");
   gtk_label_set_text(GTK_LABEL(app_wdgts->w_lbl_user6), "(Optional) Fill the Circle?");
   break;
  } 
  //free up dynamically allocated memory
  g_free(item_text);
  type = object_type;
}

void on_btn_add_object_clicked(GtkButton *button, app_widgets *app_wdgts) {

  int x1,y1,length,height,i,j,filled;
  float radius,magnitude;
  f = fopen("log.txt","a");

    filled=gtk_toggle_button_get_active(GTK_TOGGLE_BUTTON(app_wdgts->w_tbtn_user));
    x1 = gtk_spin_button_get_value_as_int(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user1));
    y1 = gtk_spin_button_get_value_as_int(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user2));
    magnitude = gtk_spin_button_get_value(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user5));
    
  // Matrix values altered according to type of shape
  switch(type) {
  case 1 : //Point
    printf("Point entered: (%d,%d) with magnitude %f\n",x1,y1,magnitude);
    fprintf(f,"Point entered: (%d,%d) with magnitude %f\n",x1,y1,magnitude);
    matrix[x1][y1]=magnitude;
    break;
  
  case 2 : //Rectangle
    length = gtk_spin_button_get_value_as_int(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user3));
    height = gtk_spin_button_get_value_as_int(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user4));
    printf("Rectangle entered from (%d,%d), with length %d, height %d and magnitude %f\n",x1,y1,length,height,magnitude);
    fprintf(f,"Rectangle entered from (%d,%d), with length %d, height %d and magnitude %f\n",x1,y1,length,height,magnitude);
    for (i=x1; i < x1+length; i++) {
      for (j=y1; j < y1+height; j++) {
	if (i==x1 || i==x1+length-1 || j==y1 || j==y1+height-1) {
	  matrix[i][j]=magnitude;
	  //add if element is on rectangle boundary
	}
	if (filled) {
	  matrix[i][j]=magnitude;
	  //add if within boundary and is filled
	}
      }
    }
   break;
    
  case 3 : //Circle
    radius = gtk_spin_button_get_value(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_user3));
    printf("Circle entered with center (%d,%d), radius %f and magnitude %f\n",x1,y1,radius,magnitude);
    fprintf(f,"Circle entered with center (%d,%d), radius %f and magnitude %f\n",x1,y1,radius,magnitude);
 
     for (i=0; i < dimension; i++) { 
       for (j=0; j < dimension; j++) { 
     	double distance = sqrt((double)(i-y1)*(i-y1)+(j-x1)*(j-x1)); 
     	if (distance>radius-0.5 && distance<radius+0.5) { 
     	      matrix[i][j]=magnitude; 
     	    } else if (distance<radius+0.5 && filled) { 
     	      matrix[i][j]=magnitude; 
     	} 
       } 
     }	    
    break;
  }

  for (int i=0; i < dimension; i++) {
    for (int j=0; j < dimension; j++) {
      if (matrix[i][j]==100000) {
	printf("0.00 "); fprintf(f,"0.00");
      } else {
	printf("%.2f ", matrix[i][j]); fprintf(f,"%.2f ", matrix[i][j]);
      }
    }
    printf("\n"); fprintf(f,"\n");
  }
fclose(f);
}

//Takes dimension of matrix and produces square matrix on text file
void on_btn_matrix_clicked(GtkButton *button, app_widgets *app_wdgts) {

  //stores integer read from spin button widget
  dimension = gtk_spin_button_get_value_as_int(GTK_SPIN_BUTTON(app_wdgts->w_sbtn_quantity));
  
  //outputs dimension and initialises matrix elements
  printf("Matrix dimension is %d\n", dimension);
    for (int i=0; i < dimension; i++) {
      for (int j=0; j < dimension; j++) {
	matrix[i][j]=100000; //100000 denotes unknown value (outwith acceptable potential range)
      }
   }
    f=fopen("log.txt","w");
}

void on_btn_generate_clicked (GtkButton *button, app_widgets *app_wdgts) {
  
  FILE *fp;
  fp = fopen("matrix.txt","w");
  f = fopen("log.txt","a");

  for (int i=0; i < dimension; i++) {
    for (int j=0; j < dimension; j++) {
      if (matrix[i][j] == 100000) {
	fprintf(fp, "#@");
      } else {
        fprintf(fp, "%.2f@", matrix[i][j]);
      }
    }
    fprintf(fp,"\n");
  }
  fclose(fp);
  printf("Matrix successfully outputted to matrix.txt!\n");
  fprintf(f,"Matrix successfully outputted to matrix.txt!\n");
  fclose(f);
}
