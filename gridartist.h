#ifndef _GRIDARTIST_
#define _GRIDARTIST_

#define TEMPERATURE_RATIO 40.0f
#define COLOR_RATIO 120.0f
#define GRID_SIZE 25
#include <iostream>
using namespace std;
#include <GL/glut.h>    // Header File For The GLUT Library 
#include <GL/gl.h>	// Header File For The OpenGL32 Library
#include <GL/glu.h>	// Header File For The GLu32 Library
#include "SDL.h"
#include <stdio.h>      // Header file for standard file i/o.
#include <stdlib.h>     // Header file for malloc/free.
class GridArtist
{
	private:

	public:
	GridArtist();
	void DrawGrid( int** thegrid);
	void DrawSlot(int temperature);
};
#endif
