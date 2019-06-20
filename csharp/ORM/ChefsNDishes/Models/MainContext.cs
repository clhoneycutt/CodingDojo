using Microsoft.EntityFrameworkCore;
 
namespace ChefsNDishes.Models
{
    public class MyContext : DbContext
    {
        // base() calls the parent class' constructor passing the "options" parameter along

        public MyContext(DbContextOptions options) : base(options) { }

        public DbSet<Chef> Chefs {get;set;}
        public DbSet<Dish> Dishes {get;set;}
    }
}