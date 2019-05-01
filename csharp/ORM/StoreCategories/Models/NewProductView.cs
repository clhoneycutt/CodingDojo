using System.Collections.Generic;
using StoreCategories.Models;

namespace StoreCategories.Models
{
    public class NewProductView
    {
        public Product Product {get;set;}
        public IEnumerable<Product> Products {get;set;}
    }
}