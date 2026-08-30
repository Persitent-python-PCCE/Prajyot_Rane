class Account {
    protected String accountNumber;
    protected String holderName;
    protected double balance;
 
    public Account(String accountNumber, String holderName, double balance) {
        this.accountNumber=accountNumber;
        this.holderName=holderName;
        this.balance=balance;
    }
 
    // ---- Overloaded deposit methods ----
    public void deposit(double amount) {
        this.balance+=amount;
        System.out.println("Deposit successful."+accountNumber+ "balance:"+balance);
    }
 
    public void deposit(double amount, String mode) {
        if (amount>0)
        {   
            this.balance+=amount;
            System.out.printf("Deposit via"+mode+" successful."+accountNumber+" balance: "+balance+"\n");
        }
    }
 
    public void deposit(double amount, String mode, String reference) {
         if (amount>0)
        {
            this.balance+=amount;
            System.out.printf("Deposit via"+mode+" successful."+accountNumber+" balance: "+balance+"Reference"+reference+"\n");
        }    
    }
 
    // ---- Methods intended to be overridden ----
    public boolean withdraw(double amount) {
        if (balance>amount)
        {
            balance-=amount;
            return true;
        }
        return false;
    }
 
    public double calculateInterest() {
        return 0;
    }
 
    public void displayDetails() {
        System.out.printf("AccountNo:%s Holdername:%s Balance:%s \n"+accountNumber,holderName,balance);
    }
}


class SavingsAccount extends Account {
    private double minBalance;
    private double interestRate;
 
    public SavingsAccount(String accountNumber, String holderName, double balance) {
        super(accountNumber, holderName, balance);
        minBalance = 1000;
        interestRate = 4.0;
    }
 
    @Override
    public boolean withdraw(double amount) {
        if(balance-amount>=minBalance)
        {
            balance-=amount;
            return true;
        }
        else
        {
            System.out.println("Withdrawal denied. Minimum balance of"+minBalance+" must be maintained.\n");
            return false;
        }
    }
 
    @Override
    public double calculateInterest() {
        double intres= balance * interestRate / 100;
        System.out.println("Interest for"+accountNumber+":"+intres);
        return intres;
    }
 
    @Override
    public void displayDetails() {
        // TODO: print with Type=Savings and minBalance
        System.out.println("Account:"+accountNumber+" Holder:"+holderName+"Balance:"+balance+ "| Type: Savings | Min Balance: 1000.0\n");
    }
}

class CurrentAccount extends Account {
    private double overdraftLimit;
 
     CurrentAccount(String accountNumber, String holderName, double balance) {
        super(accountNumber,holderName,balance);
         overdraftLimit=10000;
        // TODO: super(...); overdraftLimit = 10000;
    }
 
    @Override
    public boolean withdraw(double amount) {
        // TODO: allow if (balance - amount) >= -overdraftLimit
        if (balance - amount >= -overdraftLimit)
        {
            balance-=amount;
            System.out.println("overdraft used"+accountNumber+"balance:"+balance);

        }
        //       print "Withdrawal successful (overdraft used)." when balance goes negative
        System.out.println("Withdrawal successful");
        return false;
    }
 
    @Override
    public double calculateInterest() {
        // TODO: print "Interest not applicable ..." and return 0
        System.out.println("Interest not applicable ...");
        return 0;
    }
 
    @Override
    public void displayDetails() {
        // TODO: print with Type=Current and overdraftLimit
        System.out.println("Account:"+accountNumber+" Holder:"+holderName+"Balance:"+balance+ "| Type: Current | Overfraft Limit:"+overdraftLimit);
    }
}

class BankDemo {
    public static void main(String[] args) {

        SavingsAccount acc1=new SavingsAccount("SB001", "Arul",5000);
        CurrentAccount acc2=new CurrentAccount("CA001", "Priya",20000);
        acc1.deposit(2000);
        acc2.deposit(5000,"UPI");
        acc1.deposit(3000,"Cheque","CHQ12345");


        acc1.withdraw(9500);
        acc2.withdraw(30000);

        acc1.calculateInterest();
        acc2.calculateInterest();
        acc1.displayDetails();
        acc2.displayDetails();
        

        // TODO:
        // 1. Create one SavingsAccount and one CurrentAccount.
        // 2. Call all three overloaded deposit() forms.
        // 3. Trigger a failing withdraw() on Savings and a
        //    successful (overdraft) one on Current.
        // 4. Store both in an Account[] and loop — call
        //    calculateInterest() and displayDetails() on
        //    Account references (runtime polymorphism).
    }
}
