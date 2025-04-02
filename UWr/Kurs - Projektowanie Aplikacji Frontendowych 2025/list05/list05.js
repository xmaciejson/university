/**
 * @typedef {object} Product
 * @property {number} id - Product ID
 * @property {string} name - Product name
 * @property {number} quantity - Number of units to purchase 
 * @property {Date} purchaseBy - Date by which the product should be purchased
 * @property {boolean} purchased - Indicates whether the product has been purchased
 * @property {number} [pricePerUnit] - Optional price per unit, only for purchased products
 */

/** @type {Product[]} */
let products = [];

/**
 * 
 * @param {string} name 
 * @param {number} quantity 
 * @param {Date} purchaseBy 
 * @param {boolean} purchased 
 * @param {number} [pricePerUnit]
 */


function addProduct(name, quantity, purchaseBy, purchased, pricePerUnit){
    const newProduct = {
        id: Math.floor(Math.random() * 100000000),
        name,
        quantity,
        purchaseBy: new Date(purchaseBy),
        purchased
    };

    if (purchased && pricePerUnit !== undefined){
        newProduct.pricePerUnit = pricePerUnit;
    }

    products.push(newProduct);
}

/**
 * 
 * @param {number} id 
 */

function removeProduct(id){
    const index = products.findIndex(function(product){
        return product.id === id;
    });

    if (index !== -1){
        products.splice(index, 1);
    }
    
}

/**
 * 
 * @param {number} id 
 * @param {string} newName 
 */

function editName(id, newName){
    const product = products.find(function(product){
        return product.id === id;
    })

    if (product){
        product.name = newName
    }
    else{
        console.log('Product not found');
    }
}

/**
 * 
 * @param {number} id 
 * @param {boolean} newStatus 
 */

function editStatus(id, newStatus){
    const product = products.find(function(product){
        return product.id === id;
    })

    if (product){
        product.purchased = newStatus
    }
    else{
        console.log('Product not found');
    }
}

/**
 * 
 * @param {number} id 
 * @param {number} newQuantity 
 */

function editQuantity(id, newQuantity){
    const product = products.find(function(product){
        return product.id === id;
    })

    if (product){
        product.quantity = newQuantity
    }
    else{
        console.log('Product not found');
    }
}

/**
 * 
 * @param {number} id 
 * @param {string} newDate 
 */

function editDate(id, newDate){
    const product = products.find(function(product){
        return product.id === id;
    })

    if (product){
        product.purchaseBy = new Date(newDate)
    }
    else{
        console.log('Product not found');
    }
}

/**
 * 
 * @param {number} id 
 * @param {string} direction - "up" or "down"
 * @returns 
 */

function moveProduct(id, direction){
    if (direction !== 'up' && direction !== 'down'){
        console.log('Wrong direction given!');
        return;
    }

    const index = products.findIndex(function(product){
        return product.id === id;
    })

    if (index === -1){
        console.log('Product not found')
        return;
    }

    if (direction === 'up' && index > 0){
        const temp = products[index];
        products[index] = products[index - 1];
        products[index - 1] = temp;
    }

    if (direction === 'down' && index < products.length - 1){
        temp = products[index];
        products[index] = products[index + 1];
        products[index + 1] = temp;
    }
}

/**
 * 
 * @returns {Array} - list of products that should be purchased today
 */

function buyToday(){
    const today = new Date();
    today.setHours(0,0,0,0);

    return products.filter(function(product){
        return !product.purchased && product.purchaseBy.getTime() === today.getTime();
    });

}

/**
 * 
 * @param {number} id 
 * @param {number} newPrice 
 * @returns 
 */

function addPrice(id, newPrice){
    const product = products.find(function(product){
        return product.id === id;
    })

    if (!product){
        console.log('Product not found');
        return;
    }

    if(!product.purchased){
        console.log('Cannot assign price because this product has not been purchase yet');
        return;
    }

    product.pricePerUnit = newPrice;
    console.log('Price assigned succesfully!');
}

/**
 * 
 * @param {string} dateString 
 * @returns {number} - total cost of purchased products on that day
 */

function calculatePrice(dateString){
    const dayDate = new Date(dateString);
    dayDate.setHours(0, 0, 0, 0);

    const purchasedProduct = products.filter(function(product){
        const productDate = new Date(product.purchaseBy);
        productDate.setHours(0,0,0,0)
        return product.purchased && productDate.getTime() === dayDate.getTime();
    });

    const totalCost = purchasedProduct.reduce(function(sum, product){
        if (product.pricePerUnit !== undefined){
            sum += product.pricePerUnit * product.quantity;
        }
        return sum;
    }, 0);

    return totalCost;

}

/**
 * 
 * @param {number[]} ids 
 * @param {function(Product): Product} func
 * @returns {Product[]}
 */

function formatProducts(ids, func) {
    products.forEach(function(product) {
        if (ids.includes(product.id)) {
            func(product); 
        }
    });
}


addProduct("Milk", 2, "2025-04-15", false);
addProduct("Bread", 1, "2025-04-16", true, 3.50);
addProduct("Eggs", 10, "2025-04-02", true, 2.00);
addProduct("Cheese", 1, "2025-04-02", true, 8.20);
console.log(products);
console.log('-------------------------------------------------------');

const productToRemove = products[1].id; 
removeProduct(productToRemove);
console.log(products);
console.log('-------------------------------------------------------');

const productToEdit = products[0].id; 
editName(productToEdit, "Milk 3,2%");
console.log(products[0]);
console.log('-------------------------------------------------------');

editStatus(productToEdit, true);
console.log(products[0]);
console.log('-------------------------------------------------------');

editQuantity(productToEdit, 3);
console.log(products[0]);
console.log('-------------------------------------------------------');

editDate(productToEdit, "2025-05-20");
console.log(products[0]);
console.log('-------------------------------------------------------');

moveProduct(products[1].id, 'up'); 
console.log(products);
console.log('-------------------------------------------------------');

moveProduct(products[1].id, 'down'); 
console.log(products);
console.log('-------------------------------------------------------');

const todayProducts = buyToday();
console.log(todayProducts);
console.log('-------------------------------------------------------');

addPrice(productToEdit, 2.99); 
console.log(products.find(function(p){
    return p.id === productToEdit;
}));
console.log('-------------------------------------------------------');

console.log(products)
const testDate = "2025-04-02"; 
const dailyCost = calculatePrice(testDate);
console.log(`Total cost: ${testDate}:`, dailyCost);
console.log('-------------------------------------------------------');

const productsToConvert = [products[0].id, products[1].id];
formatProducts(productsToConvert, function(product){
    product.quantity *= 2;
});
console.log(products);

