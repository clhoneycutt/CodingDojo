using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using ChefsNDishes.Models;

namespace ChefsNDishes.Models
{
    
    
    [Table("chefs")]
    public class Chef
    {
        [Key]
        public int ChefID {get;set;}
        [Required]
        [MinLength(2, ErrorMessage="Your first name must be at least 2 letters long.")]
        public string FirstName {get;set;}
        [Required]
        [MinLength(2, ErrorMessage="Your last name must be at least 2 letters long.")]
        public string LastName {get;set;}
        [DisplayFormat(DataFormatString = "{0:yyyy-MM-dd}", ApplyFormatInEditMode = true)]
        public DateTime DateOfBirth {get;set;}
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;
        [NotMapped]
        public int Age
        {
            get
            { 
                int age = 0;  
                age = DateTime.Now.Year - DateOfBirth.Year;  
                if (DateTime.Now.DayOfYear < DateOfBirth.DayOfYear)  
                    age = age - 1;
                return age; 
            }
        }
        public List<Dish> Dishes {get;set;}
    }

    
}