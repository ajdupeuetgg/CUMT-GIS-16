#include "Point.h"
int main()
{
    Point P1(6,3);
    cout<<"P1.x="<<P1.get_x()<<endl;
    cout<<"P1.y="<<P1.get_y()<<endl;
    
    int x,y;
    cout<<"请输入P2点的x坐标：";
    cin>>x;
    cout<<"请输入P2点的y坐标：";
    cin>>y;
    Point P2(x,y);
    cout<<"P2.x="<<P2.get_x()<<endl;
    cout<<"P2.y="<<P2.get_y()<<endl;
    
    
    Point P3(8,18);
    cout<<P3;
    
    
    Point *p4=new Point(10,20);
    cout<<"p4.x="<<p4->get_x()<<endl<<"p4.y="<<p4->get_y()<<endl;
    
    
    Point P5(1,1);
    Point P6(2,2);
    Point P7=P5+P6;
    cout<<"p7.x="<<P7.get_x()<<endl<<"p7.y="<<P7.get_y()<<endl;
    
    int pause;
    cin>>pause;

}
