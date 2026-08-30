package OOPS_Hands_On;
class Employee
{
    String id;
    String name;
    long base_salary;
        Employee()
        {
            this.id="E000";
            this.name="Unknown";
        }
        Employee(String id,String name)
        {
            this.id=id;
            this.name=name;
            base_salary=15000;
        }

    public Employee(String id, String name, long base_salary) {
        this.id = id;
        this.name = name;
        this.base_salary = base_salary;
    }
        public void display()
        {
            System.out.printf("Employee Name: %s",this.name);
            System.out.printf("Employee ID: %s",this.id);
            System.out.printf("Base Salary: %s",this.base_salary);


        }
    }
class InternEmployee extends Employee
{
    long stipend;
    int duration;

    public InternEmployee() {
        stipend=8000;
        duration=6;
    }
     public InternEmployee(String id,String name) {
        super(id,name);  
        this.id=id;
        this.name=name;
     }
    
    public InternEmployee(String id,String name,long stipend,int duration ) {
        super(id,name);  
        this.id=id;
        this.name=name;
        this.stipend=stipend;
        this.duration=duration;
    }

@Override
    public void display(){
            System.out.printf("Employee Name: %s",this.name);
            System.out.printf("Employee ID: %s",this.id);
            System.out.printf("Stipend: %s",this.stipend);
            System.out.printf("Duration: %s",this.duration);
    }
}
class FullTimeEmployee extends Employee{
    long bonus;
    public FullTimeEmployee(String id,String name,long base_salary) {
        super(id,name,base_salary);
        this.id=id;
        this.name=name;
        this.base_salary=base_salary;
        bonus=5000;
    }
     public FullTimeEmployee(String id,String name,long base_salary,long bonus) {
        super(id,name,base_salary);
        this.id=id;
        this.name=name;
        this.base_salary=base_salary;
        this.bonus=bonus;
    }
    @Override
    public void display()
    {
        System.out.printf("Employee Name: %s",this.name);
        System.out.printf("Employee ID: %s",this.id);
        System.out.printf("Base Salary: %s",this.base_salary);
        System.out.printf("bonus: %s",this.bonus);
    }


    
}