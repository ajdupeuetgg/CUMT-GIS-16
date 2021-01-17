#ifndef POINT_H
#define POINT_H
#include<iostream>
using namespace std;

class Point
{
private:
    int x;
    int y;
public:
    Point(int a,int b);
    ~Point();
    int get_x();
    int get_y();
private:
    friend ostream& operator<<(ostream& out,Point& p);
public:
    void set_x(int a);
    void set_y(int b);
    Point operator+(Point p);
};

Point::Point(int a,int b)
{
    x=a;
    y=b;
}

Point::~Point(){}

int Point::get_x()
{
    return x;
}
int Point::get_y()
{
    return y;
}

ostream& operator<<(ostream& out,Point& p)
{
    return out<<"private p.x="<<p.x<<endl<<"private p.y="<<p.y<<endl;
}

void Point::set_x(int a)
{
    x=a;
}
void Point::set_y(int b)
{
    y=b;
}
Point Point::operator+(Point p)
{
    Point ResultPoint(0,0);
    ResultPoint.set_x(x+p.get_x());
    ResultPoint.set_y(y+p.get_y());
    return ResultPoint;
}

#endif
