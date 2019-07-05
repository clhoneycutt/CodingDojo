using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace WeddingPlanner.Models
{
    [Table("weddings")]
    public class Wedding
    {
        [Key]
        public int WeddingID {get;set;}
        public int OrganizerID {get;set;}
        public string Bride {get;set;}
        public string Groom {get;set;}
        public DateTime Date {get;set;}
        public string Address {get;set;}
        public DateTime CreatedAt{get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;
        public User Organizer {get;set;}
        public List<Guest> Guests {get;set;}
    }

}