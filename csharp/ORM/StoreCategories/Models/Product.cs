using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace StoreCategories.Models
{
    public class Product
    {
       [Key]
       public int ProductID {get;set;}
       [Required]
       public string Name {get;set;}
       [Required]
       public string Description {get;set;}
       [Required]
       [RegularExpression("^[$]?[0-9]*(.)?[0-9]?[0-9]?$", ErrorMessage="Please enter a valid dollar amount")]
       public float Price {get;set;}
       public DateTime CreatedAt {get;set;} = DateTime.Now;
       public DateTime UpdatedAt {get;set;} = DateTime.Now;

       public List<Association> AssociatedCategories {get;set;}
    }
}