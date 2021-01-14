#include<iostream>
#include<vector>

using namespace std;

class FixedPointTheorem{
	public:
		double cycleRange(double R){
			double cur = 0.25;

			for(int i=0; i<201000; i++)
				cur = R*cur*(1-cur);

			double max = -999999999.9;
			double min = 999999999.9;

			for(int i=0; i<1000; i++){
				cur = R*cur*(1-cur);
				if(cur>max) max = cur;
				if(cur<min) min = cur;
			}
			return max-min;		
		}
};
