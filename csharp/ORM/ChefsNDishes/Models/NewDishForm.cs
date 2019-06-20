using System.Collections.Generic;
using ChefsNDishes.Models;

namespace ChefsNDishes
{
    public class NewDishForm  
    {  
        public IEnumerable<Chef> Chefs { get; set; }  
        public Dish Dish { get; set; }
    }  
}