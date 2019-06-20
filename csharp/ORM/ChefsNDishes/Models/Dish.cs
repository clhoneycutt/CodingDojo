using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ChefsNDishes.Models
{
    [Table("dishes")]
    public class Dish
    {
        [Key]
        public int DishID {get;set;}
        [Required]
        public int ChefID {get;set;}
        [Required(ErrorMessage="Dish name is required.")]
        [MinLength(2, ErrorMessage="Dish name must be at least 2 characters long.")]
        public string Name {get;set;}
        [Required(ErrorMessage="Must enter number of calories.")]
        [RegularExpression("([0-9]+)", ErrorMessage="Please enter a valid number.")]
        public int Calories {get;set;}
        public int Tastiness {get;set;}
        [Required(ErrorMessage="Please enter a description of the dish.")]
        [MinLength(15, ErrorMessage="The Description must be at least 15 characters")]
        public string Description {get;set;}
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;
        public Chef Chef {get;set;}

    }
}