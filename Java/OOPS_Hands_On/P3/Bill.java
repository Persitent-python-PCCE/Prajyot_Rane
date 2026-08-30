
import java.util.ArrayList;
import java.util.List;
 
class Bill {
    private List<Product> products = new ArrayList<>();
    double total=0;
 
  public void addProduct(Product p) {
    products.add(p);
}
 
    public void generateBill() {
        // TODO: print header
        //       loop over products — call display() (polymorphic)
        //       sum calculateFinalPrice() (polymorphic)
        //       print grand total formatted to 2 decimals
        for(Product p:products)
        {
            p.display();
            total+=p.calculateFinalPrice();
        }
        System.out.println("============================");
    System.out.println("Total Items: " + products.size());
    System.out.printf("Grand Total: %.2f%n", total);
    }
 
    public static void main(String[] args) {

    Grocery g1 =
        new Grocery("G001", "Rice 5kg", 300, 3);

    Electronics e1 =
        new Electronics("E001", "Headphones", 2000, 1, 12);

    Clothing c1 =
        new Clothing("C001", "T-Shirt", 800, 2);

    Grocery g2 =
        new Grocery("G002", "Sugar 1kg", 50, 15);

    Bill bill = new Bill();

    bill.addProduct(g1);
    bill.addProduct(e1);
    bill.addProduct(c1);
    bill.addProduct(g2);

    bill.generateBill();
}
}
abstract class Product {
    protected String productId;
    protected String name;
    protected double basePrice;   // per unit
    protected int quantity;
 
    Product(String productId, String name, double basePrice, int quantity) {
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
    System.out.printf(
        "%s | %s | %s | Qty: %d | Base: %.1f | Final: %.2f%n",
        productId,
        name,
        getCategory(),
        quantity,
        basePrice * quantity,
        calculateFinalPrice()
    );
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
            gross = gross * (1 - BULK_DISCOUNT / 100);  
              }
               gross = gross * (1 + GST_RATE / 100);
        return gross;
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
        super(productId,name,basePrice,quantity);
        this.warrantyMonths=warrantyMonths;
    }
 
    @Override
    public double calculateFinalPrice() {
        // TODO: (basePrice * quantity) with 18% GST
 double gross = basePrice * quantity;
        return gross * (1 + GST_RATE / 100);
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
        
    double gross = basePrice * quantity;
    gross = gross * (1 - SEASONAL_DISCOUNT / 100);
    gross = gross * (1 + GST_RATE / 100);
        return gross;
    }
 
    @Override
    public String getCategory() { return "Clothing"; }
}
