using System.Collections.Generic;
using StoreCategories.Models;

namespace StoreCategories.Models
{
    public class AddCategorytoProductView
    {
        public Product Product {get;set;}
        public IEnumerable<Category> Categories {get;set;}
    }
}