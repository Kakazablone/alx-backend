import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Create an array of products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Create a Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

// Function to get item by ID
const getItemById = (id) => {
  return listProducts.find(product => product.id === id);
};

// Route to list all products
app.get('/list_products', (req, res) => {
  const products = listProducts.map(({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price,
    initialAvailableQuantity: stock,
  }));
  res.json(products);
});

// Function to reserve stock by ID
const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

// Async function to get current reserved stock by ID
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
};

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);
  
  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: product.stock - reservedStock,
  });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  
  if (product.stock - reservedStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  reserveStockById(itemId, reservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
