using System;
using System.ComponentModel.DataAnnotations;

namespace StoreCategories.Models
{
    public class Association
    {
        [Key]
        public int AssociationID {get;set;}
        public int ProductID {get;set;}
        public int CategoryID {get;set;}
        public Product Product {get;set;}
        public Category Category {get;set;}
    }
}