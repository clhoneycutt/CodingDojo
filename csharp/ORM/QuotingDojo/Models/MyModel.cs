using System;
using System.ComponentModel.DataAnnotations;

namespace QuotingDojo.Models
{
    public class Entry
    {
        [Required]
        public string Name {get;set;}
        [Required]
        public string Quote{get;set;}
    }
}