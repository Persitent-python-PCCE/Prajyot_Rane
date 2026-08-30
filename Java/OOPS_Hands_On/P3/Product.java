package OOPS_Hands_On.P3;
import java.util.ArrayList;
import java.util.List;
 
class Bill {
    private List<Product> products = new ArrayList<>();
 
    public void addProduct(Product p) {
        // TODO: add to list
    }
 
    public void generateBill() {
        // TODO: print header
        //       loop over products — call display() (polymorphic)
        //       sum calculateFinalPrice() (polymorphic)
        //       print grand total formatted to 2 decimals
    }
 
    public static void main(String[] args) {
        // TODO:
        // 1. (Teaching moment) Uncomment the line below and observe the
        //    compile error — abstract classes cannot be instantiated:
        //    // Product p = new Product("X", "Y", 100, 1);
        //
        // 2. Create Grocery, Electronics, and Clothing instances
        //    matching the sample input.
        // 3. Add all products to a Bill.
        // 4. Call bill.generateBill().
    }
}
public abstract class Product {
    protected String productId;
    protected String name;
    protected double basePrice;   // per unit
    protected int quantity;
 
    public Product(String productId, String name, double basePrice, int quantity) {
        // TODO: initialize fields
        this.productId=productId;
        this.name=name;
        this.basePrice=basePrice;
        this.quantity=quantity;
    }
 
    // Each category MUST implement its own pricing logic
    public abstract double calculateFinalPrice();
 
    // Each category returns its label ("Grocery", "Electronics", "Clothing")
    public abstract String getCategory();
 
    // Concrete method reused by all subclasses
    public void display() {
        System.out.println("productId:"+productId+" | name"+name+" | category: | qty"+quantity+" | base:"+basePrice+" | final");
        // TODO: print productId | name | category | qty | base | final
    }
}

class Grocery extends Product {
    private static final double GST_RATE = 5.0;
    private static final int BULK_QTY = 10;
    private static final double BULK_DISCOUNT = 5.0;
 
    Grocery(String productId, String name, double basePrice, int quantity) {
        // TODO: super(...)
        super(productId,name,basePrice,quantity);
    }
 
    @Override
    public double calculateFinalPrice() {
        // TODO: gross = basePrice * quantity
        //       if quantity > BULK_QTY, apply BULK_DISCOUNT
        //       apply GST_RATE and return
        double gross = basePrice * quantity;
        if(quantity>BULK_QTY && quantity>BULK_DISCOUNT)
        {
            gross*=GST_RATE;
        }
        return 0;
    }
 
    @Override
    public String getCategory() { return "Grocery"; }
}
class Electronics extends Product {
    private static final double GST_RATE = 18.0;
    private int warrantyMonths;
 
    Electronics(String productId, String name, double basePrice,
                       int quantity, int warrantyMonths) {
        // TODO: super(...); this.warrantyMonths = warrantyMonths;
        super(productId,name,basePrice,quantity)
        this.warrantyMonths=warrantyMonths;
    }
 
    @Override
    public double calculateFinalPrice() {
        // TODO: (basePrice * quantity) with 18% GST
        double FinalPrice=basePrice*quantity*GST_RATE;
        System.out.println("Final Price:"+FinalPrice);
        return 0;
    }
 
    @Override
    public String getCategory() { return "Electronics"; }
 
    public int getWarrantyMonths() { return warrantyMonths; }
}
 class Clothing extends Product {    private static final double GST_RATE = 12.0;
    private static final double SEASONAL_DISCOUNT = 20.0;
 
    Clothing(String productId, String name, double basePrice, int quantity) {
        // TODO: super(...)
        super(productId,name,basePrice,quantity);
    }
 
    @Override
    public double calculateFinalPrice() {
        // TODO: gross = basePrice * quantity
        //       apply 20% seasonal discount, then 12% GST
        double FinalPrice=basePrice*quantity*0.2*0.12;
        System.out.println("Final Price:"+FinalPrice);
        return 0;
    }
 
    @Override
    public String getCategory() { return "Clothing"; }
}
