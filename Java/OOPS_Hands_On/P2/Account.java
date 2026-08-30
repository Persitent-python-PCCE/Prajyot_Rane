public class Account {
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
    }
 
    public void deposit(double amount, String mode) {
        if (amount>0)
        {   
            this.balance+=amount;
            System.out.printf("Deposit via <mode> successful. <accNo> balance: <bal>");
        }
    }
 
    public void deposit(double amount, String mode, String reference) {
         if (amount>0)
        {
            this.balance+=amount;
            System.out.printf("Deposit via <mode> successful. <accNo> balance: <bal>");
        }
        System.out.printf("Deposit via <mode> (Ref: <ref>) successful. ...");
    
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
        System.out.printf("AccountNo:%s Holdername:%s Balance:%s"+accountNumber,holderName,balance);
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
            System.out.println("Withdrawal denied. Minimum balance of <min> must be maintained.");
            return false;
        }
    }
 
    @Override
    public double calculateInterest() {
        // TODO: return balance * interestRate / 100
        
        return 0;
    }
 
    @Override
    public void displayDetails() {
        // TODO: print with Type=Savings and minBalance
    }
}
