using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace WeddingPlanner.Models
{
    [Table("guests")]
    public class Guest
    {
        [Key]
        public int GuestID {get;set;}
        public int UserID {get;set;}
        public int WeddingID {get;set;}

        public User User {get;set;}
        public Wedding Wedding {get;set;}
    }

}