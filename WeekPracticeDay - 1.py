class Shop:
    def __init__( self, name ) :
        self.name = name
        self.products = []
    
    def add_product( self, pname, price, qty ) :
        product = Product( pname, price, qty )
        self.products.append(product)
    
    def buy_product( self, pname ) :
        print( pname )
        F = False 
        for i in self.products:
            if i.name == pname :
                F = True
                print('OK')
                var = int(input('Enter qty : '))
                print(var)
                if var < i.qty :
                    i.qty -= var
                    print( i.qty )
                    break
            
        if F == False :
            print('Not Found')
            
    def __repr__(self) -> str:
        print( 'Our Products : ' )
        for i in self.products:
            print( i.name, i.price, i.qty )
        return f'Task Completed'
    
class Product :
    def __init__(self, name, price, qty) -> None:
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self) -> str:
        return f'Product : {self.name}, Price : {self.price} quantity : { self.qty }'


p = Shop( 'Shop - 1' )
p.add_product( 'Apple', 1000, 4 )
p.add_product( 'Orange', 2000, 2 )
p.add_product( 'Date', 3000, 3 )
print ( p.products )
print ( p )
p.buy_product( 'Apple')
print ( p )