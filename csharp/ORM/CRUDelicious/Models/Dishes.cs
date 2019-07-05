using System;
using System.ComponentModel.DataAnnotations;

namespace CRUDelicious.Models
{
    public class Dish
    {
        [Key]
        public int DishID {get;set;}
        [Required]
        public string Name {get;set;}
        [Required]
        public string Chef {get;set;}
        [Required]
        [Range(1, 6)]
        public int Tastiness {get;set;}
        [Required]
        [RegularExpression("([0-9]+)")]
        public int Calories {get;set;}
        [Required]
        public string Description {get;set;}
        [Required]
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        [Required]
        public DateTime UpdatedAt {get;set;} = DateTime.Now;

        public Dish()
        {
            CreatedAt = DateTime.Now;
            UpdatedAt = DateTime.Now;
        }
    }
}