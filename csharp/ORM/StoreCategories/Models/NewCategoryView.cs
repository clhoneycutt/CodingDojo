using System.Collections.Generic;
using StoreCategories.Models;

namespace StoreCategories.Models
{
    public class NewCategoryView
    {  
        public Category Category { get; set; }  
        public IEnumerable<Category> Categories { get; set; }
    }  
}