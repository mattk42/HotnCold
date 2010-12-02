#include "gridartist.h"

GridArtist::GridArtist()
{
	return;
}

void GridArtist::DrawGrid(int ** thegrid)
{
	glPushMatrix();
	glTranslatef(((float)GRID_SIZE)/  -1.0f,	((float)GRID_SIZE)/1.0f,0.0f);
	for(int i = 0; i < GRID_SIZE;i++)
	{	
		glTranslatef(2.0f,0.0f,0.0f);
		glPushMatrix();
		for(int j = 0; j < GRID_SIZE;j++)
		{
			glTranslatef(0.0f,-2.0f,0.0f);
			DrawSlot(thegrid[i][j]);
		}
		glPopMatrix();
	}
	glPopMatrix();
}

void GridArtist::DrawSlot(int temperature)
{
	cout << temperature << endl;
	int wasneg = temperature;
	if(temperature >= 0) glColor3f(1.0f * ((float)temperature) / COLOR_RATIO , 0.0, 0.0);
	if(temperature < 0) 
	{
		temperature *= -1;
		glColor3f(0.0 , 0.0, 1.0f * ((float)temperature) / COLOR_RATIO);
	}
   	glBegin(GL_QUADS);

	/* Front Face */
	glVertex3f( -1.0f, -1.0f, 0.0f );
	glVertex3f(  1.0f, -1.0f, 0.0f );
	glVertex3f(  1.0f,  1.0f, 0.0f );
	glVertex3f( -1.0f,  1.0f, 0.0f );




	/* Top Face */
	glVertex3f( -1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f( -1.0f,  1.0f,  0.0f);
	glVertex3f(  1.0f,  1.0f,  0.0f);
	glVertex3f(  1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );

	/* Left Face */
	glVertex3f( -1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f( -1.0f, -1.0f,  0.0f);
	glVertex3f( -1.0f,  1.0f,  0.0f);
	glVertex3f( -1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );

	//OTHER GUYZ
	if(wasneg >= 0) glColor3f(1.0f * ((float)temperature-10) / COLOR_RATIO , 0.0, 0.0);
	if(wasneg < 0) 
	{
		glColor3f(0.0 , 0.0, 1.0f * ((float)temperature+10) / COLOR_RATIO);
	}
	
	/* Bottom Face */
	glVertex3f( -1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f(  1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f(  1.0f, -1.0f,  0.0f);
	glVertex3f( -1.0f, -1.0f,  0.0f);

	/* Right face */
	glVertex3f( 1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f( 1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f( 1.0f,  1.0f,  0.0f);
	glVertex3f( 1.0f, -1.0f,  0.0f);

	/* Back Face */
	glVertex3f( -1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f( -1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f(  1.0f,  1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );
	glVertex3f(  1.0f, -1.0f, 1.0f * ((float)temperature) / TEMPERATURE_RATIO );


   	glEnd( );
}
