using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace StoreCategories.Models
{
    public class Category
    {
        [Key]
        public int CategoryID {get;set;}
        [Required]
        public string Name {get;set;}
        [Required]
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;

        public List<Association> AssociatedProducts {get;set;}
    }
}