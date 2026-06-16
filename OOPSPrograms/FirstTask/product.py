class StoreManagement:
    def __init__(self, Product_ID, Product_Name, Product_Price, Product_Quantity):
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.Product_Price = Product_Price
        self.Product_Quantity = Product_Quantity
        
        self.product_details = {
            "ID": self.Product_ID,
            "Name": self.Product_Name,
            "Price": self.Product_Price,
            "Quantity": self.Product_Quantity,
        }

    def add_Product(self):
        
        product_holder = self.product_details
        
        with open("d:\\products.txt", "a") as f:
            f.write(f"Product ID:{product_holder.get('ID')}, "
                    f"Product name:{product_holder.get('Name')}, "
                    f"Product price:{product_holder.get('Price')}, "
                    f"Product Quantity:{product_holder.get('Quantity')}\n")
        print("Product added successfully.\n")
    def view_All_products(self):
        with open("D:\\products.txt", "r") as f:
               print(f.read())

    def view_Single_id(self, single_ID):
     with open("d:\\products.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
          if single_ID in line:
            print(line)
            
    print("Product ID not found")
            

    def update_products(self, single_ID,new_data):
     with open("d:\\products.txt", "r") as f:
        lines = f.readlines()
        updated_lines=[]
        for line in lines:
          if single_ID in line:
            updated_lines.append(new_data+'\n')
          else:
            updated_lines.append(line)  
            with open("d:\\products.txt","w")  as f:
                f.writelines(updated_lines)
    

    def count_product(self):

        
        with open("D:\\products.txt","r") as f:
            lines=f.readlines()
            print("total number of items: ",len(lines))

    def delete_product(self,id_to_delete) :
    
        with open("D:\\products.txt","r") as f:
            lines=f.readlines()
        with open("d:\\products.txt","w")  as f:
            for line in lines:
                Product_ID=line.strip().split(",")
                ProID=Product_ID[0].split(":")[-1].strip()
                if ProID!=id_to_delete:
                    f.write(line)
                  
                
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
            st.view_All_products()   
        case 3:
            del_id= input("Enter id No to delete: ")
            st.delete_product(del_id)
        case 4:
            single_ID = input("Enter ID: ")
            st.view_Single_id(single_ID ) 
        case 5:
             single_ID = input("Enter ID to update: ")
             st.view_Single_id(single_ID )
                 
             new_data = input("Enter product id: , product_name: ,product_price ,product_quantity ")
             st.update_products(single_ID, new_data)

        case 6:
             st.count_product()
        case 7:
            print("Exiting...")
            break
        case _:
            print("Invalid choice.\n")
