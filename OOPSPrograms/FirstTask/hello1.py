class StoreManagement:
    def __init__(self, Product_ID, Product_Name, Product_Price, Product_Quantity):
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.Product_Price = Product_Price
        self.Product_Quantity = Product_Quantity
        # Fix typo: prodect_details -> product_details
        self.product_details = {
            "ID": self.Product_ID,
            "Name": self.Product_Name,
            "Price": self.Product_Price,
            "Quantity": self.Product_Quantity,
        }

    def add_Product(self):
        # Use the correct attribute name
        product_holder = self.product_details
        # Use a relative path to ensure it works
        with open("d:\\diya.txt", "a") as f:
            f.write(f"Product ID:{product_holder.get('ID')}, "
                    f"Product name:{product_holder.get('Name')}, "
                    f"Product price:{product_holder.get('Price')}, "
                    f"Product Quantity:{product_holder.get('Quantity')}\n")
        print("Product added successfully.\n")  # Feedback to user
    
    def view_Single_id(self, single_ID):
     with open("d:\\products.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
          if single_ID in line:
            print(line)
            #with open("d:\\products.txt","w")  as f:
             #for line in lines:
              #  pass

Product_ID = input("Enter ID: ")
Product_Name = input("Enter Name: ")
Product_Price = input("Enter price: ")
Product_Quantity = input("Enter quantity: ")
st = StoreManagement(Product_ID, Product_Name, Product_Price, Product_Quantity)
st.add_Product()

while True:
    
    pick = int(input("Enter choice: "))

    match pick:
        case 1:
        
            st.add_Product()
        case 2:
             del_id= input("Enter id No to delete: ")
             st.delete_product(del_id)
                 
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice.\n")
