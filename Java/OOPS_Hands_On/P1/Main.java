package OOPS_Hands_On;

public class Main {
    public static void main(String[] args) {
        Employee emp1=new Employee();
        emp1.display();
        Employee emp2=new Employee("E101", "Ravi");
        emp2.display();
        FullTimeEmployee f1=new FullTimeEmployee("E201", "Meena", 40000);
        f1.display();
        FullTimeEmployee f2=new FullTimeEmployee("E202", "Karthik", 50000, 8000);
        f2.display();
        InternEmployee e1=new InternEmployee("E301", "Divya");
        e1.display();
        InternEmployee e2=new InternEmployee("E302", "Suresh", 12000, 6);
        e2.display();
 

 





    }
    
}
