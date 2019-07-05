using System.Collections.Generic;
using StoreCategories.Models;

namespace StoreCategories.Models
{
    public class AddProductToCategoryView
    {
        public Category Category {get;set;}
        public IEnumerable<Product> Products {get;set;}
    }
}